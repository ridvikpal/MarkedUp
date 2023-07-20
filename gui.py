### IMPORTS
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import sys
import connection
from datetime import datetime
import requests
from threading import Thread
import json
import qdarkstyle

### create a thread class that also returns a value on join()
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
        self.__exception = None
    def run(self):
        if self._target is not None:
            try:
                self._return = self._target(*self._args, **self._kwargs)
            except BaseException as e:
                self.__exception = e
    def join(self, *args):
        if self.__exception:
            raise self.__exception
        Thread.join(self, *args)
        return self._return

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1419, 839)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plotlyGroup = QGroupBox(self.centralwidget)
        self.plotlyGroup.setObjectName(u"plotlyGroup")
        self.plotlyGroup.setGeometry(QRect(10, 10, 1071, 821))

        ### create the window icon
        self.windowIcon = QIcon("MarkedUp_Icon.png")

        # self.plotlyGraph = QWidget(self.plotlyGroup)
        # self.plotlyGraph.setObjectName(u"plotlyGraph")
        # self.plotlyGraph.setGeometry(QRect(10, 70, 1051, 741))

        ### Setup plotly graph
        self.plotlyGraph = QWebEngineView(self.plotlyGroup)
        self.plotlyGraph.setObjectName(u"plotlyGraph")
        self.plotlyGraph.setGeometry(QRect(10, 70, 1051, 741))
        self.plotlyGraph.page().setBackgroundColor(QColor(0, 0, 0, 1))

        self.layoutWidget = QWidget(self.plotlyGroup)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 1051, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.oneMonthFilter = QPushButton(self.layoutWidget)
        self.oneMonthFilter.setObjectName(u"oneMonthFilter")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.oneMonthFilter.setFont(font)

        self.horizontalLayout_3.addWidget(self.oneMonthFilter)
        ### connect oneMonthFilter to show the right graph
        self.oneMonthFilter.clicked.connect(self.showOneMonthGraph)

        self.threeMonthFilter = QPushButton(self.layoutWidget)
        self.threeMonthFilter.setObjectName(u"threeMonthFilter")
        self.threeMonthFilter.setFont(font)

        self.horizontalLayout_3.addWidget(self.threeMonthFilter)
        ### connect threeMonthFilter to show the right graph
        self.threeMonthFilter.clicked.connect(self.showThreeMonthGraph)

        self.sixMonthFilter = QPushButton(self.layoutWidget)
        self.sixMonthFilter.setObjectName(u"sixMonthFilter")
        self.sixMonthFilter.setFont(font)

        self.horizontalLayout_3.addWidget(self.sixMonthFilter)
        ### connect sixMonthFilter to show the right graph
        self.sixMonthFilter.clicked.connect(self.showSixMonthGraph)

        self.oneYearFilter = QPushButton(self.layoutWidget)
        self.oneYearFilter.setObjectName(u"oneYearFilter")
        self.oneYearFilter.setFont(font)

        self.horizontalLayout_3.addWidget(self.oneYearFilter)
        ### connect oneYearFilter to show the right graph
        self.oneYearFilter.clicked.connect(self.showOneYearGraph)

        self.fiveYearFilter = QPushButton(self.layoutWidget)
        self.fiveYearFilter.setObjectName(u"fiveYearFilter")
        self.fiveYearFilter.setFont(font)

        self.horizontalLayout_3.addWidget(self.fiveYearFilter)
        ### connect fiveYearFilter to show the right graph
        self.fiveYearFilter.clicked.connect(self.showFiveYearGraph)

        self.switchColourButton = QPushButton(self.layoutWidget)
        self.switchColourButton.setObjectName(u"switchColourButton")
        self.switchColourButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.switchColourButton)
        ### connect dark mode button to switch colour function
        self.switchColourButton.clicked.connect(self.switchColourTheme)

        self.stockSearchGroup = QGroupBox(self.centralwidget)
        self.stockSearchGroup.setObjectName(u"stockSearchGroup")
        self.stockSearchGroup.setGeometry(QRect(1090, 10, 321, 61))
        self.stockSearch = QLineEdit(self.stockSearchGroup)
        self.stockSearch.setObjectName(u"stockSearch")
        self.stockSearch.setGeometry(QRect(10, 20, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.stockSearch.setFont(font1)

        ### Run function on enter for stock search line edit
        self.stockSearch.returnPressed.connect(self.enterStock)

        self.stockDataGroup = QGroupBox(self.centralwidget)
        self.stockDataGroup.setObjectName(u"stockDataGroup")
        self.stockDataGroup.setGeometry(QRect(1090, 80, 321, 541))
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
        self.stockDataTable.setGeometry(QRect(10, 150, 301, 381))
        font2 = QFont()
        font2.setFamily(u"Arial")
        self.stockDataTable.setFont(font2)
        self.stockDataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.stockDataTable.horizontalHeader().setDefaultSectionSize(200)
        self.stockDataTable.verticalHeader().setMinimumSectionSize(23)
        self.stockDataTable.verticalHeader().setDefaultSectionSize(23)
        self.layoutWidget1 = QWidget(self.stockDataGroup)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 301, 121))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stockImage = QLabel(self.layoutWidget1)
        self.stockImage.setObjectName(u"stockImage")
        font3 = QFont()
        font3.setPointSize(14)
        self.stockImage.setFont(font3)
        self.stockImage.setFrameShape(QFrame.NoFrame)
        self.stockImage.setFrameShadow(QFrame.Plain)
        self.stockImage.setAlignment(Qt.AlignCenter)
        self.stockImage.setWordWrap(True)

        self.horizontalLayout.addWidget(self.stockImage)

        self.stockName = QLabel(self.layoutWidget1)
        self.stockName.setObjectName(u"stockName")
        self.stockName.setFont(font3)
        self.stockName.setFrameShape(QFrame.NoFrame)
        self.stockName.setFrameShadow(QFrame.Plain)
        self.stockName.setAlignment(Qt.AlignCenter)
        self.stockName.setWordWrap(True)

        self.horizontalLayout.addWidget(self.stockName)

        ### variable that holds the current theme style
        self.DarkTheme = True

        self.favouritesGroup = QGroupBox(self.centralwidget)
        self.favouritesGroup.setObjectName(u"favouritesGroup")
        self.favouritesGroup.setGeometry(QRect(1090, 630, 321, 201))
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

        ### get the clicked favourite
        self.favouritesTable.cellClicked.connect(self.getClickedCell)

        self.layoutWidget2 = QWidget(self.favouritesGroup)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 170, 301, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addFavouritesButton = QPushButton(self.layoutWidget2)
        self.addFavouritesButton.setObjectName(u"addFavouritesButton")
        self.addFavouritesButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.addFavouritesButton)
        ### connect addFavourite function to addFavouritesButton
        self.addFavouritesButton.clicked.connect(self.addFavourite)

        self.loadFavouriteButton = QPushButton(self.layoutWidget2)
        self.loadFavouriteButton.setObjectName(u"loadFavouriteButton")
        self.loadFavouriteButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.loadFavouriteButton)
        ### connect the load favourites function to the loadFavouriteButton
        self.loadFavouriteButton.clicked.connect(self.loadFavourite)

        self.removeFavouritesButton = QPushButton(self.layoutWidget2)
        self.removeFavouritesButton.setObjectName(u"removeFavouritesButton")
        self.removeFavouritesButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.removeFavouritesButton)
        ### connect removeFavourite function to removeFavouritesButton
        self.removeFavouritesButton.clicked.connect(self.removeFavourite)

        ### initialize the favourites table
        self.initalizaFavourites()

        ### Add autocomplete to the stockSearch
        self.setupAutcomplete()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MarkedUp", None))
        MainWindow.setWindowIcon(self.windowIcon)
        self.plotlyGroup.setTitle(QCoreApplication.translate("MainWindow", u"CandleStick Chart", None))
        self.oneMonthFilter.setText(QCoreApplication.translate("MainWindow", u"1 Month", None))
        self.threeMonthFilter.setText(QCoreApplication.translate("MainWindow", u"3 Months", None))
        self.sixMonthFilter.setText(QCoreApplication.translate("MainWindow", u"6 Months", None))
        self.oneYearFilter.setText(QCoreApplication.translate("MainWindow", u"1 Year", None))
        self.fiveYearFilter.setText(QCoreApplication.translate("MainWindow", u"5 Years", None))
        self.switchColourButton.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.stockSearchGroup.setTitle(QCoreApplication.translate("MainWindow", u"Stock Search", None))
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
        self.loadFavouriteButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.removeFavouritesButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

    ### function to use when entering stock
    def enterStock(self) -> None:
        try:
            # get data for specific stock
            autoCompleteString = self.stockSearch.text()
            extractData = autoCompleteString.split(" - ")
            stockSymbol = extractData[-1]

            quoteThread = ThreadWithReturnValue(target=connection.getStockQuote, args=(stockSymbol,))
            priceThread = ThreadWithReturnValue(target=connection.getLivePrice, args=(stockSymbol,))
            logoThread = ThreadWithReturnValue(target=connection.getStockLogo, args=(stockSymbol,))
            timeSeriesThread = ThreadWithReturnValue(target=connection.getStockTimeSeries, args=(stockSymbol,))

            quoteThread.start()
            priceThread.start()
            logoThread.start()
            timeSeriesThread.start()

            quote = quoteThread.join()
            livePrice = priceThread.join()
            imageURL = logoThread.join()
            timeSeries = timeSeriesThread.join()

            # once the time series data is availible, now create all five graphs and store them locally
            oneMonthGraphThread = Thread(target=connection.exportFilteredTimeSeriesGraph, args=(timeSeries, "1 month"))
            threeMonthGraphThread = Thread(target=connection.exportFilteredTimeSeriesGraph, args=(timeSeries, "3 months"))
            sixMonthGraphThread = Thread(target=connection.exportFilteredTimeSeriesGraph, args=(timeSeries, "6 months"))
            oneYearGraphThread = Thread(target=connection.exportFilteredTimeSeriesGraph, args=(timeSeries, "1 year"))
            fiveYearGraphThread = Thread(target=connection.exportFilteredTimeSeriesGraph, args=(timeSeries,))

            # run all threads
            oneMonthGraphThread.start()
            threeMonthGraphThread.start()
            sixMonthGraphThread.start()
            oneYearGraphThread.start()
            fiveYearGraphThread.start()

            # join all threads
            oneMonthGraphThread.join()
            threeMonthGraphThread.join()
            sixMonthGraphThread.join()
            oneYearGraphThread.join()
            fiveYearGraphThread.join()

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
            # self.plotlyGraph.page().setBackgroundColor(QColor(0, 0, 0, 1))
            self.showThreeMonthGraph()

        except Exception as e:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("There was an error with the TwelveData API: ")
            errorMessage.setInformativeText(str(e))
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to show the one month graph
    def showOneMonthGraph(self) -> None:
        if self.DarkTheme:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "1 month_dark.html"))
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "1 month.html"))

        if os.path.isfile(file_path):
            # update the stock plotly graph
            self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        else:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a stock first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to show the three month graph
    def showThreeMonthGraph(self) -> None:
        if self.DarkTheme:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "3 months_dark.html"))
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "3 months.html"))

        if os.path.isfile(file_path):
            # update the stock plotly graph
            self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        else:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a stock first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to show the six month graph
    def showSixMonthGraph(self) -> None:
        if self.DarkTheme:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "6 months_dark.html"))
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "6 months.html"))
        if os.path.isfile(file_path):
            # update the stock plotly graph
            self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        else:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a stock first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to show the one year graph
    def showOneYearGraph(self) -> None:
        if self.DarkTheme:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "1 year_dark.html"))
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "1 year.html"))
        if os.path.isfile(file_path):
            # update the stock plotly graph
            self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        else:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a stock first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to show the five year graph
    def showFiveYearGraph(self) -> None:
        if self.DarkTheme:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "5 years_dark.html"))
        else:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "5 years.html"))
        if os.path.isfile(file_path):
            # update the stock plotly graph
            self.plotlyGraph.load(QUrl.fromLocalFile(file_path))
        else:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a stock first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to add favourites
    def addFavourite(self):
        name = self.stockName.text()
        symbol = self.stockDataTable.item(0, 0).text()
        if name and symbol:
            currentRowCount = self.favouritesTable.rowCount()
            self.favouritesTable.insertRow(currentRowCount)

            self.favouritesTable.setItem(currentRowCount, 0, QTableWidgetItem(symbol))
            self.favouritesTable.setItem(currentRowCount, 1, QTableWidgetItem(name))

            savedFavourites.update({symbol:name})

            with open('saved_favourites.json', 'w') as f:
                json.dump(savedFavourites, f)
        else:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a stock first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to get the clicked favourites cell
    def getClickedCell(self, row, column) -> None:
        global selectedFavourite
        selectedFavourite = self.favouritesTable.item(row, column)

    ### function to remove favourites
    def removeFavourite(self) -> None:
        try:
            if self.favouritesTable.rowCount() > 0:
                rowToDelete = selectedFavourite.row()
                symbol = self.favouritesTable.item(rowToDelete, 0).text()

                self.favouritesTable.removeRow(rowToDelete)
                del savedFavourites[symbol]

                with open('saved_favourites.json', 'w') as f:
                    json.dump(savedFavourites, f)
        except Exception as e:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a favourite first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to load the selected favourite
    def loadFavourite(self) -> None:
        try:
            if self.favouritesTable.rowCount() > 0:
                rowToLoad = selectedFavourite.row()
                symbol = self.favouritesTable.item(rowToLoad, 0).text()
                name = self.favouritesTable.item(rowToLoad, 1).text()
                self.stockSearch.setText(name + " - " + symbol)
                self.enterStock()
        except Exception as e:
            errorMessage = QMessageBox()
            errorMessage.setWindowIcon(self.windowIcon)
            errorMessage.setWindowTitle("An error has occured")
            errorMessage.setIcon(QMessageBox.Information)
            errorMessage.setText("Please select a favourite first")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

    ### function to load favourites stored in json file
    def initalizaFavourites(self) -> None:
        global savedFavourites
        if os.path.isfile('saved_favourites.json'):
            savedFavourites = json.load(open('saved_favourites.json'))
            for symbol in savedFavourites:
                currentRowCount = self.favouritesTable.rowCount()
                self.favouritesTable.insertRow(currentRowCount)

                self.favouritesTable.setItem(currentRowCount, 0, QTableWidgetItem(symbol))
                self.favouritesTable.setItem(currentRowCount, 1, QTableWidgetItem(savedFavourites[symbol]))
        else:
            open('saved_favourites.json', 'w').close()
            savedFavourites = dict()

    ### function to switch between dark/light themes
    def switchColourTheme(self):
        app = QCoreApplication.instance()
        if self.DarkTheme:
            app.setStyleSheet(lightTheme)
            self.switchColourButton.setText("Dark Mode")
        else:
            app.setStyleSheet(darkTheme)
            self.switchColourButton.setText("Light Mode")
        self.DarkTheme = not self.DarkTheme

        current_graph = self.plotlyGraph.page().title()
        if "1 month" in current_graph:
            self.showOneMonthGraph()
        elif "3 months" in current_graph:
            self.showThreeMonthGraph()
        elif "6 months" in current_graph:
            self.showSixMonthGraph()
        elif "1 year" in current_graph:
            self.showOneYearGraph()
        elif "5 year" in current_graph:
            self.showFiveYearGraph()
        else:
            pass

    def setupAutcomplete(self) -> None:
        self.stocksList = connection.getStocksList()
        self.stockCompleter = QCompleter(self.stocksList)
        self.stockCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.stockCompleter.setModelSorting(QCompleter.CaseSensitivelySortedModel)
        self.stockSearch.setCompleter(self.stockCompleter)
        self.stockCompleter.setMaxVisibleItems(40)

### function to create main window
def createMainWindow() -> None:
    app = QApplication(sys.argv)
    window = QMainWindow()

    # setup stylesheet
    global lightTheme
    global darkTheme
    lightTheme = qdarkstyle.load_stylesheet(palette=qdarkstyle.LightPalette)
    darkTheme = qdarkstyle.load_stylesheet(palette=qdarkstyle.DarkPalette)
    app.setStyleSheet(darkTheme)

    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    run = app.exec_()

    sys.exit(run)

### function used to test things
def testFunction():
    # df = connection.update_stocks_list()
    matches = connection.getStocksList('United States')
    # for x in matches: print(x)
    print(matches)