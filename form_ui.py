# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1032, 716)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"/*\n"
"ManjaroMix Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 25/02/2020, 15:42.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/ManjaroMix.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#151a1e;\n"
"}\n"
"QCalendar {\n"
"	background-color: #151a1e;\n"
"}\n"
"QListWidget {\n"
"	background-color: #151a1e;\n"
"	color: #d3dae3;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"	background-color: #222b2e;\n"
"	color: #d3dae3;\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"	background-color: #222b2e;\n"
"	color: #d3dae3;\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 2"
                        "27, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-wid"
                        "th: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	back"
                        "ground-color: #151a1e;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #FFFFFF;\n"
"	padding: 2px;\n"
"	background-color: #151a1e;;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: #1c1f1f;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: #2c2f2f;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0"
                        ", y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"	background-color: #222b2e;\n"
"	color: #d3dae3;\n"
"}\n"
"QLabel {\n"
"	color: #d3dae3;\n"
"}\n"
"QLCDNumber {\n"
"	color: #4d9b87;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: #d3dae3;\n"
"	border-radius: 10px;\n"
"	border-color: transparent;\n"
"	border-style: solid;\n"
"	background-color: #52595d;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #214037	;\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: #151a1e;\n"
"}\n"
"QMenuBar::item {\n"
"	color: #d3dae3;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-c"
                        "olor: #151a1e;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: #252a2e;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu {\n"
"	background-color: #151a1e;\n"
"}\n"
"QMenu::item:selected {\n"
"	background-color: #252a2e;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item {\n"
"	color: #d3dae3;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: #050a0e;\n"
"		background-color: #1e282c;\n"
"		border-style: solid;\n"
"		border-width: 1px;\n"
"    	border-bottom-left-radius: 4px;\n"
"		border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	border-top-left-radius: 4px;\n"
"	color: #d3dae3;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #151a1e;\n"
""
                        "}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-left-width:1px;\n"
"	border-right-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-color: #050a0e;\n"
"	border-top-right-radius: 4px;\n"
"	color: #d3dae3;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-left-width:1px;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	color: #d3dae3;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
""
                        "	background-color: #1e282c;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:0px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #1e282c;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #000000;\n"
""
                        "	background-color: qradialgradient(cx:0.4, cy:0.4, radius: 1.5,fx:0, fy:0, stop:0 #1e282c, stop:0.3 #1e282c, stop:0.4 #4fa08b, stop:0.5 #1e282c, stop:1 #1e282c);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: #d3dae3;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #a9b7c6;\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #4fa08b, stop:1 #1e282c);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpi"
                        "nBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QTimeEdit {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QDateEdit {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QFontComboBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QComboBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	borde"
                        "r-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"\n"
"QDial {\n"
"	background: #16a085;\n"
"}\n"
"\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color: #222b2e;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#222b2e;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#222b2e;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#222b2e;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: #52595d;\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: #52595d;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: #1a2224;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: #1a2224;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
""
                        "QSlider::add-page:horizontal {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #15433a;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #15433a;\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 10px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"	background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 10px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"	background: transparent;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: #52595d;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: #58a492;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: #52595d;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-height: 25"
                        "px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: #58a492;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add"
                        "-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: "
                        "20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon = QIcon()
        iconThemeName = u"sync-synchronizing"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionRefresh.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.buttonRescanPort = QPushButton(self.frame_6)
        self.buttonRescanPort.setObjectName(u"buttonRescanPort")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonRescanPort.sizePolicy().hasHeightForWidth())
        self.buttonRescanPort.setSizePolicy(sizePolicy1)
        self.buttonRescanPort.setFont(font)
        self.buttonRescanPort.setFlat(False)

        self.horizontalLayout_4.addWidget(self.buttonRescanPort)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.comboBoxComPorts = QComboBox(self.frame_3)
        self.comboBoxComPorts.setObjectName(u"comboBoxComPorts")
        self.comboBoxComPorts.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.comboBoxComPorts.setFont(font1)

        self.verticalLayout_2.addWidget(self.comboBoxComPorts)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.buttonRescanLeaves = QPushButton(self.frame_7)
        self.buttonRescanLeaves.setObjectName(u"buttonRescanLeaves")
        self.buttonRescanLeaves.setEnabled(False)
        self.buttonRescanLeaves.setFont(font)

        self.horizontalLayout_5.addWidget(self.buttonRescanLeaves)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.listWidgetLeaves = QListWidget(self.frame_5)
        self.listWidgetLeaves.setObjectName(u"listWidgetLeaves")
        self.listWidgetLeaves.setFont(font1)

        self.verticalLayout_3.addWidget(self.listWidgetLeaves)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_7.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.labelLeafInfo = QLabel(self.frame_9)
        self.labelLeafInfo.setObjectName(u"labelLeafInfo")
        self.labelLeafInfo.setFont(font)
        self.labelLeafInfo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelLeafInfo)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget = QTabWidget(self.frame_10)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.tabWidget.setFont(font2)
        self.tabValues = QWidget()
        self.tabValues.setObjectName(u"tabValues")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.tabValues.setFont(font3)
        self.tabWidget.addTab(self.tabValues, "")
        self.tabSettings = QWidget()
        self.tabSettings.setObjectName(u"tabSettings")
        self.tabSettings.setFont(font3)
        self.formLayout = QFormLayout(self.tabSettings)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.tabSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEditLeafAddress = QLineEdit(self.tabSettings)
        self.lineEditLeafAddress.setObjectName(u"lineEditLeafAddress")
        self.lineEditLeafAddress.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditLeafAddress)

        self.label_5 = QLabel(self.tabSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.frame_8 = QFrame(self.tabSettings)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBoxFreeRun = QCheckBox(self.frame_8)
        self.checkBoxFreeRun.setObjectName(u"checkBoxFreeRun")
        self.checkBoxFreeRun.setFont(font1)

        self.horizontalLayout_3.addWidget(self.checkBoxFreeRun)

        self.checkBoxCalcStat = QCheckBox(self.frame_8)
        self.checkBoxCalcStat.setObjectName(u"checkBoxCalcStat")
        self.checkBoxCalcStat.setFont(font1)

        self.horizontalLayout_3.addWidget(self.checkBoxCalcStat)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_8)

        self.label = QLabel(self.tabSettings)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.labelVersion = QLabel(self.tabSettings)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelVersion)

        self.tabWidget.addTab(self.tabSettings, "")

        self.verticalLayout_11.addWidget(self.tabWidget)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XerxesInspector", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Connection</span></p></body></html>", None))
        self.buttonRescanPort.setText(QCoreApplication.translate("MainWindow", u"Rescan", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Sensors</span></p></body></html>", None))
        self.buttonRescanLeaves.setText(QCoreApplication.translate("MainWindow", u"Rescan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Sensor</span></p></body></html>", None))
        self.labelLeafInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">-</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabValues), QCoreApplication.translate("MainWindow", u"Values", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.checkBoxFreeRun.setText(QCoreApplication.translate("MainWindow", u"Free run", None))
        self.checkBoxCalcStat.setText(QCoreApplication.translate("MainWindow", u"Calculate statistics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.labelVersion.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

