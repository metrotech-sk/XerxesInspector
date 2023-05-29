# This Python file uses the following encoding: utf-8

import sys
from typing import List

from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PySide6 import QtCore
from dataclasses import dataclass, field
from datetime import datetime


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from utils import devIdTable
import logging
import serial
import time
import xerxes_protocol as xp

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    # log time, function and line number
    format="%(asctime)s %(funcName)s:%(lineno)d %(message)s",
    # save log to file as well
    handlers=[
        logging.FileHandler("xerxes.log"),
        logging.StreamHandler()
    ]
)


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.setSizePolicy(
            QSizePolicy.Expanding, 
            QSizePolicy.Expanding
            )
        self.updateGeometry()
        self.restyle()

    def restyle(self):
        
        # Set the background color of the plot area
        self.axes.set_facecolor("#d3dae3")

        # Set the color of the axes
        self.axes.spines['bottom'].set_color("#222b2e")
        self.axes.spines['top'].set_color("#222b2e") 
        self.axes.spines['right'].set_color("#222b2e")
        self.axes.spines['left'].set_color("#222b2e")
        
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Value')

        self.axes.legend(
            loc='upper left',
        )
        
        self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

class DiscoverComPorts(QtCore.QThread):
    sigAvailablePorts = QtCore.Signal(str)
    sigLog = QtCore.Signal(str)
    sigDone = QtCore.Signal(bool)

    def run(self):
        """Discover the COM port of the Xerxes device."""

        for portnum in range(1,100):
            try:
                portname = f"COM{portnum}"
                self.sigLog.emit(f"Trying port {portname}")
                port = serial.Serial(portname, timeout=.02, baudrate=115200)
                port.close()
                self.sigAvailablePorts.emit(portname)
                self.sigLog.emit(f"Found port: {portname}")
                log.info(f"Found port: {portname}")

            except serial.SerialException:
                pass
        
        self.sigLog.emit("Done")
        self.sigDone.emit(True)


class DiscoverLeaves(QtCore.QThread):
    sigAvailableLeaves = QtCore.Signal(xp.Leaf)
    sigLog = QtCore.Signal(str)
    sigDone = QtCore.Signal(bool)

    def __init__(self, port, range=6):
        super().__init__()
        self.port = port
        self._r = range
    
    def run(self):
        log.info(f"Discovering leaves on port {self.port}")

        self._xn = xp.XerxesNetwork(self.port)
        self._xn.init(timeout=0.05)
        self._xr = xp.XerxesRoot(0xfe, self._xn)

        for leaf_addr in range(0, self._r):
            leaf = xp.Leaf(leaf_addr, self._xr)
            try:
                log.info(f"Trying leaf {leaf_addr}")
                self.sigLog.emit(f"Looking for sensor with address: {leaf_addr}")
                leaf.ping()
                self.sigAvailableLeaves.emit(leaf)
                self.sigLog.emit(f"Found sensor: {leaf}")
            except TimeoutError:
                pass

        self.sigLog.emit("Done")
        self.sigDone.emit(True)


class PollSensor(QtCore.QThread):
    sigDataY = QtCore.Signal(list)
    sigLog = QtCore.Signal(str)

    def __init__(self, leaf: xp.Leaf):
        super().__init__()
        self.leaf = leaf
    
    def run(self):
        while True:
            try:
                cfg = self.leaf.device_config & 0x01  # free run bit
                if not cfg:  # free run is disabled -> read data
                    # need to sync first
                    self.leaf.root.sync()
                
                log.info(f"Reading sensor data from {self.leaf.address}")
                pv0 = self.leaf.pv0
                pv1 = self.leaf.pv1
                pv2 = self.leaf.pv2
                pv3 = self.leaf.pv3
                self.sigDataY.emit([pv0, pv1, pv2, pv3])
            except TimeoutError:
                self.sigLog.emit("TimeoutError while reading sensor data")
            except Exception as e:
                self.sigLog.emit(f"Exception while reading sensor data: {e}")
            time.sleep(1)

