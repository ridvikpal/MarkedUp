# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface_designheHNiq.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1081, 641))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plotlyGraph = QWidget(self.layoutWidget)
        self.plotlyGraph.setObjectName(u"plotlyGraph")

        self.horizontalLayout.addWidget(self.plotlyGraph)

        self.tabs = QTabWidget(self.layoutWidget)
        self.tabs.setObjectName(u"tabs")
        self.stockTab = QWidget()
        self.stockTab.setObjectName(u"stockTab")
        self.stockInput = QLineEdit(self.stockTab)
        self.stockInput.setObjectName(u"stockInput")
        self.stockInput.setGeometry(QRect(10, 10, 331, 20))
        self.stockSymbol = QLabel(self.stockTab)
        self.stockSymbol.setObjectName(u"stockSymbol")
        self.stockSymbol.setGeometry(QRect(10, 40, 331, 31))
        font = QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.stockSymbol.setFont(font)
        self.stockSymbol.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayoutWidget = QWidget(self.stockTab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 80, 331, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.stockNameLabel = QLabel(self.formLayoutWidget)
        self.stockNameLabel.setObjectName(u"stockNameLabel")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.stockNameLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.stockNameLabel)

        self.stockExchangeLabel = QLabel(self.formLayoutWidget)
        self.stockExchangeLabel.setObjectName(u"stockExchangeLabel")
        self.stockExchangeLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.stockExchangeLabel)

        self.stockMicCodeLabel = QLabel(self.formLayoutWidget)
        self.stockMicCodeLabel.setObjectName(u"stockMicCodeLabel")
        self.stockMicCodeLabel.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.stockMicCodeLabel)

        self.stockCurrencyLabel = QLabel(self.formLayoutWidget)
        self.stockCurrencyLabel.setObjectName(u"stockCurrencyLabel")
        self.stockCurrencyLabel.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.stockCurrencyLabel)

        self.stockTimeStampLabel = QLabel(self.formLayoutWidget)
        self.stockTimeStampLabel.setObjectName(u"stockTimeStampLabel")
        self.stockTimeStampLabel.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.stockTimeStampLabel)

        self.stockName = QLabel(self.formLayoutWidget)
        self.stockName.setObjectName(u"stockName")
        font2 = QFont()
        font2.setPointSize(14)
        self.stockName.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.stockName)

        self.stockExchange = QLabel(self.formLayoutWidget)
        self.stockExchange.setObjectName(u"stockExchange")
        self.stockExchange.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.stockExchange)

        self.stockMicCode = QLabel(self.formLayoutWidget)
        self.stockMicCode.setObjectName(u"stockMicCode")
        self.stockMicCode.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.stockMicCode)

        self.stockCurrency = QLabel(self.formLayoutWidget)
        self.stockCurrency.setObjectName(u"stockCurrency")
        self.stockCurrency.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.stockCurrency)

        self.stockTimeStamp = QLabel(self.formLayoutWidget)
        self.stockTimeStamp.setObjectName(u"stockTimeStamp")
        self.stockTimeStamp.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.stockTimeStamp)

        self.currentPriceTable = QTableView(self.stockTab)
        self.currentPriceTable.setObjectName(u"currentPriceTable")
        self.currentPriceTable.setGeometry(QRect(10, 240, 331, 81))
        self.fiftyTwoWeekAverageLabel = QLabel(self.stockTab)
        self.fiftyTwoWeekAverageLabel.setObjectName(u"fiftyTwoWeekAverageLabel")
        self.fiftyTwoWeekAverageLabel.setGeometry(QRect(10, 330, 331, 21))
        font3 = QFont()
        font3.setPointSize(12)
        self.fiftyTwoWeekAverageLabel.setFont(font3)
        self.fiftyTwoWeekAverageTable = QTableView(self.stockTab)
        self.fiftyTwoWeekAverageTable.setObjectName(u"fiftyTwoWeekAverageTable")
        self.fiftyTwoWeekAverageTable.setGeometry(QRect(10, 360, 331, 241))
        self.tabs.addTab(self.stockTab, "")
        self.etfTab = QWidget()
        self.etfTab.setObjectName(u"etfTab")
        self.tabs.addTab(self.etfTab, "")

        self.horizontalLayout.addWidget(self.tabs)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1084, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # extension for plotly web widget
        self.web = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "figure.html"))
        self.web.load(QUrl.fromLocalFile(file_path))
        self.web.show()
        ##

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)




        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.stockSymbol.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stockNameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.stockExchangeLabel.setText(QCoreApplication.translate("MainWindow", u"Exchange", None))
        self.stockMicCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Mic Code", None))
        self.stockCurrencyLabel.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
        self.stockTimeStampLabel.setText(QCoreApplication.translate("MainWindow", u"Time Stamp", None))
        self.stockName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stockExchange.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stockMicCode.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stockCurrency.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stockTimeStamp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.fiftyTwoWeekAverageLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabs.setTabText(self.tabs.indexOf(self.stockTab), QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.tabs.setTabText(self.tabs.indexOf(self.etfTab), QCoreApplication.translate("MainWindow", u"ETFs", None))
    # retranslateUi
