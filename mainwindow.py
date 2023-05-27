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
from Discover import Discover
from utils import devIdTable
import logging
import argparse
import serial
import threading
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
                port = serial.Serial(portname, timeout=.01, baudrate=115200)
                port.close()
                self.sigAvailablePorts.emit(portname)
                self.sigLog.emit(f"Found port: {portname}")
                log.info(f"Found port: {portname}")

            except serial.SerialException:
                pass
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
        self._get_leaves()
        log.info(f"Found {len(self.leaves)} leaves")
        self.ui.buttonRescanLeaves.setEnabled(True)
        self.ui.listWidgetLeaves.clear()
        self.ui.listWidgetLeaves.addItems([str(leaf) for leaf in self.leaves])

    def leafSelected(self, index):
        log.info(f"Selected leaf: {index.row()}")
        self.leaf: xp.Leaf = self.leaves[index.row()]
        pingReply: xp.XerxesPingReply = self.leaf.ping()
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
