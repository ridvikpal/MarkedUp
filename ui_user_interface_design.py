# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface_designcJnntN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1411, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.currentPriceGroup = QGroupBox(self.centralwidget)
        self.currentPriceGroup.setObjectName(u"currentPriceGroup")
        self.currentPriceGroup.setGeometry(QRect(1100, 270, 301, 221))
        self.currentPriceGroup.setCheckable(False)
        self.currentPriceTable = QTableWidget(self.currentPriceGroup)
        self.currentPriceTable.setObjectName(u"currentPriceTable")
        self.currentPriceTable.setGeometry(QRect(10, 20, 281, 191))
        font = QFont()
        font.setFamily(u"Arial")
        self.currentPriceTable.setFont(font)
        self.fiftyTwoWeekAverageGroup = QGroupBox(self.centralwidget)
        self.fiftyTwoWeekAverageGroup.setObjectName(u"fiftyTwoWeekAverageGroup")
        self.fiftyTwoWeekAverageGroup.setGeometry(QRect(1100, 500, 301, 251))
        self.fiftyTwoWeekAverageGroup.setCheckable(False)
        self.fiftyTwoWeekAverageTable = QTableWidget(self.fiftyTwoWeekAverageGroup)
        self.fiftyTwoWeekAverageTable.setObjectName(u"fiftyTwoWeekAverageTable")
        self.fiftyTwoWeekAverageTable.setGeometry(QRect(10, 20, 281, 221))
        self.fiftyTwoWeekAverageTable.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1100, 19, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1100, 60, 301, 52))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stockSymbol = QLabel(self.layoutWidget)
        self.stockSymbol.setObjectName(u"stockSymbol")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(32)
        self.stockSymbol.setFont(font2)

        self.horizontalLayout_2.addWidget(self.stockSymbol)

        self.stockName = QLabel(self.layoutWidget)
        self.stockName.setObjectName(u"stockName")
        font3 = QFont()
        font3.setPointSize(14)
        self.stockName.setFont(font3)
        self.stockName.setFrameShape(QFrame.NoFrame)
        self.stockName.setFrameShadow(QFrame.Plain)
        self.stockName.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.stockName)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1100, 120, 301, 141))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stockImage = QLabel(self.layoutWidget1)
        self.stockImage.setObjectName(u"stockImage")

        self.horizontalLayout.addWidget(self.stockImage)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stockExchange = QLabel(self.layoutWidget1)
        self.stockExchange.setObjectName(u"stockExchange")
        self.stockExchange.setFont(font3)
        self.stockExchange.setFrameShape(QFrame.NoFrame)
        self.stockExchange.setFrameShadow(QFrame.Plain)
        self.stockExchange.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stockExchange)

        self.stockMicCode = QLabel(self.layoutWidget1)
        self.stockMicCode.setObjectName(u"stockMicCode")
        self.stockMicCode.setFont(font3)
        self.stockMicCode.setFrameShape(QFrame.NoFrame)
        self.stockMicCode.setFrameShadow(QFrame.Plain)
        self.stockMicCode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stockMicCode)

        self.stockCurrency = QLabel(self.layoutWidget1)
        self.stockCurrency.setObjectName(u"stockCurrency")
        self.stockCurrency.setFont(font3)
        self.stockCurrency.setFrameShape(QFrame.NoFrame)
        self.stockCurrency.setFrameShadow(QFrame.Plain)
        self.stockCurrency.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stockCurrency)

        self.stockTimeStamp = QLabel(self.layoutWidget1)
        self.stockTimeStamp.setObjectName(u"stockTimeStamp")
        self.stockTimeStamp.setFont(font3)
        self.stockTimeStamp.setFrameShape(QFrame.NoFrame)
        self.stockTimeStamp.setFrameShadow(QFrame.Plain)
        self.stockTimeStamp.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stockTimeStamp)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.plotlyGroupBox = QGroupBox(self.centralwidget)
        self.plotlyGroupBox.setObjectName(u"plotlyGroupBox")
        self.plotlyGroupBox.setGeometry(QRect(10, 10, 1081, 741))

        # self.plotlyGraph = QWidget(self.plotlyGroupBox)
        # self.plotlyGraph.setObjectName(u"plotlyGraph")
        # self.plotlyGraph.setGeometry(QRect(10, 20, 1061, 711))

        # setup the plotly graph
        self.plotlyGraph = QWebEngineView(self.plotlyGroupBox)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "figure.html"))
        self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        self.plotlyGraph.setObjectName(u"plotlyGraph")
        self.plotlyGraph.setGeometry(QRect(10, 20, 1061, 711))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1411, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MarkedUp", None))
        self.currentPriceGroup.setTitle(QCoreApplication.translate("MainWindow", u"Current Prices", None))
        self.fiftyTwoWeekAverageGroup.setTitle(QCoreApplication.translate("MainWindow", u"52-Week Average", None))
        self.stockSymbol.setText("")
        self.stockName.setText("")
        self.stockImage.setText("")
        self.stockExchange.setText("")
        self.stockMicCode.setText("")
        self.stockCurrency.setText("")
        self.stockTimeStamp.setText("")
        self.plotlyGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"CandleStick Chart", None))
    # retranslateUi

def createMainWindow() -> None:
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())