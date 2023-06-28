# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface_designXxxAQK.ui'
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
from datetime import datetime
import plotly.offline
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1418, 830)
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
        self.plotlyGraph.setObjectName(u"plotlyGraph")
        self.plotlyGraph.setGeometry(QRect(10, 20, 1051, 781))

        self.stockSearchGroup = QGroupBox(self.centralwidget)
        self.stockSearchGroup.setObjectName(u"stockSearchGroup")
        self.stockSearchGroup.setGeometry(QRect(1090, 10, 321, 61))
        self.stockSearch = QLineEdit(self.stockSearchGroup)
        self.stockSearch.setObjectName(u"stockSearch")
        self.stockSearch.setGeometry(QRect(10, 20, 171, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.stockSearch.setFont(font)

        ### Add connection to stock search line edit
        self.stockSearch.editingFinished.connect(self.enterStock)

        self.countrySelectBox = QComboBox(self.stockSearchGroup)
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.addItem("")
        self.countrySelectBox.setObjectName(u"countrySelectBox")
        self.countrySelectBox.setGeometry(QRect(190, 20, 121, 31))
        self.stockDataGroup = QGroupBox(self.centralwidget)
        self.stockDataGroup.setObjectName(u"stockDataGroup")
        self.stockDataGroup.setGeometry(QRect(1090, 80, 321, 531))
        self.stockDataTable = QTableWidget(self.stockDataGroup)
        if (self.stockDataTable.columnCount() < 1):
            self.stockDataTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.stockDataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.stockDataTable.rowCount() < 15):
            self.stockDataTable.setRowCount(15)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(11, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(12, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(13, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.stockDataTable.setVerticalHeaderItem(14, __qtablewidgetitem15)
        self.stockDataTable.setObjectName(u"stockDataTable")
        self.stockDataTable.setGeometry(QRect(10, 150, 301, 371))
        font1 = QFont()
        font1.setFamily(u"Arial")
        self.stockDataTable.setFont(font1)
        self.stockDataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.stockDataTable.horizontalHeader().setDefaultSectionSize(200)
        self.stockDataTable.verticalHeader().setMinimumSectionSize(23)
        self.stockDataTable.verticalHeader().setDefaultSectionSize(23)
        self.layoutWidget = QWidget(self.stockDataGroup)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 301, 121))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stockImage = QLabel(self.layoutWidget)
        self.stockImage.setObjectName(u"stockImage")
        font2 = QFont()
        font2.setPointSize(14)
        self.stockImage.setFont(font2)
        self.stockImage.setFrameShape(QFrame.NoFrame)
        self.stockImage.setFrameShadow(QFrame.Plain)
        self.stockImage.setAlignment(Qt.AlignCenter)
        self.stockImage.setWordWrap(True)

        self.horizontalLayout.addWidget(self.stockImage)

        self.stockName = QLabel(self.layoutWidget)
        self.stockName.setObjectName(u"stockName")
        self.stockName.setFont(font2)
        self.stockName.setFrameShape(QFrame.NoFrame)
        self.stockName.setFrameShadow(QFrame.Plain)
        self.stockName.setAlignment(Qt.AlignCenter)
        self.stockName.setWordWrap(True)

        self.horizontalLayout.addWidget(self.stockName)

        self.favouritesGroup = QGroupBox(self.centralwidget)
        self.favouritesGroup.setObjectName(u"favouritesGroup")
        self.favouritesGroup.setGeometry(QRect(1090, 620, 321, 201))
        self.favouritesTable = QTableWidget(self.favouritesGroup)
        if (self.favouritesTable.columnCount() < 2):
            self.favouritesTable.setColumnCount(2)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.favouritesTable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.favouritesTable.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        self.favouritesTable.setObjectName(u"favouritesTable")
        self.favouritesTable.setGeometry(QRect(10, 20, 301, 141))
        self.favouritesTable.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget1 = QWidget(self.favouritesGroup)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 170, 301, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addFavouritesButton = QPushButton(self.layoutWidget1)
        self.addFavouritesButton.setObjectName(u"addFavouritesButton")
        self.addFavouritesButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.addFavouritesButton)

        self.removeFavouritesButton = QPushButton(self.layoutWidget1)
        self.removeFavouritesButton.setObjectName(u"removeFavouritesButton")
        self.removeFavouritesButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.removeFavouritesButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MarkedUp", None))
        self.plotlyGroup.setTitle(QCoreApplication.translate("MainWindow", u"CandleStick Chart", None))
        self.stockSearchGroup.setTitle(QCoreApplication.translate("MainWindow", u"Stock Search", None))
        self.countrySelectBox.setItemText(0, QCoreApplication.translate("MainWindow", u"United States", None))
        self.countrySelectBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Canada", None))
        self.countrySelectBox.setItemText(2, QCoreApplication.translate("MainWindow", u"United Kingdom", None))
        self.countrySelectBox.setItemText(3, QCoreApplication.translate("MainWindow", u"India", None))
        self.countrySelectBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Japan", None))
        self.countrySelectBox.setItemText(5, QCoreApplication.translate("MainWindow", u"China", None))
        self.countrySelectBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Germany", None))
        self.countrySelectBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Taiwan", None))
        self.countrySelectBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Brazil", None))
        self.countrySelectBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Australia", None))
        self.countrySelectBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Switzerland", None))
        self.countrySelectBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Finland", None))
        self.countrySelectBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Indonesia", None))
        self.countrySelectBox.setItemText(13, QCoreApplication.translate("MainWindow", u"Argentina", None))
        self.countrySelectBox.setItemText(14, QCoreApplication.translate("MainWindow", u"Austria", None))
        self.countrySelectBox.setItemText(15, QCoreApplication.translate("MainWindow", u"Netherlands", None))
        self.countrySelectBox.setItemText(16, QCoreApplication.translate("MainWindow", u"Mexico", None))
        self.countrySelectBox.setItemText(17, QCoreApplication.translate("MainWindow", u"Sweden", None))
        self.countrySelectBox.setItemText(18, QCoreApplication.translate("MainWindow", u"Israel", None))
        self.countrySelectBox.setItemText(19, QCoreApplication.translate("MainWindow", u"Spain", None))
        self.countrySelectBox.setItemText(20, QCoreApplication.translate("MainWindow", u"Turkey", None))
        self.countrySelectBox.setItemText(21, QCoreApplication.translate("MainWindow", u"Singapore", None))
        self.countrySelectBox.setItemText(22, QCoreApplication.translate("MainWindow", u"South Africa", None))

        self.stockDataGroup.setTitle(QCoreApplication.translate("MainWindow", u"Stock Data", None))
        ___qtablewidgetitem = self.stockDataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem1 = self.stockDataTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem2 = self.stockDataTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Exchange", None));
        ___qtablewidgetitem3 = self.stockDataTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MIC", None));
        ___qtablewidgetitem4 = self.stockDataTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Currency", None));
        ___qtablewidgetitem5 = self.stockDataTable.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TimeStamp", None));
        ___qtablewidgetitem6 = self.stockDataTable.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Current Price", None));
        ___qtablewidgetitem7 = self.stockDataTable.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Open", None));
        ___qtablewidgetitem8 = self.stockDataTable.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem9 = self.stockDataTable.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Low", None));
        ___qtablewidgetitem10 = self.stockDataTable.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Close", None));
        ___qtablewidgetitem11 = self.stockDataTable.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Volume", None));
        ___qtablewidgetitem12 = self.stockDataTable.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Previous Close", None));
        ___qtablewidgetitem13 = self.stockDataTable.verticalHeaderItem(12)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Change", None));
        ___qtablewidgetitem14 = self.stockDataTable.verticalHeaderItem(13)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Percent Change", None));
        ___qtablewidgetitem15 = self.stockDataTable.verticalHeaderItem(14)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Average Volume", None));
        self.stockImage.setText("")
        self.stockName.setText("")
        self.favouritesGroup.setTitle(QCoreApplication.translate("MainWindow", u"Favourites", None))
        ___qtablewidgetitem16 = self.favouritesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem17 = self.favouritesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.addFavouritesButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeFavouritesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

    ### function to use when entering stock
    def enterStock(self) -> None:
        # get data for specific stock
        stockSymbol = self.stockSearch.text()
        quote = connection.getStockQuote(stockSymbol)
        imageURL = connection.getStockLogo(stockSymbol)
        stockTimeSeriesGraph = connection.getStockTimeSeriesGraph(stockSymbol)
        livePrice = connection.getLivePrice(stockSymbol)

        # update the data table
        self.stockDataTable.setItem(0, 0, QTableWidgetItem(str(quote['symbol'][0])))
        self.stockDataTable.setItem(1, 0, QTableWidgetItem(str(quote['exchange'][0])))
        self.stockDataTable.setItem(2, 0, QTableWidgetItem(str(quote['mic_code'][0])))
        self.stockDataTable.setItem(3, 0, QTableWidgetItem(str(quote['currency'][0])))
        self.stockDataTable.setItem(4, 0, QTableWidgetItem(datetime.utcfromtimestamp(quote['timestamp'][0]).strftime('%Y-%m-%d %H:%M:%S')))
        self.stockDataTable.setItem(5, 0, QTableWidgetItem("{:.2f}".format(livePrice)))
        self.stockDataTable.setItem(6, 0, QTableWidgetItem(str(quote['open'][0])))
        self.stockDataTable.setItem(7, 0, QTableWidgetItem(str(quote['high'][0])))
        self.stockDataTable.setItem(8, 0, QTableWidgetItem(str(quote['low'][0])))
        self.stockDataTable.setItem(9, 0, QTableWidgetItem(str(quote['close'][0])))
        self.stockDataTable.setItem(10, 0, QTableWidgetItem(str(quote['volume'][0])))
        self.stockDataTable.setItem(11, 0, QTableWidgetItem(str(quote['previous_close'][0])))
        self.stockDataTable.setItem(12, 0, QTableWidgetItem(str(quote['change'][0])))
        self.stockDataTable.setItem(13, 0, QTableWidgetItem(str(quote['percent_change'][0]) + "%"))
        self.stockDataTable.setItem(14, 0, QTableWidgetItem(str(quote['average_volume'][0])))

        # update the stock name
        self.stockName.setText(str(quote['name'][0]))

        # update the stock logo
        image = QImage()
        image.loadFromData(requests.get(imageURL).content)
        self.stockImage.setPixmap(QPixmap(image))

        # update the stock plotly graph
        plotly.offline.plot(stockTimeSeriesGraph, filename='figure.html', auto_open=False)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "figure.html"))
        self.plotlyGraph.load(QUrl.fromLocalFile(file_path))

def createMainWindow() -> None:
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())