# This Python file uses the following encoding: utf-8
import sys
from typing import List

from PySide6.QtWidgets import QApplication, QMainWindow
import PySide6.QtCore as QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from utils import devIdTable
import logging
import argparse
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
                port = serial.Serial(portname, timeout=.01, baudrate=115200)
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

    def __init__(self, port, range=5):
        super().__init__()
        self.port = port
        self._r = range
    
    def run(self):
        log.info(f"Discovering leaves on port {self.port}")

        self._xn = xp.XerxesNetwork(self.port)
        self._xn.init()
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

    def updateStatusBar(self, msg):
        """Update the status bar with the given message."""
        self.statusBar().showMessage(msg)

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
        self.threadDiscoverLeaves.start()

    def leafSelected(self, index):
        log.info(f"Selected leaf: {index.row()}")
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

    def changeLeafAddress(self):
        newAddress = int(self.ui.lineEditLeafAddress.text())
        try:
            self.leaf.address = newAddress
        except TimeoutError:
            log.error("TimeoutError")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Xerxes")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
