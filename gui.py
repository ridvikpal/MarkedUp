# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface_designpecthV.ui'
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
import connection
import pandas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1426, 830)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plotlyGroup = QGroupBox(self.centralwidget)
        self.plotlyGroup.setObjectName(u"plotlyGroup")
        self.plotlyGroup.setGeometry(QRect(10, 10, 1071, 811))

        # self.plotlyGraph = QWidget(self.plotlyGroup)
        # self.plotlyGraph.setObjectName(u"plotlyGraph")
        # self.plotlyGraph.setGeometry(QRect(10, 20, 1051, 781))
        ### Setup plotly graph
        self.plotlyGraph = QWebEngineView(self.plotlyGroup)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "figure.html"))
        self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        self.plotlyGraph.setObjectName(u"plotlyGraph")
        self.plotlyGraph.setGeometry(QRect(10, 20, 1051, 781))

        self.stockSearchGroup = QGroupBox(self.centralwidget)
        self.stockSearchGroup.setObjectName(u"stockSearchGroup")
        self.stockSearchGroup.setGeometry(QRect(1090, 10, 321, 61))
        self.stockSearch = QLineEdit(self.stockSearchGroup)
        self.stockSearch.setObjectName(u"stockSearch")
        self.stockSearch.setGeometry(QRect(10, 20, 301, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.stockSearch.setFont(font)

        ### Add connection to stock search line edit
        self.stockSearch.editingFinished.connect(self.enterStock)

        self.stockDataGroup = QGroupBox(self.centralwidget)
        self.stockDataGroup.setObjectName(u"stockDataGroup")
        self.stockDataGroup.setGeometry(QRect(1090, 80, 321, 511))
        self.currentPriceTable = QTableWidget(self.stockDataGroup)
        if (self.currentPriceTable.columnCount() < 1):
            self.currentPriceTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.currentPriceTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.currentPriceTable.rowCount() < 14):
            self.currentPriceTable.setRowCount(14)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(11, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(12, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.currentPriceTable.setVerticalHeaderItem(13, __qtablewidgetitem14)
        self.currentPriceTable.setObjectName(u"currentPriceTable")
        self.currentPriceTable.setGeometry(QRect(10, 150, 301, 351))
        font1 = QFont()
        font1.setFamily(u"Arial")
        self.currentPriceTable.setFont(font1)
        self.currentPriceTable.horizontalHeader().setCascadingSectionResizes(False)
        self.currentPriceTable.horizontalHeader().setDefaultSectionSize(200)
        self.currentPriceTable.verticalHeader().setMinimumSectionSize(23)
        self.currentPriceTable.verticalHeader().setDefaultSectionSize(23)
        self.widget = QWidget(self.stockDataGroup)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 301, 121))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stockImage = QLabel(self.widget)
        self.stockImage.setObjectName(u"stockImage")
        font2 = QFont()
        font2.setPointSize(14)
        self.stockImage.setFont(font2)
        self.stockImage.setFrameShape(QFrame.NoFrame)
        self.stockImage.setFrameShadow(QFrame.Plain)
        self.stockImage.setAlignment(Qt.AlignCenter)
        self.stockImage.setWordWrap(True)

        self.horizontalLayout.addWidget(self.stockImage)

        self.stockName = QLabel(self.widget)
        self.stockName.setObjectName(u"stockName")
        self.stockName.setFont(font2)
        self.stockName.setFrameShape(QFrame.NoFrame)
        self.stockName.setFrameShadow(QFrame.Plain)
        self.stockName.setAlignment(Qt.AlignCenter)
        self.stockName.setWordWrap(True)

        self.horizontalLayout.addWidget(self.stockName)

        self.favouritesGroup = QGroupBox(self.centralwidget)
        self.favouritesGroup.setObjectName(u"favouritesGroup")
        self.favouritesGroup.setGeometry(QRect(1090, 610, 321, 211))
        self.favouritesTable = QTableWidget(self.favouritesGroup)
        if (self.favouritesTable.columnCount() < 2):
            self.favouritesTable.setColumnCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.favouritesTable.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.favouritesTable.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        self.favouritesTable.setObjectName(u"favouritesTable")
        self.favouritesTable.setGeometry(QRect(10, 20, 301, 181))
        self.favouritesTable.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MarkedUp", None))
        self.plotlyGroup.setTitle(QCoreApplication.translate("MainWindow", u"CandleStick Chart", None))
        self.stockSearchGroup.setTitle(QCoreApplication.translate("MainWindow", u"Stock Search", None))
        self.stockDataGroup.setTitle(QCoreApplication.translate("MainWindow", u"Stock Data", None))
        ___qtablewidgetitem = self.currentPriceTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem1 = self.currentPriceTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem2 = self.currentPriceTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Exchange", None));
        ___qtablewidgetitem3 = self.currentPriceTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MIC", None));
        ___qtablewidgetitem4 = self.currentPriceTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem5 = self.currentPriceTable.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TimeStamp", None));
        ___qtablewidgetitem6 = self.currentPriceTable.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Open", None));
        ___qtablewidgetitem7 = self.currentPriceTable.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem8 = self.currentPriceTable.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Low", None));
        ___qtablewidgetitem9 = self.currentPriceTable.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Close", None));
        ___qtablewidgetitem10 = self.currentPriceTable.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Volume", None));
        ___qtablewidgetitem11 = self.currentPriceTable.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Previous Close", None));
        ___qtablewidgetitem12 = self.currentPriceTable.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Change", None));
        ___qtablewidgetitem13 = self.currentPriceTable.verticalHeaderItem(12)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Percent Change", None));
        ___qtablewidgetitem14 = self.currentPriceTable.verticalHeaderItem(13)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Average Volume", None));
        self.stockImage.setText("")
        self.stockName.setText("")
        self.favouritesGroup.setTitle(QCoreApplication.translate("MainWindow", u"Favourites", None))
        ___qtablewidgetitem15 = self.favouritesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem16 = self.favouritesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
    # retranslateUi

    ### function to use when entering stock
    def enterStock(self) -> None:
        # get quote for specific stock
        stockSymbol = self.stockSearch.text()
        quote = connection.getStockQuote(stockSymbol)

        # # update stock symbol
        # self.stockSymbol.setText(stockSymbol)
        # self.stockSymbol.adjustSize()
        # # update the stock name
        # self.stockName.setText(str(quote['name'][0]))
        # # update the stock
        # self.stockExchange.setText(str(quote['exchange'][0]))
        # # update the stock mic code
        # self.stockMicCode.setText(str(quote['mic_code'][0]))
        # # update the currency
        # self.stockCurrency.setText(str(quote['currency'][0]))
        # # update the timestamp
        # self.stockTimeStamp.setText(str(quote['timestamp'][0]))

        # update the table
        # self.currentPriceTable.

def createMainWindow() -> None:
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())