@dataclass
class SensorData:
    x: List[float] = field(default_factory=list)
    y: List[float] = field(default_factory=list)
    y2: List[float] = field(default_factory=list)
    y3: List[float] = field(default_factory=list)
    y4: List[float] = field(default_factory=list)

    def clear(self):
        self.x.clear()
        self.y.clear()
        self.y2.clear()
        self.y3.clear()
        self.y4.clear()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # bind rescan port button
        self.ui.buttonRescanPort.clicked.connect(self.rescanPort)
        self.ui.buttonRescanLeaves.clicked.connect(self.rescanLeaves)

        self.ui.listWidgetLeaves.clicked.connect(self.leafSelected)

        self.attributes = []
        for attr in dir(xp.XerxesMemoryMap):
            if not attr.startswith("_"):
                self.attributes.append(attr)

        self.ui.progressBar.setVisible(False)

        self.ui.mplCanvas = MplCanvas(self.ui.tabValues)
        self.ui.mplCanvas.setObjectName(u"mplCanvas")
        self.ui.horizontalLayout_6.addWidget(self.ui.mplCanvas)

        self.sensorData = SensorData()
        self.sensorData.x, self.sensorData.y = [], []

        self.ui.tabWidget.currentChanged.connect(self.tabChanged)

        self.rescanPort()

    def updatePlot(self, _v=None): 
        self.sensorData.x.append(datetime.now())
        self.sensorData.y.append(_v[0])
        self.sensorData.y2.append(_v[1])
        self.sensorData.y3.append(_v[2])
        self.sensorData.y4.append(_v[3])

        if len(self.sensorData.x) > 60:
            self.sensorData.x.pop(0)
            self.sensorData.y.pop(0)
            self.sensorData.y2.pop(0)
            self.sensorData.y3.pop(0)
            self.sensorData.y4.pop(0)

        self.ui.mplCanvas.axes.clear()

        self.ui.mplCanvas.axes.plot(
            self.sensorData.x,
            self.sensorData.y,
            color="#4fa08b",
            label="pv0"
        )
        if any(self.sensorData.y2):
            self.ui.mplCanvas.axes.plot(
                self.sensorData.x,
                self.sensorData.y2,
                color="#f2b134",
                label="pv1"
            )

        if any(self.sensorData.y3):
            self.ui.mplCanvas.axes.plot(
                self.sensorData.x,
                self.sensorData.y3,
                color="#f2b134",
                label="pv2",
                linestyle="dashed"
            )

        if any(self.sensorData.y4):
            self.ui.mplCanvas.axes.plot(
                self.sensorData.x,
                self.sensorData.y4,
                color="#f2b",
                label="pv3"
            )

        self.ui.mplCanvas.restyle()
        self.ui.mplCanvas.draw()

    def updateStatusBar(self, msg):
        """Update the status bar with the given message."""
        self.statusBar().showMessage(msg)
        QtCore.QTimer.singleShot(3000, self.statusBar().clearMessage)

    def rescanPort(self, _v=None):
        """Discover the COM port of the Xerxes device."""
        self.ui.comboBoxComPorts.clear()
        self.ui.progressBar.setVisible(True)
        try:
            self.port.close()
        except AttributeError:
            pass

        self.threadDiscoverComPorts = DiscoverComPorts()
        self.threadDiscoverComPorts.sigAvailablePorts.connect(
            self.ui.comboBoxComPorts.addItem
        )
        self.threadDiscoverComPorts.sigLog.connect(
            self.updateStatusBar
        )
        self.threadDiscoverComPorts.sigDone.connect(
            self.ui.buttonRescanPort.setEnabled
        )
        self.threadDiscoverComPorts.sigDone.connect(
            self.ui.buttonRescanLeaves.setEnabled
        )

        # hide progress bar when done
        def _f():
            self.ui.progressBar.setVisible(False)
        self.threadDiscoverComPorts.sigDone.connect(
            _f
        )

        def _f():
            self.rescanLeaves()

        self.threadDiscoverComPorts.sigDone.connect(
            _f
        )
        self.threadDiscoverComPorts.start()


    def _get_leaves(self) -> None:
        """Discover the leaves connected to the Xerxes device."""
        self.leaves = []
        log.info(f"Discovering leaves on port {self.port}")

        self._xn = xp.XerxesNetwork(self.port)
        self._xn.init()
        self._xr = xp.XerxesRoot(0xfe, self._xn)

        for leaf_addr in range(0, 5):
            leaf = xp.Leaf(leaf_addr, self._xr)
            try:
                log.info(f"Trying leaf {leaf_addr}")
                leaf.ping()
                self.leaves.append(leaf)
            except TimeoutError:
                pass

    def rescanLeaves(self, port=None):
        log.info(f"Selected port: {port}")
        try:
            self.port.close()
        except AttributeError:
            pass
        self.port = serial.Serial(port or self.ui.comboBoxComPorts.currentText())
        self.ui.listWidgetLeaves.clear()
        self.ui.progressBar.setVisible(True)
        self.ui.buttonRescanLeaves.setEnabled(False)
        self.ui.listWidgetLeaves.setEnabled(False)

        self.threadDiscoverLeaves = DiscoverLeaves(self.port)
        self.leaves = []

        def _f(leaf: xp.Leaf):
            self.ui.listWidgetLeaves.addItem(str(leaf))
            self.leaves.append(leaf)
        self.threadDiscoverLeaves.sigAvailableLeaves.connect(
            _f
        )

        def _f():
            self.ui.progressBar.setVisible(False)
        self.threadDiscoverLeaves.sigDone.connect(
            _f
        )
        self.threadDiscoverLeaves.sigLog.connect(
            self.updateStatusBar
        )
        self.threadDiscoverLeaves.sigDone.connect(
            self.ui.buttonRescanLeaves.setEnabled
        )
        self.threadDiscoverLeaves.sigDone.connect(
            self.ui.listWidgetLeaves.setEnabled
        )
        self.threadDiscoverLeaves.start()

    def tabChanged(self, index):
        if index == 0:
            # start plotter
            self.threadPlotter = PollSensor(self.leaf)
            self.threadPlotter.sigDataY.connect(self.updatePlot)
            self.threadPlotter.sigLog.connect(self.updateStatusBar)
            self.threadPlotter.start()
        else:
            # kill old thread if any
            try:
                self.threadPlotter.terminate()
            except AttributeError:
                pass
            except Exception as e:
                log.error(e)
                self.updateStatusBar("Error while terminating thread")

    def leafSelected(self, index):
        log.info(f"Selected leaf: {index.row()}")

        # clean data:
        self.sensorData.clear()
        self.leaf: xp.Leaf = self.leaves[index.row()]
        pingReply: xp.XerxesPingReply = self.leaf.ping()
        self.ui.labelVersion.setText(
            f"{pingReply.v_maj}.{pingReply.v_min}"
        )
        devId = pingReply.dev_id
        self.ui.labelLeafInfo.setText(devIdTable[devId])

        self.ui.lineEditLeafAddress.setText(
            str(int(self.leaf.address))
        )
        self.ui.lineEditLeafAddress.editingFinished.connect(
            self.changeLeafAddress
        )
        
        # enable checkboxes
        self.ui.checkBoxFreeRun.clicked.connect(self.changeLeafConfig)
        self.ui.checkBoxCalcStat.clicked.connect(self.changeLeafConfig)
        for i in range(3):
            try:
                config = self.leaf.device_config
                break
            except TimeoutError:
                pass
        self.ui.checkBoxFreeRun.setChecked(config & 0x01)
        self.ui.checkBoxCalcStat.setChecked(config & 0x02)

        self.ui.labelUID.setText(str(self.leaf.device_uid))
        self.ui.labelErrors.setText(str(self.leaf.device_error))
        self.ui.labelStatus.setText(str(self.leaf.device_status))

    def changeLeafConfig(self):
        config = self.ui.checkBoxFreeRun.isChecked() | self.ui.checkBoxCalcStat.isChecked() << 1
        log.info(f"Changing leaf config to {config}")
        for i in range(3):
            try:
                self.leaf.device_config = config
                self.updateStatusBar("Config changed")
                break
            except TimeoutError:
                pass
            except Exception as e:
                log.error(e)
                self.updateStatusBar("Config change failed")

    def changeLeafAddress(self):
        try:
            newAddress = int(self.ui.lineEditLeafAddress.text())
            self.leaf.address = newAddress
        except TimeoutError:
            log.error("TimeoutError")
            self.updateStatusBar("Sensor does not respond, try again.")
        except ValueError:
            log.error(f"Invalid address: {self.ui.lineEditLeafAddress.text()}")
            self.updateStatusBar(f"Invalid address: {self.ui.lineEditLeafAddress.text()}")
        except Exception as e:
            log.error(e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Xerxes")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
