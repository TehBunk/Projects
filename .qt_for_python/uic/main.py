# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1220, 800))
        MainWindow.setMaximumSize(QSize(1220, 800))
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/1x/attach_money.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: #a9d6e5")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 70, 1201, 721))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiLight")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color:#89C2D9")
        self.page_overview = QWidget()
        self.page_overview.setObjectName(u"page_overview")
        self.page_overview.setStyleSheet(u"")
        self.listWidget_companylist = QListWidget(self.page_overview)
        QListWidgetItem(self.listWidget_companylist)
        self.listWidget_companylist.setObjectName(u"listWidget_companylist")
        self.listWidget_companylist.setGeometry(QRect(10, 80, 141, 631))
        self.listWidget_companylist.setFont(font)
        self.listWidget_companylist.setStyleSheet(u"background-color: #61a5c2; \n"
"border: 2px solid #468FAF;\n"
"")
        self.label_companylistsubheader = QLabel(self.page_overview)
        self.label_companylistsubheader.setObjectName(u"label_companylistsubheader")
        self.label_companylistsubheader.setGeometry(QRect(10, 50, 141, 21))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiLight")
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_companylistsubheader.setFont(font1)
        self.label_companylistsubheader.setStyleSheet(u"background-color: #61a5c2; border: 2px solid #468FAF;")
        self.label_companylistsubheader.setAlignment(Qt.AlignCenter)
        self.label_companylistheader = QLabel(self.page_overview)
        self.label_companylistheader.setObjectName(u"label_companylistheader")
        self.label_companylistheader.setGeometry(QRect(10, 10, 141, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiLight")
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_companylistheader.setFont(font2)
        self.label_companylistheader.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_companylistheader.setAlignment(Qt.AlignCenter)
        self.stackedWidget_overview = QStackedWidget(self.page_overview)
        self.stackedWidget_overview.setObjectName(u"stackedWidget_overview")
        self.stackedWidget_overview.setGeometry(QRect(160, 10, 1041, 701))
        self.stackedWidget_overview.setStyleSheet(u"")
        self.page_unloaded = QWidget()
        self.page_unloaded.setObjectName(u"page_unloaded")
        self.stackedWidget_overview.addWidget(self.page_unloaded)
        self.page_loaded = QWidget()
        self.page_loaded.setObjectName(u"page_loaded")
        self.frame_overview_backround = QFrame(self.page_loaded)
        self.frame_overview_backround.setObjectName(u"frame_overview_backround")
        self.frame_overview_backround.setGeometry(QRect(0, 440, 891, 261))
        font3 = QFont()
        font3.setPointSize(10)
        self.frame_overview_backround.setFont(font3)
        self.frame_overview_backround.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_backround.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_backround.setFrameShadow(QFrame.Raised)
        self.frame_overview_background_header = QFrame(self.frame_overview_backround)
        self.frame_overview_background_header.setObjectName(u"frame_overview_background_header")
        self.frame_overview_background_header.setGeometry(QRect(0, 0, 891, 51))
        self.frame_overview_background_header.setFont(font3)
        self.frame_overview_background_header.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_background_header.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_background_header.setFrameShadow(QFrame.Raised)
        self.label_metrics = QLabel(self.frame_overview_background_header)
        self.label_metrics.setObjectName(u"label_metrics")
        self.label_metrics.setGeometry(QRect(10, 10, 211, 31))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_metrics.setFont(font4)
        self.label_metrics.setAutoFillBackground(False)
        self.label_metrics.setStyleSheet(u"\n"
"QLabel {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"\n"
"}")
        self.label_metrics.setAlignment(Qt.AlignCenter)
        self.label_lastprice = QLabel(self.frame_overview_background_header)
        self.label_lastprice.setObjectName(u"label_lastprice")
        self.label_lastprice.setGeometry(QRect(230, 10, 101, 31))
        self.label_lastprice.setFont(font4)
        self.label_lastprice.setAutoFillBackground(False)
        self.label_lastprice.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_lastprice.setAlignment(Qt.AlignCenter)
        self.label_lastprice_data = QLabel(self.frame_overview_background_header)
        self.label_lastprice_data.setObjectName(u"label_lastprice_data")
        self.label_lastprice_data.setGeometry(QRect(340, 10, 101, 31))
        self.label_lastprice_data.setFont(font4)
        self.label_lastprice_data.setAutoFillBackground(False)
        self.label_lastprice_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_lastprice_data.setAlignment(Qt.AlignCenter)
        self.label_52weekhigh_data = QLabel(self.frame_overview_background_header)
        self.label_52weekhigh_data.setObjectName(u"label_52weekhigh_data")
        self.label_52weekhigh_data.setGeometry(QRect(560, 10, 101, 31))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiLight")
        font5.setPointSize(11)
        font5.setBold(False)
        self.label_52weekhigh_data.setFont(font5)
        self.label_52weekhigh_data.setAutoFillBackground(False)
        self.label_52weekhigh_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_52weekhigh_data.setAlignment(Qt.AlignCenter)
        self.label_52weekhigh = QLabel(self.frame_overview_background_header)
        self.label_52weekhigh.setObjectName(u"label_52weekhigh")
        self.label_52weekhigh.setGeometry(QRect(450, 10, 101, 31))
        self.label_52weekhigh.setFont(font5)
        self.label_52weekhigh.setAutoFillBackground(False)
        self.label_52weekhigh.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_52weekhigh.setAlignment(Qt.AlignCenter)
        self.label_52weeklow_data = QLabel(self.frame_overview_background_header)
        self.label_52weeklow_data.setObjectName(u"label_52weeklow_data")
        self.label_52weeklow_data.setGeometry(QRect(780, 10, 101, 31))
        self.label_52weeklow_data.setFont(font5)
        self.label_52weeklow_data.setAutoFillBackground(False)
        self.label_52weeklow_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_52weeklow_data.setAlignment(Qt.AlignCenter)
        self.label_52weeklow = QLabel(self.frame_overview_background_header)
        self.label_52weeklow.setObjectName(u"label_52weeklow")
        self.label_52weeklow.setGeometry(QRect(670, 10, 101, 31))
        self.label_52weeklow.setFont(font5)
        self.label_52weeklow.setAutoFillBackground(False)
        self.label_52weeklow.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_52weeklow.setAlignment(Qt.AlignCenter)
        self.label_5yearavgyield_data = QLabel(self.frame_overview_backround)
        self.label_5yearavgyield_data.setObjectName(u"label_5yearavgyield_data")
        self.label_5yearavgyield_data.setGeometry(QRect(120, 60, 101, 31))
        self.label_5yearavgyield_data.setFont(font5)
        self.label_5yearavgyield_data.setAutoFillBackground(False)
        self.label_5yearavgyield_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_5yearavgyield_data.setAlignment(Qt.AlignCenter)
        self.label_sharesoutstanding_data = QLabel(self.frame_overview_backround)
        self.label_sharesoutstanding_data.setObjectName(u"label_sharesoutstanding_data")
        self.label_sharesoutstanding_data.setGeometry(QRect(10, 220, 211, 31))
        self.label_sharesoutstanding_data.setFont(font5)
        self.label_sharesoutstanding_data.setAutoFillBackground(False)
        self.label_sharesoutstanding_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_sharesoutstanding_data.setAlignment(Qt.AlignCenter)
        self.label_currentyield_data = QLabel(self.frame_overview_backround)
        self.label_currentyield_data.setObjectName(u"label_currentyield_data")
        self.label_currentyield_data.setGeometry(QRect(120, 100, 101, 31))
        self.label_currentyield_data.setFont(font5)
        self.label_currentyield_data.setAutoFillBackground(False)
        self.label_currentyield_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_currentyield_data.setAlignment(Qt.AlignCenter)
        self.label_sharediv_data = QLabel(self.frame_overview_backround)
        self.label_sharediv_data.setObjectName(u"label_sharediv_data")
        self.label_sharediv_data.setGeometry(QRect(120, 140, 101, 31))
        self.label_sharediv_data.setFont(font5)
        self.label_sharediv_data.setAutoFillBackground(False)
        self.label_sharediv_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_sharediv_data.setAlignment(Qt.AlignCenter)
        self.label_beta_data = QLabel(self.frame_overview_backround)
        self.label_beta_data.setObjectName(u"label_beta_data")
        self.label_beta_data.setGeometry(QRect(340, 140, 101, 31))
        self.label_beta_data.setFont(font5)
        self.label_beta_data.setAutoFillBackground(False)
        self.label_beta_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_beta_data.setAlignment(Qt.AlignCenter)
        self.label_50dayma_data = QLabel(self.frame_overview_backround)
        self.label_50dayma_data.setObjectName(u"label_50dayma_data")
        self.label_50dayma_data.setGeometry(QRect(340, 100, 101, 31))
        self.label_50dayma_data.setFont(font5)
        self.label_50dayma_data.setAutoFillBackground(False)
        self.label_50dayma_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_50dayma_data.setAlignment(Qt.AlignCenter)
        self.label_enterprisevalue_data = QLabel(self.frame_overview_backround)
        self.label_enterprisevalue_data.setObjectName(u"label_enterprisevalue_data")
        self.label_enterprisevalue_data.setGeometry(QRect(230, 220, 211, 31))
        self.label_enterprisevalue_data.setFont(font5)
        self.label_enterprisevalue_data.setAutoFillBackground(False)
        self.label_enterprisevalue_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_enterprisevalue_data.setAlignment(Qt.AlignCenter)
        self.label_200dayma_data = QLabel(self.frame_overview_backround)
        self.label_200dayma_data.setObjectName(u"label_200dayma_data")
        self.label_200dayma_data.setGeometry(QRect(340, 60, 101, 31))
        self.label_200dayma_data.setFont(font5)
        self.label_200dayma_data.setAutoFillBackground(False)
        self.label_200dayma_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_200dayma_data.setAlignment(Qt.AlignCenter)
        self.label_200dayma = QLabel(self.frame_overview_backround)
        self.label_200dayma.setObjectName(u"label_200dayma")
        self.label_200dayma.setGeometry(QRect(230, 60, 101, 31))
        self.label_200dayma.setFont(font4)
        self.label_200dayma.setAutoFillBackground(False)
        self.label_200dayma.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_200dayma.setAlignment(Qt.AlignCenter)
        self.label_50dayma = QLabel(self.frame_overview_backround)
        self.label_50dayma.setObjectName(u"label_50dayma")
        self.label_50dayma.setGeometry(QRect(230, 100, 101, 31))
        self.label_50dayma.setFont(font4)
        self.label_50dayma.setAutoFillBackground(False)
        self.label_50dayma.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_50dayma.setAlignment(Qt.AlignCenter)
        self.label_5yearavgyield = QLabel(self.frame_overview_backround)
        self.label_5yearavgyield.setObjectName(u"label_5yearavgyield")
        self.label_5yearavgyield.setGeometry(QRect(10, 60, 101, 31))
        self.label_5yearavgyield.setFont(font4)
        self.label_5yearavgyield.setAutoFillBackground(False)
        self.label_5yearavgyield.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_5yearavgyield.setAlignment(Qt.AlignCenter)
        self.label_currentyield = QLabel(self.frame_overview_backround)
        self.label_currentyield.setObjectName(u"label_currentyield")
        self.label_currentyield.setGeometry(QRect(10, 100, 101, 31))
        self.label_currentyield.setFont(font4)
        self.label_currentyield.setAutoFillBackground(False)
        self.label_currentyield.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_currentyield.setAlignment(Qt.AlignCenter)
        self.label_sharediv = QLabel(self.frame_overview_backround)
        self.label_sharediv.setObjectName(u"label_sharediv")
        self.label_sharediv.setGeometry(QRect(10, 140, 101, 31))
        self.label_sharediv.setFont(font4)
        self.label_sharediv.setAutoFillBackground(False)
        self.label_sharediv.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_sharediv.setAlignment(Qt.AlignCenter)
        self.label_beta = QLabel(self.frame_overview_backround)
        self.label_beta.setObjectName(u"label_beta")
        self.label_beta.setGeometry(QRect(230, 140, 101, 31))
        self.label_beta.setFont(font4)
        self.label_beta.setAutoFillBackground(False)
        self.label_beta.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_beta.setAlignment(Qt.AlignCenter)
        self.label_enterprisevalue = QLabel(self.frame_overview_backround)
        self.label_enterprisevalue.setObjectName(u"label_enterprisevalue")
        self.label_enterprisevalue.setGeometry(QRect(230, 180, 211, 31))
        self.label_enterprisevalue.setFont(font4)
        self.label_enterprisevalue.setAutoFillBackground(False)
        self.label_enterprisevalue.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_enterprisevalue.setAlignment(Qt.AlignCenter)
        self.label_sharesoutstanding = QLabel(self.frame_overview_backround)
        self.label_sharesoutstanding.setObjectName(u"label_sharesoutstanding")
        self.label_sharesoutstanding.setGeometry(QRect(10, 180, 211, 31))
        self.label_sharesoutstanding.setFont(font4)
        self.label_sharesoutstanding.setAutoFillBackground(False)
        self.label_sharesoutstanding.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_sharesoutstanding.setAlignment(Qt.AlignCenter)
        self.label_targetmed_data = QLabel(self.frame_overview_backround)
        self.label_targetmed_data.setObjectName(u"label_targetmed_data")
        self.label_targetmed_data.setGeometry(QRect(560, 140, 101, 31))
        self.label_targetmed_data.setFont(font5)
        self.label_targetmed_data.setAutoFillBackground(False)
        self.label_targetmed_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targetmed_data.setAlignment(Qt.AlignCenter)
        self.label_targetmed = QLabel(self.frame_overview_backround)
        self.label_targetmed.setObjectName(u"label_targetmed")
        self.label_targetmed.setGeometry(QRect(450, 140, 101, 31))
        self.label_targetmed.setFont(font4)
        self.label_targetmed.setAutoFillBackground(False)
        self.label_targetmed.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targetmed.setAlignment(Qt.AlignCenter)
        self.label_targethigh = QLabel(self.frame_overview_backround)
        self.label_targethigh.setObjectName(u"label_targethigh")
        self.label_targethigh.setGeometry(QRect(450, 100, 101, 31))
        self.label_targethigh.setFont(font4)
        self.label_targethigh.setAutoFillBackground(False)
        self.label_targethigh.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targethigh.setAlignment(Qt.AlignCenter)
        self.label_targetmean = QLabel(self.frame_overview_backround)
        self.label_targetmean.setObjectName(u"label_targetmean")
        self.label_targetmean.setGeometry(QRect(450, 60, 101, 31))
        self.label_targetmean.setFont(font4)
        self.label_targetmean.setAutoFillBackground(False)
        self.label_targetmean.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targetmean.setAlignment(Qt.AlignCenter)
        self.label_targetmean_data = QLabel(self.frame_overview_backround)
        self.label_targetmean_data.setObjectName(u"label_targetmean_data")
        self.label_targetmean_data.setGeometry(QRect(560, 60, 101, 31))
        self.label_targetmean_data.setFont(font5)
        self.label_targetmean_data.setAutoFillBackground(False)
        self.label_targetmean_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targetmean_data.setAlignment(Qt.AlignCenter)
        self.label_targethigh_data = QLabel(self.frame_overview_backround)
        self.label_targethigh_data.setObjectName(u"label_targethigh_data")
        self.label_targethigh_data.setGeometry(QRect(560, 100, 101, 31))
        self.label_targethigh_data.setFont(font5)
        self.label_targethigh_data.setAutoFillBackground(False)
        self.label_targethigh_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targethigh_data.setAlignment(Qt.AlignCenter)
        self.label_targetlow_data = QLabel(self.frame_overview_backround)
        self.label_targetlow_data.setObjectName(u"label_targetlow_data")
        self.label_targetlow_data.setGeometry(QRect(560, 180, 101, 31))
        self.label_targetlow_data.setFont(font5)
        self.label_targetlow_data.setAutoFillBackground(False)
        self.label_targetlow_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targetlow_data.setAlignment(Qt.AlignCenter)
        self.label_targetlow = QLabel(self.frame_overview_backround)
        self.label_targetlow.setObjectName(u"label_targetlow")
        self.label_targetlow.setGeometry(QRect(450, 180, 101, 31))
        self.label_targetlow.setFont(font4)
        self.label_targetlow.setAutoFillBackground(False)
        self.label_targetlow.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_targetlow.setAlignment(Qt.AlignCenter)
        self.label_bookvalue = QLabel(self.frame_overview_backround)
        self.label_bookvalue.setObjectName(u"label_bookvalue")
        self.label_bookvalue.setGeometry(QRect(670, 60, 101, 31))
        self.label_bookvalue.setFont(font4)
        self.label_bookvalue.setAutoFillBackground(False)
        self.label_bookvalue.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_bookvalue.setAlignment(Qt.AlignCenter)
        self.label_bookvalue_data = QLabel(self.frame_overview_backround)
        self.label_bookvalue_data.setObjectName(u"label_bookvalue_data")
        self.label_bookvalue_data.setGeometry(QRect(780, 60, 101, 31))
        self.label_bookvalue_data.setFont(font5)
        self.label_bookvalue_data.setAutoFillBackground(False)
        self.label_bookvalue_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_bookvalue_data.setAlignment(Qt.AlignCenter)
        self.label_pricebook_data = QLabel(self.frame_overview_backround)
        self.label_pricebook_data.setObjectName(u"label_pricebook_data")
        self.label_pricebook_data.setGeometry(QRect(780, 100, 101, 31))
        self.label_pricebook_data.setFont(font5)
        self.label_pricebook_data.setAutoFillBackground(False)
        self.label_pricebook_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_pricebook_data.setAlignment(Qt.AlignCenter)
        self.label_pricebook = QLabel(self.frame_overview_backround)
        self.label_pricebook.setObjectName(u"label_pricebook")
        self.label_pricebook.setGeometry(QRect(670, 100, 101, 31))
        self.label_pricebook.setFont(font4)
        self.label_pricebook.setAutoFillBackground(False)
        self.label_pricebook.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_pricebook.setAlignment(Qt.AlignCenter)
        self.label_avgvolume_data = QLabel(self.frame_overview_backround)
        self.label_avgvolume_data.setObjectName(u"label_avgvolume_data")
        self.label_avgvolume_data.setGeometry(QRect(780, 180, 101, 31))
        self.label_avgvolume_data.setFont(font5)
        self.label_avgvolume_data.setAutoFillBackground(False)
        self.label_avgvolume_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_avgvolume_data.setAlignment(Qt.AlignCenter)
        self.label_rps = QLabel(self.frame_overview_backround)
        self.label_rps.setObjectName(u"label_rps")
        self.label_rps.setGeometry(QRect(670, 140, 101, 31))
        self.label_rps.setFont(font4)
        self.label_rps.setAutoFillBackground(False)
        self.label_rps.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_rps.setAlignment(Qt.AlignCenter)
        self.label_evebitda = QLabel(self.frame_overview_backround)
        self.label_evebitda.setObjectName(u"label_evebitda")
        self.label_evebitda.setGeometry(QRect(450, 220, 101, 31))
        self.label_evebitda.setFont(font4)
        self.label_evebitda.setAutoFillBackground(False)
        self.label_evebitda.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_evebitda.setAlignment(Qt.AlignCenter)
        self.label_evebitda_data = QLabel(self.frame_overview_backround)
        self.label_evebitda_data.setObjectName(u"label_evebitda_data")
        self.label_evebitda_data.setGeometry(QRect(560, 220, 101, 31))
        self.label_evebitda_data.setFont(font5)
        self.label_evebitda_data.setAutoFillBackground(False)
        self.label_evebitda_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_evebitda_data.setAlignment(Qt.AlignCenter)
        self.label_evr_data = QLabel(self.frame_overview_backround)
        self.label_evr_data.setObjectName(u"label_evr_data")
        self.label_evr_data.setGeometry(QRect(780, 220, 101, 31))
        self.label_evr_data.setFont(font5)
        self.label_evr_data.setAutoFillBackground(False)
        self.label_evr_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_evr_data.setAlignment(Qt.AlignCenter)
        self.label_evr = QLabel(self.frame_overview_backround)
        self.label_evr.setObjectName(u"label_evr")
        self.label_evr.setGeometry(QRect(670, 220, 101, 31))
        self.label_evr.setFont(font4)
        self.label_evr.setAutoFillBackground(False)
        self.label_evr.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_evr.setAlignment(Qt.AlignCenter)
        self.label_rps_data = QLabel(self.frame_overview_backround)
        self.label_rps_data.setObjectName(u"label_rps_data")
        self.label_rps_data.setGeometry(QRect(780, 140, 101, 31))
        self.label_rps_data.setFont(font5)
        self.label_rps_data.setAutoFillBackground(False)
        self.label_rps_data.setStyleSheet(u"QLabel {\n"
"border-radius:5px;\n"
"border: 2px solid #89C2D9;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_rps_data.setAlignment(Qt.AlignCenter)
        self.label_avgvolume = QLabel(self.frame_overview_backround)
        self.label_avgvolume.setObjectName(u"label_avgvolume")
        self.label_avgvolume.setGeometry(QRect(670, 180, 101, 31))
        self.label_avgvolume.setFont(font4)
        self.label_avgvolume.setAutoFillBackground(False)
        self.label_avgvolume.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #468FAF;\n"
"border-radius:5px;\n"
"border: 2px solid #2C7DA0;\n"
"}")
        self.label_avgvolume.setAlignment(Qt.AlignCenter)
        self.label_marketcap_data = QLabel(self.page_loaded)
        self.label_marketcap_data.setObjectName(u"label_marketcap_data")
        self.label_marketcap_data.setGeometry(QRect(110, 160, 341, 31))
        self.label_marketcap_data.setFont(font4)
        self.label_marketcap_data.setAutoFillBackground(False)
        self.label_marketcap_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_marketcap_data.setAlignment(Qt.AlignCenter)
        self.label_sector = QLabel(self.page_loaded)
        self.label_sector.setObjectName(u"label_sector")
        self.label_sector.setGeometry(QRect(0, 80, 101, 31))
        self.label_sector.setFont(font4)
        self.label_sector.setAutoFillBackground(False)
        self.label_sector.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"")
        self.label_sector.setAlignment(Qt.AlignCenter)
        self.label_industry = QLabel(self.page_loaded)
        self.label_industry.setObjectName(u"label_industry")
        self.label_industry.setGeometry(QRect(0, 120, 101, 31))
        self.label_industry.setFont(font4)
        self.label_industry.setAutoFillBackground(False)
        self.label_industry.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_industry.setAlignment(Qt.AlignCenter)
        self.label_company_data = QLabel(self.page_loaded)
        self.label_company_data.setObjectName(u"label_company_data")
        self.label_company_data.setGeometry(QRect(110, 40, 341, 31))
        self.label_company_data.setFont(font4)
        self.label_company_data.setAutoFillBackground(False)
        self.label_company_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_company_data.setAlignment(Qt.AlignCenter)
        self.frame_overview_chartbackground = QFrame(self.page_loaded)
        self.frame_overview_chartbackground.setObjectName(u"frame_overview_chartbackground")
        self.frame_overview_chartbackground.setGeometry(QRect(460, 0, 571, 271))
        self.frame_overview_chartbackground.setFont(font3)
        self.frame_overview_chartbackground.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_chartbackground.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_chartbackground.setFrameShadow(QFrame.Raised)
        self.frame_overview_chart = QFrame(self.frame_overview_chartbackground)
        self.frame_overview_chart.setObjectName(u"frame_overview_chart")
        self.frame_overview_chart.setGeometry(QRect(10, 10, 561, 251))
        self.frame_overview_chart.setStyleSheet(u"border: none")
        self.frame_overview_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_chart.setFrameShadow(QFrame.Raised)
        self.frame_overview_chart_3 = QFrame(self.page_loaded)
        self.frame_overview_chart_3.setObjectName(u"frame_overview_chart_3")
        self.frame_overview_chart_3.setGeometry(QRect(900, 280, 131, 421))
        self.frame_overview_chart_3.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_chart_3.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_chart_3.setFrameShadow(QFrame.Raised)
        self.label_companylistheader_3 = QLabel(self.page_loaded)
        self.label_companylistheader_3.setObjectName(u"label_companylistheader_3")
        self.label_companylistheader_3.setGeometry(QRect(0, 200, 451, 31))
        self.label_companylistheader_3.setFont(font2)
        self.label_companylistheader_3.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_companylistheader_3.setAlignment(Qt.AlignCenter)
        self.label_industry_data = QLabel(self.page_loaded)
        self.label_industry_data.setObjectName(u"label_industry_data")
        self.label_industry_data.setGeometry(QRect(110, 120, 341, 31))
        self.label_industry_data.setFont(font4)
        self.label_industry_data.setAutoFillBackground(False)
        self.label_industry_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_industry_data.setAlignment(Qt.AlignCenter)
        self.textBrowser_description_data = QTextBrowser(self.page_loaded)
        self.textBrowser_description_data.setObjectName(u"textBrowser_description_data")
        self.textBrowser_description_data.setGeometry(QRect(0, 280, 891, 151))
        self.textBrowser_description_data.setStyleSheet(u"QTextBrowser {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"padding: 5px;\n"
"}\n"
"QTextBrowser:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_marketcap = QLabel(self.page_loaded)
        self.label_marketcap.setObjectName(u"label_marketcap")
        self.label_marketcap.setGeometry(QRect(0, 160, 101, 31))
        self.label_marketcap.setFont(font4)
        self.label_marketcap.setAutoFillBackground(False)
        self.label_marketcap.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_marketcap.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.page_loaded)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 240, 451, 31))
        self.label_description.setFont(font4)
        self.label_description.setAutoFillBackground(False)
        self.label_description.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_company = QLabel(self.page_loaded)
        self.label_company.setObjectName(u"label_company")
        self.label_company.setGeometry(QRect(0, 40, 101, 31))
        self.label_company.setFont(font4)
        self.label_company.setAutoFillBackground(False)
        self.label_company.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_company.setAlignment(Qt.AlignCenter)
        self.label_sector_data = QLabel(self.page_loaded)
        self.label_sector_data.setObjectName(u"label_sector_data")
        self.label_sector_data.setGeometry(QRect(110, 80, 341, 31))
        self.label_sector_data.setFont(font4)
        self.label_sector_data.setAutoFillBackground(False)
        self.label_sector_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_sector_data.setAlignment(Qt.AlignCenter)
        self.label_companylistheader_2 = QLabel(self.page_loaded)
        self.label_companylistheader_2.setObjectName(u"label_companylistheader_2")
        self.label_companylistheader_2.setGeometry(QRect(0, 0, 451, 31))
        self.label_companylistheader_2.setFont(font2)
        self.label_companylistheader_2.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_companylistheader_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget_overview.addWidget(self.page_loaded)
        self.stackedWidget.addWidget(self.page_overview)
        self.stackedWidget_overview.raise_()
        self.listWidget_companylist.raise_()
        self.label_companylistsubheader.raise_()
        self.label_companylistheader.raise_()
        self.page_chartview = QWidget()
        self.page_chartview.setObjectName(u"page_chartview")
        self.stackedWidget_chartview = QStackedWidget(self.page_chartview)
        self.stackedWidget_chartview.setObjectName(u"stackedWidget_chartview")
        self.stackedWidget_chartview.setGeometry(QRect(159, 49, 1041, 671))
        self.stackedWidget_chartview.setStyleSheet(u"background-color:#61A5C2")
        self.page_chartview_quad = QWidget()
        self.page_chartview_quad.setObjectName(u"page_chartview_quad")
        self.frame_chartview_quad_chartbackground1 = QFrame(self.page_chartview_quad)
        self.frame_chartview_quad_chartbackground1.setObjectName(u"frame_chartview_quad_chartbackground1")
        self.frame_chartview_quad_chartbackground1.setGeometry(QRect(10, 40, 501, 291))
        self.frame_chartview_quad_chartbackground1.setFont(font3)
        self.frame_chartview_quad_chartbackground1.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_quad_chartbackground1.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chartbackground1.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chart1 = QFrame(self.frame_chartview_quad_chartbackground1)
        self.frame_chartview_quad_chart1.setObjectName(u"frame_chartview_quad_chart1")
        self.frame_chartview_quad_chart1.setGeometry(QRect(10, 10, 481, 271))
        self.frame_chartview_quad_chart1.setStyleSheet(u"border: none")
        self.frame_chartview_quad_chart1.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chart1.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chartbackground2 = QFrame(self.page_chartview_quad)
        self.frame_chartview_quad_chartbackground2.setObjectName(u"frame_chartview_quad_chartbackground2")
        self.frame_chartview_quad_chartbackground2.setGeometry(QRect(530, 40, 501, 291))
        self.frame_chartview_quad_chartbackground2.setFont(font3)
        self.frame_chartview_quad_chartbackground2.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_quad_chartbackground2.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chartbackground2.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chart2 = QFrame(self.frame_chartview_quad_chartbackground2)
        self.frame_chartview_quad_chart2.setObjectName(u"frame_chartview_quad_chart2")
        self.frame_chartview_quad_chart2.setGeometry(QRect(10, 10, 481, 271))
        self.frame_chartview_quad_chart2.setStyleSheet(u"border: none")
        self.frame_chartview_quad_chart2.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chart2.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chartbackground3 = QFrame(self.page_chartview_quad)
        self.frame_chartview_quad_chartbackground3.setObjectName(u"frame_chartview_quad_chartbackground3")
        self.frame_chartview_quad_chartbackground3.setGeometry(QRect(10, 370, 501, 291))
        self.frame_chartview_quad_chartbackground3.setFont(font3)
        self.frame_chartview_quad_chartbackground3.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_quad_chartbackground3.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chartbackground3.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chart3 = QFrame(self.frame_chartview_quad_chartbackground3)
        self.frame_chartview_quad_chart3.setObjectName(u"frame_chartview_quad_chart3")
        self.frame_chartview_quad_chart3.setGeometry(QRect(10, 10, 481, 271))
        self.frame_chartview_quad_chart3.setStyleSheet(u"border: none")
        self.frame_chartview_quad_chart3.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chart3.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chartbackground4 = QFrame(self.page_chartview_quad)
        self.frame_chartview_quad_chartbackground4.setObjectName(u"frame_chartview_quad_chartbackground4")
        self.frame_chartview_quad_chartbackground4.setGeometry(QRect(530, 370, 501, 291))
        self.frame_chartview_quad_chartbackground4.setFont(font3)
        self.frame_chartview_quad_chartbackground4.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_quad_chartbackground4.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chartbackground4.setFrameShadow(QFrame.Raised)
        self.frame_chartview_quad_chart4 = QFrame(self.frame_chartview_quad_chartbackground4)
        self.frame_chartview_quad_chart4.setObjectName(u"frame_chartview_quad_chart4")
        self.frame_chartview_quad_chart4.setGeometry(QRect(10, 10, 481, 271))
        self.frame_chartview_quad_chart4.setStyleSheet(u"border: none")
        self.frame_chartview_quad_chart4.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_quad_chart4.setFrameShadow(QFrame.Raised)
        self.label_chartview_quad_apply1 = QPushButton(self.page_chartview_quad)
        self.label_chartview_quad_apply1.setObjectName(u"label_chartview_quad_apply1")
        self.label_chartview_quad_apply1.setGeometry(QRect(180, 10, 121, 21))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift SemiLight")
        font6.setPointSize(12)
        self.label_chartview_quad_apply1.setFont(font6)
        self.label_chartview_quad_apply1.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.comboBox_chartview_chartviewselector_2 = QComboBox(self.page_chartview_quad)
        self.comboBox_chartview_chartviewselector_2.addItem("")
        self.comboBox_chartview_chartviewselector_2.addItem("")
        self.comboBox_chartview_chartviewselector_2.addItem("")
        self.comboBox_chartview_chartviewselector_2.addItem("")
        self.comboBox_chartview_chartviewselector_2.addItem("")
        self.comboBox_chartview_chartviewselector_2.setObjectName(u"comboBox_chartview_chartviewselector_2")
        self.comboBox_chartview_chartviewselector_2.setGeometry(QRect(310, 10, 201, 21))
        self.comboBox_chartview_chartviewselector_2.setFont(font4)
        self.comboBox_chartview_chartviewselector_2.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_chartviewselector_2.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_chartviewselector_2.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_chartview_chartviewselector_3 = QComboBox(self.page_chartview_quad)
        self.comboBox_chartview_chartviewselector_3.addItem("")
        self.comboBox_chartview_chartviewselector_3.addItem("")
        self.comboBox_chartview_chartviewselector_3.addItem("")
        self.comboBox_chartview_chartviewselector_3.addItem("")
        self.comboBox_chartview_chartviewselector_3.addItem("")
        self.comboBox_chartview_chartviewselector_3.setObjectName(u"comboBox_chartview_chartviewselector_3")
        self.comboBox_chartview_chartviewselector_3.setGeometry(QRect(830, 10, 201, 21))
        self.comboBox_chartview_chartviewselector_3.setFont(font4)
        self.comboBox_chartview_chartviewselector_3.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_chartviewselector_3.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_chartviewselector_3.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_chartview_quad_apply2 = QPushButton(self.page_chartview_quad)
        self.label_chartview_quad_apply2.setObjectName(u"label_chartview_quad_apply2")
        self.label_chartview_quad_apply2.setGeometry(QRect(700, 10, 121, 21))
        self.label_chartview_quad_apply2.setFont(font6)
        self.label_chartview_quad_apply2.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.label_chartview_quad_apply4 = QPushButton(self.page_chartview_quad)
        self.label_chartview_quad_apply4.setObjectName(u"label_chartview_quad_apply4")
        self.label_chartview_quad_apply4.setGeometry(QRect(700, 340, 121, 21))
        self.label_chartview_quad_apply4.setFont(font6)
        self.label_chartview_quad_apply4.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.comboBox_chartview_chartviewselector_4 = QComboBox(self.page_chartview_quad)
        self.comboBox_chartview_chartviewselector_4.addItem("")
        self.comboBox_chartview_chartviewselector_4.addItem("")
        self.comboBox_chartview_chartviewselector_4.addItem("")
        self.comboBox_chartview_chartviewselector_4.addItem("")
        self.comboBox_chartview_chartviewselector_4.addItem("")
        self.comboBox_chartview_chartviewselector_4.setObjectName(u"comboBox_chartview_chartviewselector_4")
        self.comboBox_chartview_chartviewselector_4.setGeometry(QRect(310, 340, 201, 21))
        self.comboBox_chartview_chartviewselector_4.setFont(font4)
        self.comboBox_chartview_chartviewselector_4.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_chartviewselector_4.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_chartviewselector_4.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_chartview_quad_apply3 = QPushButton(self.page_chartview_quad)
        self.label_chartview_quad_apply3.setObjectName(u"label_chartview_quad_apply3")
        self.label_chartview_quad_apply3.setGeometry(QRect(180, 340, 121, 21))
        self.label_chartview_quad_apply3.setFont(font6)
        self.label_chartview_quad_apply3.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.comboBox_chartview_chartviewselector_5 = QComboBox(self.page_chartview_quad)
        self.comboBox_chartview_chartviewselector_5.addItem("")
        self.comboBox_chartview_chartviewselector_5.addItem("")
        self.comboBox_chartview_chartviewselector_5.addItem("")
        self.comboBox_chartview_chartviewselector_5.addItem("")
        self.comboBox_chartview_chartviewselector_5.addItem("")
        self.comboBox_chartview_chartviewselector_5.setObjectName(u"comboBox_chartview_chartviewselector_5")
        self.comboBox_chartview_chartviewselector_5.setGeometry(QRect(830, 340, 201, 21))
        self.comboBox_chartview_chartviewselector_5.setFont(font4)
        self.comboBox_chartview_chartviewselector_5.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_chartviewselector_5.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_chartviewselector_5.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_chartview_quad_chart1 = QLabel(self.page_chartview_quad)
        self.label_chartview_quad_chart1.setObjectName(u"label_chartview_quad_chart1")
        self.label_chartview_quad_chart1.setGeometry(QRect(10, 10, 161, 21))
        self.label_chartview_quad_chart1.setFont(font4)
        self.label_chartview_quad_chart1.setAutoFillBackground(False)
        self.label_chartview_quad_chart1.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_quad_chart1.setAlignment(Qt.AlignCenter)
        self.label_chartview_quad_chart2 = QLabel(self.page_chartview_quad)
        self.label_chartview_quad_chart2.setObjectName(u"label_chartview_quad_chart2")
        self.label_chartview_quad_chart2.setGeometry(QRect(530, 10, 161, 21))
        self.label_chartview_quad_chart2.setFont(font4)
        self.label_chartview_quad_chart2.setAutoFillBackground(False)
        self.label_chartview_quad_chart2.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_quad_chart2.setAlignment(Qt.AlignCenter)
        self.label_chartview_quad_chart3 = QLabel(self.page_chartview_quad)
        self.label_chartview_quad_chart3.setObjectName(u"label_chartview_quad_chart3")
        self.label_chartview_quad_chart3.setGeometry(QRect(10, 340, 161, 21))
        self.label_chartview_quad_chart3.setFont(font4)
        self.label_chartview_quad_chart3.setAutoFillBackground(False)
        self.label_chartview_quad_chart3.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_quad_chart3.setAlignment(Qt.AlignCenter)
        self.label_chartview_quad_chart4 = QLabel(self.page_chartview_quad)
        self.label_chartview_quad_chart4.setObjectName(u"label_chartview_quad_chart4")
        self.label_chartview_quad_chart4.setGeometry(QRect(530, 340, 161, 21))
        self.label_chartview_quad_chart4.setFont(font4)
        self.label_chartview_quad_chart4.setAutoFillBackground(False)
        self.label_chartview_quad_chart4.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_quad_chart4.setAlignment(Qt.AlignCenter)
        self.stackedWidget_chartview.addWidget(self.page_chartview_quad)
        self.page_chartview_split = QWidget()
        self.page_chartview_split.setObjectName(u"page_chartview_split")
        self.frame_chartview_split_chartbackground1 = QFrame(self.page_chartview_split)
        self.frame_chartview_split_chartbackground1.setObjectName(u"frame_chartview_split_chartbackground1")
        self.frame_chartview_split_chartbackground1.setGeometry(QRect(210, 10, 821, 321))
        self.frame_chartview_split_chartbackground1.setFont(font3)
        self.frame_chartview_split_chartbackground1.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_split_chartbackground1.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_split_chartbackground1.setFrameShadow(QFrame.Raised)
        self.frame_chartview_split_chart1 = QFrame(self.frame_chartview_split_chartbackground1)
        self.frame_chartview_split_chart1.setObjectName(u"frame_chartview_split_chart1")
        self.frame_chartview_split_chart1.setGeometry(QRect(10, 10, 801, 301))
        self.frame_chartview_split_chart1.setStyleSheet(u"border: none")
        self.frame_chartview_split_chart1.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_split_chart1.setFrameShadow(QFrame.Raised)
        self.label_chartview_split_chart2 = QLabel(self.page_chartview_split)
        self.label_chartview_split_chart2.setObjectName(u"label_chartview_split_chart2")
        self.label_chartview_split_chart2.setGeometry(QRect(10, 340, 191, 21))
        self.label_chartview_split_chart2.setFont(font4)
        self.label_chartview_split_chart2.setAutoFillBackground(False)
        self.label_chartview_split_chart2.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_split_chart2.setAlignment(Qt.AlignCenter)
        self.comboBox_chartview_splitchartviewselector1 = QComboBox(self.page_chartview_split)
        self.comboBox_chartview_splitchartviewselector1.addItem("")
        self.comboBox_chartview_splitchartviewselector1.addItem("")
        self.comboBox_chartview_splitchartviewselector1.addItem("")
        self.comboBox_chartview_splitchartviewselector1.addItem("")
        self.comboBox_chartview_splitchartviewselector1.addItem("")
        self.comboBox_chartview_splitchartviewselector1.setObjectName(u"comboBox_chartview_splitchartviewselector1")
        self.comboBox_chartview_splitchartviewselector1.setGeometry(QRect(10, 400, 191, 21))
        self.comboBox_chartview_splitchartviewselector1.setFont(font4)
        self.comboBox_chartview_splitchartviewselector1.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_splitchartviewselector1.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_splitchartviewselector1.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.pushButton_chartview_split_apply2 = QPushButton(self.page_chartview_split)
        self.pushButton_chartview_split_apply2.setObjectName(u"pushButton_chartview_split_apply2")
        self.pushButton_chartview_split_apply2.setGeometry(QRect(10, 370, 191, 21))
        self.pushButton_chartview_split_apply2.setFont(font6)
        self.pushButton_chartview_split_apply2.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.comboBox_chartview_splitchartviewselector2 = QComboBox(self.page_chartview_split)
        self.comboBox_chartview_splitchartviewselector2.addItem("")
        self.comboBox_chartview_splitchartviewselector2.addItem("")
        self.comboBox_chartview_splitchartviewselector2.addItem("")
        self.comboBox_chartview_splitchartviewselector2.addItem("")
        self.comboBox_chartview_splitchartviewselector2.addItem("")
        self.comboBox_chartview_splitchartviewselector2.setObjectName(u"comboBox_chartview_splitchartviewselector2")
        self.comboBox_chartview_splitchartviewselector2.setGeometry(QRect(10, 70, 191, 21))
        self.comboBox_chartview_splitchartviewselector2.setFont(font4)
        self.comboBox_chartview_splitchartviewselector2.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_splitchartviewselector2.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_splitchartviewselector2.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.pushButton_chartview_split_apply1 = QPushButton(self.page_chartview_split)
        self.pushButton_chartview_split_apply1.setObjectName(u"pushButton_chartview_split_apply1")
        self.pushButton_chartview_split_apply1.setGeometry(QRect(10, 40, 191, 21))
        self.pushButton_chartview_split_apply1.setFont(font6)
        self.pushButton_chartview_split_apply1.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.label_chartview_split_chart1 = QLabel(self.page_chartview_split)
        self.label_chartview_split_chart1.setObjectName(u"label_chartview_split_chart1")
        self.label_chartview_split_chart1.setGeometry(QRect(10, 10, 191, 21))
        self.label_chartview_split_chart1.setFont(font4)
        self.label_chartview_split_chart1.setAutoFillBackground(False)
        self.label_chartview_split_chart1.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_split_chart1.setAlignment(Qt.AlignCenter)
        self.frame_chartview_split_chartbackground2 = QFrame(self.page_chartview_split)
        self.frame_chartview_split_chartbackground2.setObjectName(u"frame_chartview_split_chartbackground2")
        self.frame_chartview_split_chartbackground2.setGeometry(QRect(210, 340, 821, 321))
        self.frame_chartview_split_chartbackground2.setFont(font3)
        self.frame_chartview_split_chartbackground2.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_split_chartbackground2.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_split_chartbackground2.setFrameShadow(QFrame.Raised)
        self.frame_chartview_split_chart2 = QFrame(self.frame_chartview_split_chartbackground2)
        self.frame_chartview_split_chart2.setObjectName(u"frame_chartview_split_chart2")
        self.frame_chartview_split_chart2.setGeometry(QRect(10, 10, 801, 301))
        self.frame_chartview_split_chart2.setStyleSheet(u"border: none")
        self.frame_chartview_split_chart2.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_split_chart2.setFrameShadow(QFrame.Raised)
        self.label_chartview_split_datainview1 = QLabel(self.page_chartview_split)
        self.label_chartview_split_datainview1.setObjectName(u"label_chartview_split_datainview1")
        self.label_chartview_split_datainview1.setGeometry(QRect(10, 140, 191, 21))
        self.label_chartview_split_datainview1.setFont(font1)
        self.label_chartview_split_datainview1.setStyleSheet(u"background-color: #61a5c2; border: 2px solid #468FAF;")
        self.label_chartview_split_datainview1.setAlignment(Qt.AlignCenter)
        self.listWidget_chartview_split_selection1 = QListWidget(self.page_chartview_split)
        QListWidgetItem(self.listWidget_chartview_split_selection1)
        self.listWidget_chartview_split_selection1.setObjectName(u"listWidget_chartview_split_selection1")
        self.listWidget_chartview_split_selection1.setGeometry(QRect(10, 170, 191, 161))
        self.listWidget_chartview_split_selection1.setFont(font)
        self.listWidget_chartview_split_selection1.setStyleSheet(u"background-color: #61a5c2; \n"
"border: 2px solid #468FAF;\n"
"")
        self.label_chartview_split_currentlyviewing1 = QLabel(self.page_chartview_split)
        self.label_chartview_split_currentlyviewing1.setObjectName(u"label_chartview_split_currentlyviewing1")
        self.label_chartview_split_currentlyviewing1.setGeometry(QRect(10, 100, 191, 31))
        self.label_chartview_split_currentlyviewing1.setFont(font2)
        self.label_chartview_split_currentlyviewing1.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_chartview_split_currentlyviewing1.setAlignment(Qt.AlignCenter)
        self.label_chartview_split_datainview2 = QLabel(self.page_chartview_split)
        self.label_chartview_split_datainview2.setObjectName(u"label_chartview_split_datainview2")
        self.label_chartview_split_datainview2.setGeometry(QRect(10, 470, 191, 21))
        self.label_chartview_split_datainview2.setFont(font1)
        self.label_chartview_split_datainview2.setStyleSheet(u"background-color: #61a5c2; border: 2px solid #468FAF;")
        self.label_chartview_split_datainview2.setAlignment(Qt.AlignCenter)
        self.listWidget_chartview_split_selection2 = QListWidget(self.page_chartview_split)
        self.listWidget_chartview_split_selection2.setObjectName(u"listWidget_chartview_split_selection2")
        self.listWidget_chartview_split_selection2.setGeometry(QRect(10, 500, 191, 161))
        self.listWidget_chartview_split_selection2.setFont(font)
        self.listWidget_chartview_split_selection2.setStyleSheet(u"background-color: #61a5c2; \n"
"border: 2px solid #468FAF;\n"
"")
        self.label_chartview_split_currentlyviewing2 = QLabel(self.page_chartview_split)
        self.label_chartview_split_currentlyviewing2.setObjectName(u"label_chartview_split_currentlyviewing2")
        self.label_chartview_split_currentlyviewing2.setGeometry(QRect(10, 430, 191, 31))
        self.label_chartview_split_currentlyviewing2.setFont(font2)
        self.label_chartview_split_currentlyviewing2.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_chartview_split_currentlyviewing2.setAlignment(Qt.AlignCenter)
        self.stackedWidget_chartview.addWidget(self.page_chartview_split)
        self.page_chartview_single = QWidget()
        self.page_chartview_single.setObjectName(u"page_chartview_single")
        self.frame_chartview_single_chartbackground = QFrame(self.page_chartview_single)
        self.frame_chartview_single_chartbackground.setObjectName(u"frame_chartview_single_chartbackground")
        self.frame_chartview_single_chartbackground.setGeometry(QRect(10, 40, 1021, 621))
        self.frame_chartview_single_chartbackground.setFont(font3)
        self.frame_chartview_single_chartbackground.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_chartview_single_chartbackground.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_single_chartbackground.setFrameShadow(QFrame.Raised)
        self.frame_chartview_single_chart = QFrame(self.frame_chartview_single_chartbackground)
        self.frame_chartview_single_chart.setObjectName(u"frame_chartview_single_chart")
        self.frame_chartview_single_chart.setGeometry(QRect(10, 10, 1001, 601))
        self.frame_chartview_single_chart.setStyleSheet(u"border: none")
        self.frame_chartview_single_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chartview_single_chart.setFrameShadow(QFrame.Raised)
        self.pushButton_chartview_single_apply1 = QPushButton(self.page_chartview_single)
        self.pushButton_chartview_single_apply1.setObjectName(u"pushButton_chartview_single_apply1")
        self.pushButton_chartview_single_apply1.setGeometry(QRect(180, 10, 121, 21))
        self.pushButton_chartview_single_apply1.setFont(font6)
        self.pushButton_chartview_single_apply1.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.label_chartview_single_chart1 = QLabel(self.page_chartview_single)
        self.label_chartview_single_chart1.setObjectName(u"label_chartview_single_chart1")
        self.label_chartview_single_chart1.setGeometry(QRect(10, 10, 161, 21))
        self.label_chartview_single_chart1.setFont(font4)
        self.label_chartview_single_chart1.setAutoFillBackground(False)
        self.label_chartview_single_chart1.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_single_chart1.setAlignment(Qt.AlignCenter)
        self.comboBox_chartview_single_chartselector1 = QComboBox(self.page_chartview_single)
        self.comboBox_chartview_single_chartselector1.addItem("")
        self.comboBox_chartview_single_chartselector1.addItem("")
        self.comboBox_chartview_single_chartselector1.addItem("")
        self.comboBox_chartview_single_chartselector1.addItem("")
        self.comboBox_chartview_single_chartselector1.addItem("")
        self.comboBox_chartview_single_chartselector1.setObjectName(u"comboBox_chartview_single_chartselector1")
        self.comboBox_chartview_single_chartselector1.setGeometry(QRect(310, 10, 201, 21))
        self.comboBox_chartview_single_chartselector1.setFont(font4)
        self.comboBox_chartview_single_chartselector1.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_single_chartselector1.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_chartview_single_chartselector1.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.stackedWidget_chartview.addWidget(self.page_chartview_single)
        self.label_chartview_companyname = QLabel(self.page_chartview)
        self.label_chartview_companyname.setObjectName(u"label_chartview_companyname")
        self.label_chartview_companyname.setGeometry(QRect(160, 10, 441, 31))
        self.label_chartview_companyname.setFont(font4)
        self.label_chartview_companyname.setAutoFillBackground(False)
        self.label_chartview_companyname.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_chartview_companyname.setAlignment(Qt.AlignCenter)
        self.comboBox_chartview_chartviewselector = QComboBox(self.page_chartview)
        self.comboBox_chartview_chartviewselector.addItem("")
        self.comboBox_chartview_chartviewselector.addItem("")
        self.comboBox_chartview_chartviewselector.addItem("")
        self.comboBox_chartview_chartviewselector.setObjectName(u"comboBox_chartview_chartviewselector")
        self.comboBox_chartview_chartviewselector.setGeometry(QRect(610, 10, 131, 31))
        self.comboBox_chartview_chartviewselector.setFont(font4)
        self.comboBox_chartview_chartviewselector.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_chartview_chartviewselector.setStyleSheet(u"QComboBox {\n"
"background-color: #61a5c2;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.comboBox_chartview_chartviewselector.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_chartview_datatypes = QLabel(self.page_chartview)
        self.label_chartview_datatypes.setObjectName(u"label_chartview_datatypes")
        self.label_chartview_datatypes.setGeometry(QRect(10, 10, 141, 31))
        self.label_chartview_datatypes.setFont(font2)
        self.label_chartview_datatypes.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_chartview_datatypes.setAlignment(Qt.AlignCenter)
        self.listWidget_chartview_datatypeslist = QListWidget(self.page_chartview)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        QListWidgetItem(self.listWidget_chartview_datatypeslist)
        self.listWidget_chartview_datatypeslist.setObjectName(u"listWidget_chartview_datatypeslist")
        self.listWidget_chartview_datatypeslist.setGeometry(QRect(10, 80, 141, 631))
        self.listWidget_chartview_datatypeslist.setFont(font)
        self.listWidget_chartview_datatypeslist.setStyleSheet(u"QListWidget {\n"
"	background-color: #61a5c2; \n"
"	border: 2px solid #468FAF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #61a5c2;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #468FAF;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN BO"
                        "TTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #89C2D9f;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"")
        self.listWidget_chartview_datatypeslist.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_chartview_datatypeslist.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.label_chartview_datatypesdesc = QLabel(self.page_chartview)
        self.label_chartview_datatypesdesc.setObjectName(u"label_chartview_datatypesdesc")
        self.label_chartview_datatypesdesc.setGeometry(QRect(10, 50, 141, 21))
        self.label_chartview_datatypesdesc.setFont(font1)
        self.label_chartview_datatypesdesc.setStyleSheet(u"background-color: #61a5c2; border: 2px solid #468FAF;")
        self.label_chartview_datatypesdesc.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_chartview)
        self.page_dataview = QWidget()
        self.page_dataview.setObjectName(u"page_dataview")
        self.label_chartview_datatypesdesc_2 = QLabel(self.page_dataview)
        self.label_chartview_datatypesdesc_2.setObjectName(u"label_chartview_datatypesdesc_2")
        self.label_chartview_datatypesdesc_2.setGeometry(QRect(10, 50, 221, 21))
        self.label_chartview_datatypesdesc_2.setFont(font1)
        self.label_chartview_datatypesdesc_2.setStyleSheet(u"background-color: #61a5c2; border: 2px solid #468FAF;")
        self.label_chartview_datatypesdesc_2.setAlignment(Qt.AlignCenter)
        self.listWidget_chartview_datatypeslist_2 = QListWidget(self.page_dataview)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        QListWidgetItem(self.listWidget_chartview_datatypeslist_2)
        self.listWidget_chartview_datatypeslist_2.setObjectName(u"listWidget_chartview_datatypeslist_2")
        self.listWidget_chartview_datatypeslist_2.setGeometry(QRect(10, 80, 221, 631))
        self.listWidget_chartview_datatypeslist_2.setFont(font)
        self.listWidget_chartview_datatypeslist_2.setStyleSheet(u"QListWidget {\n"
"	background-color: #61a5c2; \n"
"	border: 2px solid #468FAF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #61a5c2;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #468FAF;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN BO"
                        "TTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #89C2D9f;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.listWidget_chartview_datatypeslist_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_chartview_datatypeslist_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.label_chartview_datatypes_2 = QLabel(self.page_dataview)
        self.label_chartview_datatypes_2.setObjectName(u"label_chartview_datatypes_2")
        self.label_chartview_datatypes_2.setGeometry(QRect(10, 10, 221, 31))
        self.label_chartview_datatypes_2.setFont(font2)
        self.label_chartview_datatypes_2.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_chartview_datatypes_2.setAlignment(Qt.AlignCenter)
        self.tableWidget_dataview_1 = QTableWidget(self.page_dataview)
        if (self.tableWidget_dataview_1.columnCount() < 12):
            self.tableWidget_dataview_1.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_dataview_1.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.tableWidget_dataview_1.rowCount() < 2):
            self.tableWidget_dataview_1.setRowCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_dataview_1.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_dataview_1.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_dataview_1.setItem(0, 0, __qtablewidgetitem14)
        self.tableWidget_dataview_1.setObjectName(u"tableWidget_dataview_1")
        self.tableWidget_dataview_1.setGeometry(QRect(240, 40, 951, 111))
        self.tableWidget_dataview_1.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #468FAF;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #89C2D9;\n"
"}")
        self.label_dataview_company = QLabel(self.page_dataview)
        self.label_dataview_company.setObjectName(u"label_dataview_company")
        self.label_dataview_company.setGeometry(QRect(730, 10, 101, 21))
        self.label_dataview_company.setFont(font4)
        self.label_dataview_company.setAutoFillBackground(False)
        self.label_dataview_company.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}")
        self.label_dataview_company.setAlignment(Qt.AlignCenter)
        self.label_dataview_company_data = QLabel(self.page_dataview)
        self.label_dataview_company_data.setObjectName(u"label_dataview_company_data")
        self.label_dataview_company_data.setGeometry(QRect(840, 10, 351, 21))
        self.label_dataview_company_data.setFont(font4)
        self.label_dataview_company_data.setAutoFillBackground(False)
        self.label_dataview_company_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_company_data.setAlignment(Qt.AlignCenter)
        self.label_dataview_loadeddata = QLabel(self.page_dataview)
        self.label_dataview_loadeddata.setObjectName(u"label_dataview_loadeddata")
        self.label_dataview_loadeddata.setGeometry(QRect(240, 10, 151, 21))
        self.label_dataview_loadeddata.setFont(font2)
        self.label_dataview_loadeddata.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_dataview_loadeddata.setAlignment(Qt.AlignCenter)
        self.label_dataview_selecteddatatype = QLabel(self.page_dataview)
        self.label_dataview_selecteddatatype.setObjectName(u"label_dataview_selecteddatatype")
        self.label_dataview_selecteddatatype.setGeometry(QRect(400, 10, 321, 21))
        self.label_dataview_selecteddatatype.setFont(font4)
        self.label_dataview_selecteddatatype.setAutoFillBackground(False)
        self.label_dataview_selecteddatatype.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_selecteddatatype.setAlignment(Qt.AlignCenter)
        self.tableWidget_dataview_2 = QTableWidget(self.page_dataview)
        if (self.tableWidget_dataview_2.columnCount() < 10):
            self.tableWidget_dataview_2.setColumnCount(10)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_dataview_2.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        if (self.tableWidget_dataview_2.rowCount() < 2):
            self.tableWidget_dataview_2.setRowCount(2)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_dataview_2.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_dataview_2.setVerticalHeaderItem(1, __qtablewidgetitem26)
        self.tableWidget_dataview_2.setObjectName(u"tableWidget_dataview_2")
        self.tableWidget_dataview_2.setGeometry(QRect(240, 190, 951, 111))
        self.tableWidget_dataview_2.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #468FAF;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #89C2D9;\n"
"}")
        self.label_dataview_projectforward = QLabel(self.page_dataview)
        self.label_dataview_projectforward.setObjectName(u"label_dataview_projectforward")
        self.label_dataview_projectforward.setGeometry(QRect(240, 160, 151, 21))
        self.label_dataview_projectforward.setFont(font2)
        self.label_dataview_projectforward.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_dataview_projectforward.setAlignment(Qt.AlignCenter)
        self.spinBox_dataview_change = QSpinBox(self.page_dataview)
        self.spinBox_dataview_change.setObjectName(u"spinBox_dataview_change")
        self.spinBox_dataview_change.setGeometry(QRect(620, 160, 51, 21))
        self.spinBox_dataview_change.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_change = QLabel(self.page_dataview)
        self.label_dataview_change.setObjectName(u"label_dataview_change")
        self.label_dataview_change.setGeometry(QRect(510, 160, 101, 21))
        self.label_dataview_change.setFont(font4)
        self.label_dataview_change.setAutoFillBackground(False)
        self.label_dataview_change.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_change.setAlignment(Qt.AlignCenter)
        self.checkBox_dataview_applychange = QCheckBox(self.page_dataview)
        self.checkBox_dataview_applychange.setObjectName(u"checkBox_dataview_applychange")
        self.checkBox_dataview_applychange.setGeometry(QRect(680, 160, 71, 21))
        self.checkBox_dataview_applychange.setFont(font6)
        self.checkBox_dataview_applychange.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_dataview_throttle = QSpinBox(self.page_dataview)
        self.spinBox_dataview_throttle.setObjectName(u"spinBox_dataview_throttle")
        self.spinBox_dataview_throttle.setGeometry(QRect(870, 160, 51, 21))
        self.spinBox_dataview_throttle.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_throttle = QLabel(self.page_dataview)
        self.label_dataview_throttle.setObjectName(u"label_dataview_throttle")
        self.label_dataview_throttle.setGeometry(QRect(760, 160, 101, 21))
        self.label_dataview_throttle.setFont(font4)
        self.label_dataview_throttle.setAutoFillBackground(False)
        self.label_dataview_throttle.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_throttle.setAlignment(Qt.AlignCenter)
        self.checkBox_dataview_applythrottle = QCheckBox(self.page_dataview)
        self.checkBox_dataview_applythrottle.setObjectName(u"checkBox_dataview_applythrottle")
        self.checkBox_dataview_applythrottle.setGeometry(QRect(930, 160, 71, 21))
        self.checkBox_dataview_applythrottle.setFont(font6)
        self.checkBox_dataview_applythrottle.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.comboBox_dataview_avgofyears = QComboBox(self.page_dataview)
        self.comboBox_dataview_avgofyears.addItem("")
        self.comboBox_dataview_avgofyears.addItem("")
        self.comboBox_dataview_avgofyears.addItem("")
        self.comboBox_dataview_avgofyears.setObjectName(u"comboBox_dataview_avgofyears")
        self.comboBox_dataview_avgofyears.setGeometry(QRect(1100, 160, 91, 21))
        self.comboBox_dataview_avgofyears.setFont(font4)
        self.comboBox_dataview_avgofyears.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_dataview_avgofyears.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_dataview_avgofyears.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_dataview_avgof = QLabel(self.page_dataview)
        self.label_dataview_avgof.setObjectName(u"label_dataview_avgof")
        self.label_dataview_avgof.setGeometry(QRect(1010, 160, 81, 21))
        self.label_dataview_avgof.setFont(font4)
        self.label_dataview_avgof.setAutoFillBackground(False)
        self.label_dataview_avgof.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_dataview_avgof.setAlignment(Qt.AlignCenter)
        self.comboBox_dataview_projectyears = QComboBox(self.page_dataview)
        self.comboBox_dataview_projectyears.addItem("")
        self.comboBox_dataview_projectyears.addItem("")
        self.comboBox_dataview_projectyears.addItem("")
        self.comboBox_dataview_projectyears.setObjectName(u"comboBox_dataview_projectyears")
        self.comboBox_dataview_projectyears.setGeometry(QRect(400, 160, 81, 21))
        self.comboBox_dataview_projectyears.setFont(font4)
        self.comboBox_dataview_projectyears.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_dataview_projectyears.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_dataview_projectyears.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.frame_dataview_chartbackground = QFrame(self.page_dataview)
        self.frame_dataview_chartbackground.setObjectName(u"frame_dataview_chartbackground")
        self.frame_dataview_chartbackground.setGeometry(QRect(240, 340, 951, 371))
        self.frame_dataview_chartbackground.setFont(font3)
        self.frame_dataview_chartbackground.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_dataview_chartbackground.setFrameShape(QFrame.StyledPanel)
        self.frame_dataview_chartbackground.setFrameShadow(QFrame.Raised)
        self.frame_dataview_chart = QFrame(self.frame_dataview_chartbackground)
        self.frame_dataview_chart.setObjectName(u"frame_dataview_chart")
        self.frame_dataview_chart.setGeometry(QRect(10, 10, 931, 381))
        self.frame_dataview_chart.setStyleSheet(u"border: none")
        self.frame_dataview_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_dataview_chart.setFrameShadow(QFrame.Raised)
        self.comboBox_dataview_chartselector = QComboBox(self.page_dataview)
        self.comboBox_dataview_chartselector.addItem("")
        self.comboBox_dataview_chartselector.addItem("")
        self.comboBox_dataview_chartselector.addItem("")
        self.comboBox_dataview_chartselector.addItem("")
        self.comboBox_dataview_chartselector.addItem("")
        self.comboBox_dataview_chartselector.setObjectName(u"comboBox_dataview_chartselector")
        self.comboBox_dataview_chartselector.setGeometry(QRect(400, 310, 201, 21))
        self.comboBox_dataview_chartselector.setFont(font4)
        self.comboBox_dataview_chartselector.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_dataview_chartselector.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_dataview_chartselector.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_dataview_visualized = QLabel(self.page_dataview)
        self.label_dataview_visualized.setObjectName(u"label_dataview_visualized")
        self.label_dataview_visualized.setGeometry(QRect(240, 310, 151, 21))
        self.label_dataview_visualized.setFont(font2)
        self.label_dataview_visualized.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_dataview_visualized.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_dataview)
        self.page_forecast = QWidget()
        self.page_forecast.setObjectName(u"page_forecast")
        self.tableWidget_forecast1 = QTableWidget(self.page_forecast)
        if (self.tableWidget_forecast1.columnCount() < 10):
            self.tableWidget_forecast1.setColumnCount(10)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_forecast1.setHorizontalHeaderItem(9, __qtablewidgetitem36)
        if (self.tableWidget_forecast1.rowCount() < 19):
            self.tableWidget_forecast1.setRowCount(19)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(8, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(9, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(10, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(11, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(12, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(13, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(14, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(15, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(16, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(17, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_forecast1.setVerticalHeaderItem(18, __qtablewidgetitem55)
        self.tableWidget_forecast1.setObjectName(u"tableWidget_forecast1")
        self.tableWidget_forecast1.setGeometry(QRect(240, 40, 951, 261))
        self.tableWidget_forecast1.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #468FAF;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #89C2D9;\n"
"}\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #61a5c2;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #468FAF;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::sub-line:vert"
                        "ical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #89C2D9f;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: #61a5c2;\n"
"    height: 14px;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal  {	\n"
"	background-color: #468FAF;\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"Q"
                        "ScrollBar::handle:horizontal :hover{	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::handle:horizontal :pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"")
        self.label_forecast_2 = QLabel(self.page_forecast)
        self.label_forecast_2.setObjectName(u"label_forecast_2")
        self.label_forecast_2.setGeometry(QRect(240, 10, 151, 21))
        self.label_forecast_2.setFont(font2)
        self.label_forecast_2.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast_2.setAlignment(Qt.AlignCenter)
        self.label_forecast_company_data = QLabel(self.page_forecast)
        self.label_forecast_company_data.setObjectName(u"label_forecast_company_data")
        self.label_forecast_company_data.setGeometry(QRect(400, 10, 351, 21))
        self.label_forecast_company_data.setFont(font4)
        self.label_forecast_company_data.setAutoFillBackground(False)
        self.label_forecast_company_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_company_data.setAlignment(Qt.AlignCenter)
        self.frame_forecast_chartbackground1 = QFrame(self.page_forecast)
        self.frame_forecast_chartbackground1.setObjectName(u"frame_forecast_chartbackground1")
        self.frame_forecast_chartbackground1.setGeometry(QRect(240, 340, 951, 371))
        self.frame_forecast_chartbackground1.setFont(font3)
        self.frame_forecast_chartbackground1.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_forecast_chartbackground1.setFrameShape(QFrame.StyledPanel)
        self.frame_forecast_chartbackground1.setFrameShadow(QFrame.Raised)
        self.frame_forecast_chart1 = QFrame(self.frame_forecast_chartbackground1)
        self.frame_forecast_chart1.setObjectName(u"frame_forecast_chart1")
        self.frame_forecast_chart1.setGeometry(QRect(10, 10, 931, 351))
        self.frame_forecast_chart1.setStyleSheet(u"border: none")
        self.frame_forecast_chart1.setFrameShape(QFrame.StyledPanel)
        self.frame_forecast_chart1.setFrameShadow(QFrame.Raised)
        self.label_forecast = QLabel(self.page_forecast)
        self.label_forecast.setObjectName(u"label_forecast")
        self.label_forecast.setGeometry(QRect(10, 10, 221, 31))
        self.label_forecast.setFont(font2)
        self.label_forecast.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast.setAlignment(Qt.AlignCenter)
        self.frame_forecast_controlpanel = QFrame(self.page_forecast)
        self.frame_forecast_controlpanel.setObjectName(u"frame_forecast_controlpanel")
        self.frame_forecast_controlpanel.setGeometry(QRect(10, 50, 221, 661))
        self.frame_forecast_controlpanel.setFont(font3)
        self.frame_forecast_controlpanel.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_forecast_controlpanel.setFrameShape(QFrame.StyledPanel)
        self.frame_forecast_controlpanel.setFrameShadow(QFrame.Raised)
        self.label_forecast_throttle_9 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_9.setObjectName(u"label_forecast_throttle_9")
        self.label_forecast_throttle_9.setGeometry(QRect(10, 159, 111, 21))
        self.label_forecast_throttle_9.setFont(font5)
        self.label_forecast_throttle_9.setAutoFillBackground(False)
        self.label_forecast_throttle_9.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_9.setAlignment(Qt.AlignCenter)
        self.spinBox_forecast_throttlefcf = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_throttlefcf.setObjectName(u"spinBox_forecast_throttlefcf")
        self.spinBox_forecast_throttlefcf.setGeometry(QRect(130, 159, 81, 21))
        self.spinBox_forecast_throttlefcf.setFont(font3)
        self.spinBox_forecast_throttlefcf.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.comboBox_forecast_avgofyears = QComboBox(self.frame_forecast_controlpanel)
        self.comboBox_forecast_avgofyears.addItem("")
        self.comboBox_forecast_avgofyears.addItem("")
        self.comboBox_forecast_avgofyears.addItem("")
        self.comboBox_forecast_avgofyears.addItem("")
        self.comboBox_forecast_avgofyears.setObjectName(u"comboBox_forecast_avgofyears")
        self.comboBox_forecast_avgofyears.setGeometry(QRect(130, 70, 81, 21))
        self.comboBox_forecast_avgofyears.setFont(font1)
        self.comboBox_forecast_avgofyears.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_forecast_avgofyears.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_forecast_avgofyears.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.checkBox_forecast_enabledfcf = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_enabledfcf.setObjectName(u"checkBox_forecast_enabledfcf")
        self.checkBox_forecast_enabledfcf.setGeometry(QRect(130, 129, 81, 21))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift SemiLight")
        font7.setPointSize(10)
        self.checkBox_forecast_enabledfcf.setFont(font7)
        self.checkBox_forecast_enabledfcf.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_12 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_12.setObjectName(u"label_forecast_throttle_12")
        self.label_forecast_throttle_12.setGeometry(QRect(10, 129, 111, 21))
        self.label_forecast_throttle_12.setFont(font5)
        self.label_forecast_throttle_12.setAutoFillBackground(False)
        self.label_forecast_throttle_12.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_12.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_13 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_13.setObjectName(u"label_forecast_throttle_13")
        self.label_forecast_throttle_13.setGeometry(QRect(10, 70, 111, 21))
        self.label_forecast_throttle_13.setFont(font5)
        self.label_forecast_throttle_13.setAutoFillBackground(False)
        self.label_forecast_throttle_13.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_13.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_14 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_14.setObjectName(u"label_forecast_throttle_14")
        self.label_forecast_throttle_14.setGeometry(QRect(10, 40, 111, 21))
        self.label_forecast_throttle_14.setFont(font5)
        self.label_forecast_throttle_14.setAutoFillBackground(False)
        self.label_forecast_throttle_14.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_14.setAlignment(Qt.AlignCenter)
        self.comboBox_forecast_projectyears = QComboBox(self.frame_forecast_controlpanel)
        self.comboBox_forecast_projectyears.addItem("")
        self.comboBox_forecast_projectyears.addItem("")
        self.comboBox_forecast_projectyears.addItem("")
        self.comboBox_forecast_projectyears.setObjectName(u"comboBox_forecast_projectyears")
        self.comboBox_forecast_projectyears.setGeometry(QRect(130, 40, 81, 21))
        self.comboBox_forecast_projectyears.setFont(font1)
        self.comboBox_forecast_projectyears.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_forecast_projectyears.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_forecast_projectyears.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.checkBox_forecast_enabledebitda = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_enabledebitda.setObjectName(u"checkBox_forecast_enabledebitda")
        self.checkBox_forecast_enabledebitda.setGeometry(QRect(130, 249, 81, 21))
        self.checkBox_forecast_enabledebitda.setFont(font7)
        self.checkBox_forecast_enabledebitda.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_forecast_throttleebitda = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_throttleebitda.setObjectName(u"spinBox_forecast_throttleebitda")
        self.spinBox_forecast_throttleebitda.setGeometry(QRect(130, 279, 81, 21))
        self.spinBox_forecast_throttleebitda.setFont(font3)
        self.spinBox_forecast_throttleebitda.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_15 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_15.setObjectName(u"label_forecast_throttle_15")
        self.label_forecast_throttle_15.setGeometry(QRect(10, 249, 111, 21))
        self.label_forecast_throttle_15.setFont(font5)
        self.label_forecast_throttle_15.setAutoFillBackground(False)
        self.label_forecast_throttle_15.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_15.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_16 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_16.setObjectName(u"label_forecast_throttle_16")
        self.label_forecast_throttle_16.setGeometry(QRect(10, 279, 111, 21))
        self.label_forecast_throttle_16.setFont(font5)
        self.label_forecast_throttle_16.setAutoFillBackground(False)
        self.label_forecast_throttle_16.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_16.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_19 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_19.setObjectName(u"label_forecast_throttle_19")
        self.label_forecast_throttle_19.setGeometry(QRect(10, 100, 201, 20))
        self.label_forecast_throttle_19.setFont(font2)
        self.label_forecast_throttle_19.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast_throttle_19.setAlignment(Qt.AlignCenter)
        self.checkBox_forecast_enabledfcfyield = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_enabledfcfyield.setObjectName(u"checkBox_forecast_enabledfcfyield")
        self.checkBox_forecast_enabledfcfyield.setGeometry(QRect(130, 189, 81, 21))
        self.checkBox_forecast_enabledfcfyield.setFont(font7)
        self.checkBox_forecast_enabledfcfyield.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_17 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_17.setObjectName(u"label_forecast_throttle_17")
        self.label_forecast_throttle_17.setGeometry(QRect(10, 189, 111, 21))
        self.label_forecast_throttle_17.setFont(font5)
        self.label_forecast_throttle_17.setAutoFillBackground(False)
        self.label_forecast_throttle_17.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_17.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_18 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_18.setObjectName(u"label_forecast_throttle_18")
        self.label_forecast_throttle_18.setGeometry(QRect(10, 219, 111, 21))
        self.label_forecast_throttle_18.setFont(font5)
        self.label_forecast_throttle_18.setAutoFillBackground(False)
        self.label_forecast_throttle_18.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_18.setAlignment(Qt.AlignCenter)
        self.spinBox_forecast_throttlefcfyield = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_throttlefcfyield.setObjectName(u"spinBox_forecast_throttlefcfyield")
        self.spinBox_forecast_throttlefcfyield.setGeometry(QRect(130, 219, 81, 21))
        self.spinBox_forecast_throttlefcfyield.setFont(font3)
        self.spinBox_forecast_throttlefcfyield.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_20 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_20.setObjectName(u"label_forecast_throttle_20")
        self.label_forecast_throttle_20.setGeometry(QRect(10, 369, 201, 21))
        self.label_forecast_throttle_20.setFont(font2)
        self.label_forecast_throttle_20.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast_throttle_20.setAlignment(Qt.AlignCenter)
        self.checkBox_forecast_enabledshares = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_enabledshares.setObjectName(u"checkBox_forecast_enabledshares")
        self.checkBox_forecast_enabledshares.setGeometry(QRect(130, 309, 81, 21))
        self.checkBox_forecast_enabledshares.setFont(font7)
        self.checkBox_forecast_enabledshares.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle.setObjectName(u"label_forecast_throttle")
        self.label_forecast_throttle.setGeometry(QRect(10, 309, 111, 21))
        self.label_forecast_throttle.setFont(font5)
        self.label_forecast_throttle.setAutoFillBackground(False)
        self.label_forecast_throttle.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_2 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_2.setObjectName(u"label_forecast_throttle_2")
        self.label_forecast_throttle_2.setGeometry(QRect(10, 339, 111, 21))
        self.label_forecast_throttle_2.setFont(font5)
        self.label_forecast_throttle_2.setAutoFillBackground(False)
        self.label_forecast_throttle_2.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_2.setAlignment(Qt.AlignCenter)
        self.spinBox_forecast_throttlesharesout = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_throttlesharesout.setObjectName(u"spinBox_forecast_throttlesharesout")
        self.spinBox_forecast_throttlesharesout.setGeometry(QRect(130, 339, 81, 21))
        self.spinBox_forecast_throttlesharesout.setFont(font3)
        self.spinBox_forecast_throttlesharesout.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_forecast_lockenabled_ebitda = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_lockenabled_ebitda.setObjectName(u"checkBox_forecast_lockenabled_ebitda")
        self.checkBox_forecast_lockenabled_ebitda.setGeometry(QRect(130, 519, 81, 21))
        self.checkBox_forecast_lockenabled_ebitda.setFont(font7)
        self.checkBox_forecast_lockenabled_ebitda.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_forecast_lockenabled_fcf = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_lockenabled_fcf.setObjectName(u"checkBox_forecast_lockenabled_fcf")
        self.checkBox_forecast_lockenabled_fcf.setGeometry(QRect(130, 399, 81, 21))
        self.checkBox_forecast_lockenabled_fcf.setFont(font7)
        self.checkBox_forecast_lockenabled_fcf.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_3 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_3.setObjectName(u"label_forecast_throttle_3")
        self.label_forecast_throttle_3.setGeometry(QRect(10, 399, 111, 21))
        self.label_forecast_throttle_3.setFont(font5)
        self.label_forecast_throttle_3.setAutoFillBackground(False)
        self.label_forecast_throttle_3.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_3.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_4 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_4.setObjectName(u"label_forecast_throttle_4")
        self.label_forecast_throttle_4.setGeometry(QRect(10, 459, 111, 21))
        self.label_forecast_throttle_4.setFont(font5)
        self.label_forecast_throttle_4.setAutoFillBackground(False)
        self.label_forecast_throttle_4.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_4.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_5 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_5.setObjectName(u"label_forecast_throttle_5")
        self.label_forecast_throttle_5.setGeometry(QRect(10, 579, 111, 21))
        self.label_forecast_throttle_5.setFont(font5)
        self.label_forecast_throttle_5.setAutoFillBackground(False)
        self.label_forecast_throttle_5.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_5.setAlignment(Qt.AlignCenter)
        self.checkBox_forecast_lockenabled_fcfyield = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_lockenabled_fcfyield.setObjectName(u"checkBox_forecast_lockenabled_fcfyield")
        self.checkBox_forecast_lockenabled_fcfyield.setGeometry(QRect(130, 459, 81, 21))
        self.checkBox_forecast_lockenabled_fcfyield.setFont(font7)
        self.checkBox_forecast_lockenabled_fcfyield.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_forecast_lockfcf = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_lockfcf.setObjectName(u"spinBox_forecast_lockfcf")
        self.spinBox_forecast_lockfcf.setGeometry(QRect(130, 429, 81, 21))
        self.spinBox_forecast_lockfcf.setFont(font3)
        self.spinBox_forecast_lockfcf.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_forecast_lockenabled_shares = QCheckBox(self.frame_forecast_controlpanel)
        self.checkBox_forecast_lockenabled_shares.setObjectName(u"checkBox_forecast_lockenabled_shares")
        self.checkBox_forecast_lockenabled_shares.setGeometry(QRect(130, 579, 81, 21))
        self.checkBox_forecast_lockenabled_shares.setFont(font7)
        self.checkBox_forecast_lockenabled_shares.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_forecast_lockshares = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_lockshares.setObjectName(u"spinBox_forecast_lockshares")
        self.spinBox_forecast_lockshares.setGeometry(QRect(130, 609, 81, 21))
        self.spinBox_forecast_lockshares.setFont(font3)
        self.spinBox_forecast_lockshares.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_6 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_6.setObjectName(u"label_forecast_throttle_6")
        self.label_forecast_throttle_6.setGeometry(QRect(10, 519, 111, 21))
        self.label_forecast_throttle_6.setFont(font5)
        self.label_forecast_throttle_6.setAutoFillBackground(False)
        self.label_forecast_throttle_6.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_6.setAlignment(Qt.AlignCenter)
        self.spinBox_forecast_lockfcfyield = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_lockfcfyield.setObjectName(u"spinBox_forecast_lockfcfyield")
        self.spinBox_forecast_lockfcfyield.setGeometry(QRect(130, 489, 81, 21))
        self.spinBox_forecast_lockfcfyield.setFont(font3)
        self.spinBox_forecast_lockfcfyield.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_forecast_lockebitda = QSpinBox(self.frame_forecast_controlpanel)
        self.spinBox_forecast_lockebitda.setObjectName(u"spinBox_forecast_lockebitda")
        self.spinBox_forecast_lockebitda.setGeometry(QRect(130, 549, 81, 21))
        self.spinBox_forecast_lockebitda.setFont(font3)
        self.spinBox_forecast_lockebitda.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_7 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_7.setObjectName(u"label_forecast_throttle_7")
        self.label_forecast_throttle_7.setGeometry(QRect(10, 429, 111, 21))
        self.label_forecast_throttle_7.setFont(font5)
        self.label_forecast_throttle_7.setAutoFillBackground(False)
        self.label_forecast_throttle_7.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_7.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_8 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_8.setObjectName(u"label_forecast_throttle_8")
        self.label_forecast_throttle_8.setGeometry(QRect(10, 489, 111, 21))
        self.label_forecast_throttle_8.setFont(font5)
        self.label_forecast_throttle_8.setAutoFillBackground(False)
        self.label_forecast_throttle_8.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_8.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_10 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_10.setObjectName(u"label_forecast_throttle_10")
        self.label_forecast_throttle_10.setGeometry(QRect(10, 549, 111, 21))
        self.label_forecast_throttle_10.setFont(font5)
        self.label_forecast_throttle_10.setAutoFillBackground(False)
        self.label_forecast_throttle_10.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_10.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_11 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_11.setObjectName(u"label_forecast_throttle_11")
        self.label_forecast_throttle_11.setGeometry(QRect(10, 609, 111, 21))
        self.label_forecast_throttle_11.setFont(font5)
        self.label_forecast_throttle_11.setAutoFillBackground(False)
        self.label_forecast_throttle_11.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_forecast_throttle_11.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_21 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_21.setObjectName(u"label_forecast_throttle_21")
        self.label_forecast_throttle_21.setGeometry(QRect(10, 10, 201, 20))
        self.label_forecast_throttle_21.setFont(font2)
        self.label_forecast_throttle_21.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast_throttle_21.setAlignment(Qt.AlignCenter)
        self.label_forecast_throttle_22 = QLabel(self.frame_forecast_controlpanel)
        self.label_forecast_throttle_22.setObjectName(u"label_forecast_throttle_22")
        self.label_forecast_throttle_22.setGeometry(QRect(0, 640, 221, 21))
        self.label_forecast_throttle_22.setFont(font1)
        self.label_forecast_throttle_22.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast_throttle_22.setAlignment(Qt.AlignCenter)
        self.comboBox_forecast_charttype1 = QComboBox(self.page_forecast)
        self.comboBox_forecast_charttype1.addItem("")
        self.comboBox_forecast_charttype1.addItem("")
        self.comboBox_forecast_charttype1.addItem("")
        self.comboBox_forecast_charttype1.addItem("")
        self.comboBox_forecast_charttype1.addItem("")
        self.comboBox_forecast_charttype1.setObjectName(u"comboBox_forecast_charttype1")
        self.comboBox_forecast_charttype1.setGeometry(QRect(400, 310, 201, 21))
        self.comboBox_forecast_charttype1.setFont(font4)
        self.comboBox_forecast_charttype1.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_forecast_charttype1.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_forecast_charttype1.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.label_forecast_3 = QLabel(self.page_forecast)
        self.label_forecast_3.setObjectName(u"label_forecast_3")
        self.label_forecast_3.setGeometry(QRect(240, 310, 151, 21))
        self.label_forecast_3.setFont(font2)
        self.label_forecast_3.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_forecast_3.setAlignment(Qt.AlignCenter)
        self.comboBox_forecast_chartselector1 = QComboBox(self.page_forecast)
        self.comboBox_forecast_chartselector1.addItem("")
        self.comboBox_forecast_chartselector1.addItem("")
        self.comboBox_forecast_chartselector1.addItem("")
        self.comboBox_forecast_chartselector1.addItem("")
        self.comboBox_forecast_chartselector1.setObjectName(u"comboBox_forecast_chartselector1")
        self.comboBox_forecast_chartselector1.setGeometry(QRect(610, 310, 221, 21))
        self.comboBox_forecast_chartselector1.setFont(font4)
        self.comboBox_forecast_chartselector1.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_forecast_chartselector1.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_forecast_chartselector1.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.stackedWidget.addWidget(self.page_forecast)
        self.page_checklist = QWidget()
        self.page_checklist.setObjectName(u"page_checklist")
        self.frame_checklist_2 = QFrame(self.page_checklist)
        self.frame_checklist_2.setObjectName(u"frame_checklist_2")
        self.frame_checklist_2.setGeometry(QRect(10, 10, 331, 491))
        self.frame_checklist_2.setFont(font3)
        self.frame_checklist_2.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_checklist_2.setFrameShape(QFrame.StyledPanel)
        self.frame_checklist_2.setFrameShadow(QFrame.Raised)
        self.label_checklist_8 = QLabel(self.frame_checklist_2)
        self.label_checklist_8.setObjectName(u"label_checklist_8")
        self.label_checklist_8.setGeometry(QRect(10, 40, 141, 21))
        self.label_checklist_8.setFont(font5)
        self.label_checklist_8.setAutoFillBackground(False)
        self.label_checklist_8.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_8.setAlignment(Qt.AlignCenter)
        self.label_checklist_24 = QLabel(self.frame_checklist_2)
        self.label_checklist_24.setObjectName(u"label_checklist_24")
        self.label_checklist_24.setGeometry(QRect(10, 70, 141, 21))
        self.label_checklist_24.setFont(font5)
        self.label_checklist_24.setAutoFillBackground(False)
        self.label_checklist_24.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_24.setAlignment(Qt.AlignCenter)
        self.label_checklist_23 = QLabel(self.frame_checklist_2)
        self.label_checklist_23.setObjectName(u"label_checklist_23")
        self.label_checklist_23.setGeometry(QRect(10, 100, 141, 21))
        self.label_checklist_23.setFont(font5)
        self.label_checklist_23.setAutoFillBackground(False)
        self.label_checklist_23.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_23.setAlignment(Qt.AlignCenter)
        self.label_checklist_22 = QLabel(self.frame_checklist_2)
        self.label_checklist_22.setObjectName(u"label_checklist_22")
        self.label_checklist_22.setGeometry(QRect(10, 130, 141, 21))
        self.label_checklist_22.setFont(font5)
        self.label_checklist_22.setAutoFillBackground(False)
        self.label_checklist_22.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_22.setAlignment(Qt.AlignCenter)
        self.label_checklist_21 = QLabel(self.frame_checklist_2)
        self.label_checklist_21.setObjectName(u"label_checklist_21")
        self.label_checklist_21.setGeometry(QRect(10, 160, 141, 21))
        self.label_checklist_21.setFont(font5)
        self.label_checklist_21.setAutoFillBackground(False)
        self.label_checklist_21.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_21.setAlignment(Qt.AlignCenter)
        self.label_checklist_20 = QLabel(self.frame_checklist_2)
        self.label_checklist_20.setObjectName(u"label_checklist_20")
        self.label_checklist_20.setGeometry(QRect(10, 190, 141, 21))
        self.label_checklist_20.setFont(font5)
        self.label_checklist_20.setAutoFillBackground(False)
        self.label_checklist_20.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_20.setAlignment(Qt.AlignCenter)
        self.label_checklist_19 = QLabel(self.frame_checklist_2)
        self.label_checklist_19.setObjectName(u"label_checklist_19")
        self.label_checklist_19.setGeometry(QRect(10, 220, 141, 21))
        self.label_checklist_19.setFont(font5)
        self.label_checklist_19.setAutoFillBackground(False)
        self.label_checklist_19.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_19.setAlignment(Qt.AlignCenter)
        self.label_checklist_18 = QLabel(self.frame_checklist_2)
        self.label_checklist_18.setObjectName(u"label_checklist_18")
        self.label_checklist_18.setGeometry(QRect(10, 250, 141, 21))
        self.label_checklist_18.setFont(font5)
        self.label_checklist_18.setAutoFillBackground(False)
        self.label_checklist_18.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_18.setAlignment(Qt.AlignCenter)
        self.label_checklist_17 = QLabel(self.frame_checklist_2)
        self.label_checklist_17.setObjectName(u"label_checklist_17")
        self.label_checklist_17.setGeometry(QRect(10, 280, 141, 21))
        self.label_checklist_17.setFont(font5)
        self.label_checklist_17.setAutoFillBackground(False)
        self.label_checklist_17.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_17.setAlignment(Qt.AlignCenter)
        self.label_checklist_16 = QLabel(self.frame_checklist_2)
        self.label_checklist_16.setObjectName(u"label_checklist_16")
        self.label_checklist_16.setGeometry(QRect(10, 340, 141, 21))
        self.label_checklist_16.setFont(font5)
        self.label_checklist_16.setAutoFillBackground(False)
        self.label_checklist_16.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_16.setAlignment(Qt.AlignCenter)
        self.label_checklist_15 = QLabel(self.frame_checklist_2)
        self.label_checklist_15.setObjectName(u"label_checklist_15")
        self.label_checklist_15.setGeometry(QRect(10, 400, 141, 21))
        self.label_checklist_15.setFont(font5)
        self.label_checklist_15.setAutoFillBackground(False)
        self.label_checklist_15.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_15.setAlignment(Qt.AlignCenter)
        self.label_checklist_14 = QLabel(self.frame_checklist_2)
        self.label_checklist_14.setObjectName(u"label_checklist_14")
        self.label_checklist_14.setGeometry(QRect(10, 430, 141, 21))
        self.label_checklist_14.setFont(font5)
        self.label_checklist_14.setAutoFillBackground(False)
        self.label_checklist_14.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_14.setAlignment(Qt.AlignCenter)
        self.label_checklist_13 = QLabel(self.frame_checklist_2)
        self.label_checklist_13.setObjectName(u"label_checklist_13")
        self.label_checklist_13.setGeometry(QRect(10, 460, 141, 21))
        self.label_checklist_13.setFont(font5)
        self.label_checklist_13.setAutoFillBackground(False)
        self.label_checklist_13.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_13.setAlignment(Qt.AlignCenter)
        self.label_checklist_11 = QLabel(self.frame_checklist_2)
        self.label_checklist_11.setObjectName(u"label_checklist_11")
        self.label_checklist_11.setGeometry(QRect(10, 10, 211, 20))
        self.label_checklist_11.setFont(font2)
        self.label_checklist_11.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_11.setAlignment(Qt.AlignCenter)
        self.label_checklist_10 = QLabel(self.frame_checklist_2)
        self.label_checklist_10.setObjectName(u"label_checklist_10")
        self.label_checklist_10.setGeometry(QRect(10, 370, 211, 20))
        self.label_checklist_10.setFont(font2)
        self.label_checklist_10.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_10.setAlignment(Qt.AlignCenter)
        self.checkBox_checklist_passprofit = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passprofit.setObjectName(u"checkBox_checklist_passprofit")
        self.checkBox_checklist_passprofit.setGeometry(QRect(160, 40, 61, 21))
        self.checkBox_checklist_passprofit.setFont(font6)
        self.checkBox_checklist_passprofit.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passrevenue = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passrevenue.setObjectName(u"checkBox_checklist_passrevenue")
        self.checkBox_checklist_passrevenue.setGeometry(QRect(160, 70, 61, 21))
        self.checkBox_checklist_passrevenue.setFont(font6)
        self.checkBox_checklist_passrevenue.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passearnings = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passearnings.setObjectName(u"checkBox_checklist_passearnings")
        self.checkBox_checklist_passearnings.setGeometry(QRect(160, 100, 61, 21))
        self.checkBox_checklist_passearnings.setFont(font6)
        self.checkBox_checklist_passearnings.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passassetsvsliabilties = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passassetsvsliabilties.setObjectName(u"checkBox_checklist_passassetsvsliabilties")
        self.checkBox_checklist_passassetsvsliabilties.setGeometry(QRect(160, 160, 61, 21))
        self.checkBox_checklist_passassetsvsliabilties.setFont(font6)
        self.checkBox_checklist_passassetsvsliabilties.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passassests = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passassests.setObjectName(u"checkBox_checklist_passassests")
        self.checkBox_checklist_passassests.setGeometry(QRect(160, 190, 61, 21))
        self.checkBox_checklist_passassests.setFont(font6)
        self.checkBox_checklist_passassests.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passfcf = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passfcf.setObjectName(u"checkBox_checklist_passfcf")
        self.checkBox_checklist_passfcf.setGeometry(QRect(160, 130, 61, 21))
        self.checkBox_checklist_passfcf.setFont(font6)
        self.checkBox_checklist_passfcf.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passpe = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passpe.setObjectName(u"checkBox_checklist_passpe")
        self.checkBox_checklist_passpe.setGeometry(QRect(160, 250, 61, 21))
        self.checkBox_checklist_passpe.setFont(font6)
        self.checkBox_checklist_passpe.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passshares = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passshares.setObjectName(u"checkBox_checklist_passshares")
        self.checkBox_checklist_passshares.setGeometry(QRect(160, 340, 61, 21))
        self.checkBox_checklist_passshares.setFont(font6)
        self.checkBox_checklist_passshares.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passsolidmoat = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passsolidmoat.setObjectName(u"checkBox_checklist_passsolidmoat")
        self.checkBox_checklist_passsolidmoat.setGeometry(QRect(160, 400, 61, 21))
        self.checkBox_checklist_passsolidmoat.setFont(font6)
        self.checkBox_checklist_passsolidmoat.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passsolidmanagment = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passsolidmanagment.setObjectName(u"checkBox_checklist_passsolidmanagment")
        self.checkBox_checklist_passsolidmanagment.setGeometry(QRect(160, 430, 61, 21))
        self.checkBox_checklist_passsolidmanagment.setFont(font6)
        self.checkBox_checklist_passsolidmanagment.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passfairfcfratio = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passfairfcfratio.setObjectName(u"checkBox_checklist_passfairfcfratio")
        self.checkBox_checklist_passfairfcfratio.setGeometry(QRect(160, 280, 61, 21))
        self.checkBox_checklist_passfairfcfratio.setFont(font6)
        self.checkBox_checklist_passfairfcfratio.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passfairliabilities = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passfairliabilities.setObjectName(u"checkBox_checklist_passfairliabilities")
        self.checkBox_checklist_passfairliabilities.setGeometry(QRect(160, 220, 61, 21))
        self.checkBox_checklist_passfairliabilities.setFont(font6)
        self.checkBox_checklist_passfairliabilities.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.checkBox_checklist_passinsiderbuying = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passinsiderbuying.setObjectName(u"checkBox_checklist_passinsiderbuying")
        self.checkBox_checklist_passinsiderbuying.setGeometry(QRect(160, 460, 61, 21))
        self.checkBox_checklist_passinsiderbuying.setFont(font6)
        self.checkBox_checklist_passinsiderbuying.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.comboBox_checklist_avgyeras = QComboBox(self.frame_checklist_2)
        self.comboBox_checklist_avgyeras.addItem("")
        self.comboBox_checklist_avgyeras.addItem("")
        self.comboBox_checklist_avgyeras.addItem("")
        self.comboBox_checklist_avgyeras.addItem("")
        self.comboBox_checklist_avgyeras.setObjectName(u"comboBox_checklist_avgyeras")
        self.comboBox_checklist_avgyeras.setGeometry(QRect(230, 10, 91, 21))
        self.comboBox_checklist_avgyeras.setFont(font4)
        self.comboBox_checklist_avgyeras.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_checklist_avgyeras.setStyleSheet(u"QComboBox {\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"	text-align: center;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}\n"
"")
        self.comboBox_checklist_avgyeras.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.spinBox_dataview_throttle_10 = QSpinBox(self.frame_checklist_2)
        self.spinBox_dataview_throttle_10.setObjectName(u"spinBox_dataview_throttle_10")
        self.spinBox_dataview_throttle_10.setGeometry(QRect(230, 250, 41, 21))
        self.spinBox_dataview_throttle_10.setFont(font3)
        self.spinBox_dataview_throttle_10.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_dataview_throttle_10.setMinimum(0)
        self.spinBox_dataview_throttle_10.setMaximum(99)
        self.spinBox_dataview_throttle_10.setValue(15)
        self.label_checklist_fairliabilties = QLabel(self.frame_checklist_2)
        self.label_checklist_fairliabilties.setObjectName(u"label_checklist_fairliabilties")
        self.label_checklist_fairliabilties.setGeometry(QRect(230, 220, 91, 21))
        self.label_checklist_fairliabilties.setFont(font5)
        self.label_checklist_fairliabilties.setAutoFillBackground(False)
        self.label_checklist_fairliabilties.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_fairliabilties.setAlignment(Qt.AlignCenter)
        self.label_checklist_assetgrowth = QLabel(self.frame_checklist_2)
        self.label_checklist_assetgrowth.setObjectName(u"label_checklist_assetgrowth")
        self.label_checklist_assetgrowth.setGeometry(QRect(230, 190, 91, 21))
        self.label_checklist_assetgrowth.setFont(font5)
        self.label_checklist_assetgrowth.setAutoFillBackground(False)
        self.label_checklist_assetgrowth.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_assetgrowth.setAlignment(Qt.AlignCenter)
        self.label_checklist_assetliabilties = QLabel(self.frame_checklist_2)
        self.label_checklist_assetliabilties.setObjectName(u"label_checklist_assetliabilties")
        self.label_checklist_assetliabilties.setGeometry(QRect(230, 160, 91, 21))
        self.label_checklist_assetliabilties.setFont(font5)
        self.label_checklist_assetliabilties.setAutoFillBackground(False)
        self.label_checklist_assetliabilties.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_assetliabilties.setAlignment(Qt.AlignCenter)
        self.label_checklist_fcfgrowth = QLabel(self.frame_checklist_2)
        self.label_checklist_fcfgrowth.setObjectName(u"label_checklist_fcfgrowth")
        self.label_checklist_fcfgrowth.setGeometry(QRect(230, 130, 91, 21))
        self.label_checklist_fcfgrowth.setFont(font5)
        self.label_checklist_fcfgrowth.setAutoFillBackground(False)
        self.label_checklist_fcfgrowth.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_fcfgrowth.setAlignment(Qt.AlignCenter)
        self.label_checklist_earningsgrowth = QLabel(self.frame_checklist_2)
        self.label_checklist_earningsgrowth.setObjectName(u"label_checklist_earningsgrowth")
        self.label_checklist_earningsgrowth.setGeometry(QRect(230, 100, 91, 21))
        self.label_checklist_earningsgrowth.setFont(font5)
        self.label_checklist_earningsgrowth.setAutoFillBackground(False)
        self.label_checklist_earningsgrowth.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_earningsgrowth.setAlignment(Qt.AlignCenter)
        self.label_checklist_revgrowth = QLabel(self.frame_checklist_2)
        self.label_checklist_revgrowth.setObjectName(u"label_checklist_revgrowth")
        self.label_checklist_revgrowth.setGeometry(QRect(230, 70, 91, 21))
        self.label_checklist_revgrowth.setFont(font5)
        self.label_checklist_revgrowth.setAutoFillBackground(False)
        self.label_checklist_revgrowth.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_revgrowth.setAlignment(Qt.AlignCenter)
        self.label_checklist_profitgrowth = QLabel(self.frame_checklist_2)
        self.label_checklist_profitgrowth.setObjectName(u"label_checklist_profitgrowth")
        self.label_checklist_profitgrowth.setGeometry(QRect(230, 40, 91, 21))
        self.label_checklist_profitgrowth.setFont(font5)
        self.label_checklist_profitgrowth.setAutoFillBackground(False)
        self.label_checklist_profitgrowth.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_profitgrowth.setAlignment(Qt.AlignCenter)
        self.label_checklistfcfratio = QLabel(self.frame_checklist_2)
        self.label_checklistfcfratio.setObjectName(u"label_checklistfcfratio")
        self.label_checklistfcfratio.setGeometry(QRect(280, 280, 41, 21))
        self.label_checklistfcfratio.setFont(font5)
        self.label_checklistfcfratio.setAutoFillBackground(False)
        self.label_checklistfcfratio.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklistfcfratio.setAlignment(Qt.AlignCenter)
        self.spinBox_dataview_throttle_11 = QSpinBox(self.frame_checklist_2)
        self.spinBox_dataview_throttle_11.setObjectName(u"spinBox_dataview_throttle_11")
        self.spinBox_dataview_throttle_11.setGeometry(QRect(230, 280, 41, 21))
        self.spinBox_dataview_throttle_11.setFont(font3)
        self.spinBox_dataview_throttle_11.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_dataview_throttle_11.setValue(15)
        self.checkBox_checklist_passsolidmargin = QCheckBox(self.frame_checklist_2)
        self.checkBox_checklist_passsolidmargin.setObjectName(u"checkBox_checklist_passsolidmargin")
        self.checkBox_checklist_passsolidmargin.setGeometry(QRect(160, 310, 61, 21))
        self.checkBox_checklist_passsolidmargin.setFont(font6)
        self.checkBox_checklist_passsolidmargin.setStyleSheet(u"QCheckBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QCheckBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_12 = QLabel(self.frame_checklist_2)
        self.label_checklist_12.setObjectName(u"label_checklist_12")
        self.label_checklist_12.setGeometry(QRect(10, 310, 141, 21))
        self.label_checklist_12.setFont(font5)
        self.label_checklist_12.setAutoFillBackground(False)
        self.label_checklist_12.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_12.setAlignment(Qt.AlignCenter)
        self.spinBox_dataview_throttle_12 = QSpinBox(self.frame_checklist_2)
        self.spinBox_dataview_throttle_12.setObjectName(u"spinBox_dataview_throttle_12")
        self.spinBox_dataview_throttle_12.setGeometry(QRect(230, 310, 41, 21))
        self.spinBox_dataview_throttle_12.setFont(font3)
        self.spinBox_dataview_throttle_12.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_dataview_throttle_12.setValue(15)
        self.label_checklist_profitmargin = QLabel(self.frame_checklist_2)
        self.label_checklist_profitmargin.setObjectName(u"label_checklist_profitmargin")
        self.label_checklist_profitmargin.setGeometry(QRect(280, 310, 41, 21))
        self.label_checklist_profitmargin.setFont(font5)
        self.label_checklist_profitmargin.setAutoFillBackground(False)
        self.label_checklist_profitmargin.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_profitmargin.setAlignment(Qt.AlignCenter)
        self.label_checklist_shares = QLabel(self.frame_checklist_2)
        self.label_checklist_shares.setObjectName(u"label_checklist_shares")
        self.label_checklist_shares.setGeometry(QRect(230, 340, 91, 21))
        self.label_checklist_shares.setFont(font5)
        self.label_checklist_shares.setAutoFillBackground(False)
        self.label_checklist_shares.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_shares.setAlignment(Qt.AlignCenter)
        self.frame_checklist_3 = QFrame(self.frame_checklist_2)
        self.frame_checklist_3.setObjectName(u"frame_checklist_3")
        self.frame_checklist_3.setGeometry(QRect(230, 400, 91, 81))
        self.frame_checklist_3.setFont(font3)
        self.frame_checklist_3.setStyleSheet(u"background-color: #89C2D9; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_checklist_3.setFrameShape(QFrame.StyledPanel)
        self.frame_checklist_3.setFrameShadow(QFrame.Raised)
        self.label_checklist_passes = QLabel(self.frame_checklist_3)
        self.label_checklist_passes.setObjectName(u"label_checklist_passes")
        self.label_checklist_passes.setGeometry(QRect(10, 40, 31, 31))
        self.label_checklist_passes.setFont(font5)
        self.label_checklist_passes.setAutoFillBackground(False)
        self.label_checklist_passes.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_passes.setAlignment(Qt.AlignCenter)
        self.label_checklist_fails = QLabel(self.frame_checklist_3)
        self.label_checklist_fails.setObjectName(u"label_checklist_fails")
        self.label_checklist_fails.setGeometry(QRect(50, 40, 31, 31))
        self.label_checklist_fails.setFont(font5)
        self.label_checklist_fails.setAutoFillBackground(False)
        self.label_checklist_fails.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_fails.setAlignment(Qt.AlignCenter)
        self.label_checklist_25 = QLabel(self.frame_checklist_3)
        self.label_checklist_25.setObjectName(u"label_checklist_25")
        self.label_checklist_25.setGeometry(QRect(0, 0, 91, 31))
        self.label_checklist_25.setFont(font5)
        self.label_checklist_25.setAutoFillBackground(False)
        self.label_checklist_25.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #468FAF;\n"
"}")
        self.label_checklist_25.setAlignment(Qt.AlignCenter)
        self.label_checklist_9 = QLabel(self.frame_checklist_2)
        self.label_checklist_9.setObjectName(u"label_checklist_9")
        self.label_checklist_9.setGeometry(QRect(230, 370, 91, 20))
        self.label_checklist_9.setFont(font2)
        self.label_checklist_9.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_9.setAlignment(Qt.AlignCenter)
        self.label_checklist_pe = QLabel(self.frame_checklist_2)
        self.label_checklist_pe.setObjectName(u"label_checklist_pe")
        self.label_checklist_pe.setGeometry(QRect(280, 250, 41, 21))
        self.label_checklist_pe.setFont(font5)
        self.label_checklist_pe.setAutoFillBackground(False)
        self.label_checklist_pe.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_pe.setAlignment(Qt.AlignCenter)
        self.label_checklist_39 = QLabel(self.page_checklist)
        self.label_checklist_39.setObjectName(u"label_checklist_39")
        self.label_checklist_39.setGeometry(QRect(350, 10, 151, 21))
        self.label_checklist_39.setFont(font2)
        self.label_checklist_39.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_39.setAlignment(Qt.AlignCenter)
        self.frame_checklist_chartbackground = QFrame(self.page_checklist)
        self.frame_checklist_chartbackground.setObjectName(u"frame_checklist_chartbackground")
        self.frame_checklist_chartbackground.setGeometry(QRect(350, 40, 841, 351))
        self.frame_checklist_chartbackground.setFont(font3)
        self.frame_checklist_chartbackground.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_checklist_chartbackground.setFrameShape(QFrame.StyledPanel)
        self.frame_checklist_chartbackground.setFrameShadow(QFrame.Raised)
        self.frame_checklist_chart = QFrame(self.frame_checklist_chartbackground)
        self.frame_checklist_chart.setObjectName(u"frame_checklist_chart")
        self.frame_checklist_chart.setGeometry(QRect(10, 10, 821, 331))
        self.frame_checklist_chart.setStyleSheet(u"border: none")
        self.frame_checklist_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_checklist_chart.setFrameShadow(QFrame.Raised)
        self.tableWidget_checklist_prices = QTableWidget(self.page_checklist)
        if (self.tableWidget_checklist_prices.columnCount() < 4):
            self.tableWidget_checklist_prices.setColumnCount(4)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setHorizontalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setHorizontalHeaderItem(1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setHorizontalHeaderItem(2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setHorizontalHeaderItem(3, __qtablewidgetitem59)
        if (self.tableWidget_checklist_prices.rowCount() < 7):
            self.tableWidget_checklist_prices.setRowCount(7)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(5, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_checklist_prices.setVerticalHeaderItem(6, __qtablewidgetitem66)
        self.tableWidget_checklist_prices.setObjectName(u"tableWidget_checklist_prices")
        self.tableWidget_checklist_prices.setGeometry(QRect(350, 430, 481, 281))
        self.tableWidget_checklist_prices.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #468FAF;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #89C2D9;\n"
"}\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #61a5c2;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #468FAF;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::sub-line:vert"
                        "ical:pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #61a5c2;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #89C2D9f;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: #61a5c2;\n"
"    height: 14px;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:horizontal  {	\n"
"	background-color: #468FAF;\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"Q"
                        "ScrollBar::handle:horizontal :hover{	\n"
"	background-color: #89C2D9;\n"
"}\n"
"QScrollBar::handle:horizontal :pressed {	\n"
"	background-color: #89C2D9;\n"
"}\n"
"")
        self.label_checklist_40 = QLabel(self.page_checklist)
        self.label_checklist_40.setObjectName(u"label_checklist_40")
        self.label_checklist_40.setGeometry(QRect(350, 400, 151, 21))
        self.label_checklist_40.setFont(font2)
        self.label_checklist_40.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_40.setAlignment(Qt.AlignCenter)
        self.label_checklist_41 = QLabel(self.page_checklist)
        self.label_checklist_41.setObjectName(u"label_checklist_41")
        self.label_checklist_41.setGeometry(QRect(10, 510, 331, 21))
        self.label_checklist_41.setFont(font2)
        self.label_checklist_41.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_41.setAlignment(Qt.AlignCenter)
        self.label_checklist_32 = QLabel(self.page_checklist)
        self.label_checklist_32.setObjectName(u"label_checklist_32")
        self.label_checklist_32.setGeometry(QRect(10, 540, 161, 21))
        self.label_checklist_32.setFont(font5)
        self.label_checklist_32.setAutoFillBackground(False)
        self.label_checklist_32.setStyleSheet(u"QLabel {\n"
"background-color: #577590;\n"
"border-radius:5px;\n"
"border: 2px solid #384C5D;\n"
"}")
        self.label_checklist_32.setAlignment(Qt.AlignCenter)
        self.label_checklist_31 = QLabel(self.page_checklist)
        self.label_checklist_31.setObjectName(u"label_checklist_31")
        self.label_checklist_31.setGeometry(QRect(10, 570, 161, 21))
        self.label_checklist_31.setFont(font5)
        self.label_checklist_31.setAutoFillBackground(False)
        self.label_checklist_31.setStyleSheet(u"QLabel {\n"
"background-color: #5b8e7d;\n"
"border-radius:5px;\n"
"border: 2px solid #355148;\n"
"}")
        self.label_checklist_31.setAlignment(Qt.AlignCenter)
        self.label_checklist_30 = QLabel(self.page_checklist)
        self.label_checklist_30.setObjectName(u"label_checklist_30")
        self.label_checklist_30.setGeometry(QRect(10, 600, 161, 21))
        self.label_checklist_30.setFont(font5)
        self.label_checklist_30.setAutoFillBackground(False)
        self.label_checklist_30.setStyleSheet(u"QLabel {\n"
"background-color: #8cb369;\n"
"border-radius:5px;\n"
"border: 2px solid #4F6B37;\n"
"}")
        self.label_checklist_30.setAlignment(Qt.AlignCenter)
        self.label_checklist_29 = QLabel(self.page_checklist)
        self.label_checklist_29.setObjectName(u"label_checklist_29")
        self.label_checklist_29.setGeometry(QRect(10, 630, 161, 21))
        self.label_checklist_29.setFont(font5)
        self.label_checklist_29.setAutoFillBackground(False)
        self.label_checklist_29.setStyleSheet(u"QLabel {\n"
"background-color: #f4e285;\n"
"border-radius:5px;\n"
"border: 2px solid #C2A516;\n"
"}")
        self.label_checklist_29.setAlignment(Qt.AlignCenter)
        self.label_checklist_28 = QLabel(self.page_checklist)
        self.label_checklist_28.setObjectName(u"label_checklist_28")
        self.label_checklist_28.setGeometry(QRect(10, 660, 161, 21))
        self.label_checklist_28.setFont(font5)
        self.label_checklist_28.setAutoFillBackground(False)
        self.label_checklist_28.setStyleSheet(u"QLabel {\n"
"background-color: #f4a259;\n"
"border-radius:5px;\n"
"border: 2px solid #AD590F;\n"
"}")
        self.label_checklist_28.setAlignment(Qt.AlignCenter)
        self.label_checklist_26 = QLabel(self.page_checklist)
        self.label_checklist_26.setObjectName(u"label_checklist_26")
        self.label_checklist_26.setGeometry(QRect(10, 690, 161, 21))
        self.label_checklist_26.setFont(font5)
        self.label_checklist_26.setAutoFillBackground(False)
        self.label_checklist_26.setStyleSheet(u"QLabel {\n"
"background-color: #bc4b51;\n"
"border-radius:5px;\n"
"border: 2px solid #6D2A2E;\n"
"}")
        self.label_checklist_26.setAlignment(Qt.AlignCenter)
        self.label_checklist_27 = QLabel(self.page_checklist)
        self.label_checklist_27.setObjectName(u"label_checklist_27")
        self.label_checklist_27.setGeometry(QRect(180, 630, 161, 21))
        self.label_checklist_27.setFont(font5)
        self.label_checklist_27.setAutoFillBackground(False)
        self.label_checklist_27.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_27.setAlignment(Qt.AlignCenter)
        self.label_checklist_38 = QLabel(self.page_checklist)
        self.label_checklist_38.setObjectName(u"label_checklist_38")
        self.label_checklist_38.setGeometry(QRect(180, 540, 161, 21))
        self.label_checklist_38.setFont(font5)
        self.label_checklist_38.setAutoFillBackground(False)
        self.label_checklist_38.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_38.setAlignment(Qt.AlignCenter)
        self.label_checklist_37 = QLabel(self.page_checklist)
        self.label_checklist_37.setObjectName(u"label_checklist_37")
        self.label_checklist_37.setGeometry(QRect(180, 600, 161, 21))
        self.label_checklist_37.setFont(font5)
        self.label_checklist_37.setAutoFillBackground(False)
        self.label_checklist_37.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_37.setAlignment(Qt.AlignCenter)
        self.label_checklist_36 = QLabel(self.page_checklist)
        self.label_checklist_36.setObjectName(u"label_checklist_36")
        self.label_checklist_36.setGeometry(QRect(180, 660, 161, 21))
        self.label_checklist_36.setFont(font5)
        self.label_checklist_36.setAutoFillBackground(False)
        self.label_checklist_36.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_36.setAlignment(Qt.AlignCenter)
        self.label_checklist_35 = QLabel(self.page_checklist)
        self.label_checklist_35.setObjectName(u"label_checklist_35")
        self.label_checklist_35.setGeometry(QRect(180, 570, 161, 21))
        self.label_checklist_35.setFont(font5)
        self.label_checklist_35.setAutoFillBackground(False)
        self.label_checklist_35.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_35.setAlignment(Qt.AlignCenter)
        self.label_checklist_34 = QLabel(self.page_checklist)
        self.label_checklist_34.setObjectName(u"label_checklist_34")
        self.label_checklist_34.setGeometry(QRect(180, 690, 161, 21))
        self.label_checklist_34.setFont(font5)
        self.label_checklist_34.setAutoFillBackground(False)
        self.label_checklist_34.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_34.setAlignment(Qt.AlignCenter)
        self.spinBox_checklist_marginofsaftey = QSpinBox(self.page_checklist)
        self.spinBox_checklist_marginofsaftey.setObjectName(u"spinBox_checklist_marginofsaftey")
        self.spinBox_checklist_marginofsaftey.setGeometry(QRect(650, 400, 41, 21))
        self.spinBox_checklist_marginofsaftey.setFont(font3)
        self.spinBox_checklist_marginofsaftey.setStyleSheet(u"QSpinBox {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QSpinBox:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.spinBox_checklist_marginofsaftey.setMinimum(0)
        self.spinBox_checklist_marginofsaftey.setMaximum(99)
        self.spinBox_checklist_marginofsaftey.setValue(15)
        self.label_checklist_33 = QLabel(self.page_checklist)
        self.label_checklist_33.setObjectName(u"label_checklist_33")
        self.label_checklist_33.setGeometry(QRect(510, 400, 131, 21))
        self.label_checklist_33.setFont(font5)
        self.label_checklist_33.setAutoFillBackground(False)
        self.label_checklist_33.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_33.setAlignment(Qt.AlignCenter)
        self.frame_checklist = QFrame(self.page_checklist)
        self.frame_checklist.setObjectName(u"frame_checklist")
        self.frame_checklist.setGeometry(QRect(840, 400, 351, 311))
        self.frame_checklist.setFont(font3)
        self.frame_checklist.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_checklist.setFrameShape(QFrame.StyledPanel)
        self.frame_checklist.setFrameShadow(QFrame.Raised)
        self.label_checklist_4 = QLabel(self.frame_checklist)
        self.label_checklist_4.setObjectName(u"label_checklist_4")
        self.label_checklist_4.setGeometry(QRect(10, 40, 101, 21))
        self.label_checklist_4.setFont(font5)
        self.label_checklist_4.setAutoFillBackground(False)
        self.label_checklist_4.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_4.setAlignment(Qt.AlignCenter)
        self.label_checklist_currentprice = QLabel(self.frame_checklist)
        self.label_checklist_currentprice.setObjectName(u"label_checklist_currentprice")
        self.label_checklist_currentprice.setGeometry(QRect(120, 40, 71, 21))
        self.label_checklist_currentprice.setFont(font5)
        self.label_checklist_currentprice.setAutoFillBackground(False)
        self.label_checklist_currentprice.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_currentprice.setAlignment(Qt.AlignCenter)
        self.label_checklist_6 = QLabel(self.frame_checklist)
        self.label_checklist_6.setObjectName(u"label_checklist_6")
        self.label_checklist_6.setGeometry(QRect(0, 0, 351, 31))
        self.label_checklist_6.setFont(font2)
        self.label_checklist_6.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_6.setAlignment(Qt.AlignCenter)
        self.label_checklist = QLabel(self.frame_checklist)
        self.label_checklist.setObjectName(u"label_checklist")
        self.label_checklist.setGeometry(QRect(10, 70, 101, 21))
        self.label_checklist.setFont(font5)
        self.label_checklist.setAutoFillBackground(False)
        self.label_checklist.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist.setAlignment(Qt.AlignCenter)
        self.label_checklist_currentvalue = QLabel(self.frame_checklist)
        self.label_checklist_currentvalue.setObjectName(u"label_checklist_currentvalue")
        self.label_checklist_currentvalue.setGeometry(QRect(120, 70, 71, 21))
        self.label_checklist_currentvalue.setFont(font5)
        self.label_checklist_currentvalue.setAutoFillBackground(False)
        self.label_checklist_currentvalue.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_currentvalue.setAlignment(Qt.AlignCenter)
        self.label_checklist_2 = QLabel(self.frame_checklist)
        self.label_checklist_2.setObjectName(u"label_checklist_2")
        self.label_checklist_2.setGeometry(QRect(200, 70, 71, 21))
        self.label_checklist_2.setFont(font5)
        self.label_checklist_2.setAutoFillBackground(False)
        self.label_checklist_2.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_2.setAlignment(Qt.AlignCenter)
        self.label_checklist_3 = QLabel(self.frame_checklist)
        self.label_checklist_3.setObjectName(u"label_checklist_3")
        self.label_checklist_3.setGeometry(QRect(10, 140, 101, 21))
        self.label_checklist_3.setFont(font5)
        self.label_checklist_3.setAutoFillBackground(False)
        self.label_checklist_3.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_3.setAlignment(Qt.AlignCenter)
        self.label_checklist_rating = QLabel(self.frame_checklist)
        self.label_checklist_rating.setObjectName(u"label_checklist_rating")
        self.label_checklist_rating.setGeometry(QRect(120, 140, 221, 21))
        self.label_checklist_rating.setFont(font5)
        self.label_checklist_rating.setAutoFillBackground(False)
        self.label_checklist_rating.setStyleSheet(u"QLabel {\n"
"background-color: #8cb369;\n"
"border-radius:5px;\n"
"border: 2px solid #4F6B37;\n"
"}")
        self.label_checklist_rating.setAlignment(Qt.AlignCenter)
        self.label_checklist_points = QLabel(self.frame_checklist)
        self.label_checklist_points.setObjectName(u"label_checklist_points")
        self.label_checklist_points.setGeometry(QRect(280, 70, 61, 21))
        self.label_checklist_points.setFont(font5)
        self.label_checklist_points.setAutoFillBackground(False)
        self.label_checklist_points.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_points.setAlignment(Qt.AlignCenter)
        self.label_checklist_5 = QLabel(self.frame_checklist)
        self.label_checklist_5.setObjectName(u"label_checklist_5")
        self.label_checklist_5.setGeometry(QRect(0, 100, 351, 31))
        self.label_checklist_5.setFont(font2)
        self.label_checklist_5.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_checklist_5.setAlignment(Qt.AlignCenter)
        self.label_checklist_discount = QLabel(self.frame_checklist)
        self.label_checklist_discount.setObjectName(u"label_checklist_discount")
        self.label_checklist_discount.setGeometry(QRect(280, 40, 61, 21))
        self.label_checklist_discount.setFont(font5)
        self.label_checklist_discount.setAutoFillBackground(False)
        self.label_checklist_discount.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_discount.setAlignment(Qt.AlignCenter)
        self.label_checklist_7 = QLabel(self.frame_checklist)
        self.label_checklist_7.setObjectName(u"label_checklist_7")
        self.label_checklist_7.setGeometry(QRect(200, 40, 71, 21))
        self.label_checklist_7.setFont(font5)
        self.label_checklist_7.setAutoFillBackground(False)
        self.label_checklist_7.setStyleSheet(u"QLabel {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_7.setAlignment(Qt.AlignCenter)
        self.label_checklist_company_data = QLabel(self.page_checklist)
        self.label_checklist_company_data.setObjectName(u"label_checklist_company_data")
        self.label_checklist_company_data.setGeometry(QRect(510, 10, 671, 21))
        self.label_checklist_company_data.setFont(font4)
        self.label_checklist_company_data.setAutoFillBackground(False)
        self.label_checklist_company_data.setStyleSheet(u"QLabel {\n"
"background-color: #89C2D9;\n"
"border-radius:5px;\n"
"border: 2px solid #A9D6E5;\n"
"}\n"
"QLabel:hover\n"
" {\n"
"background-color: #A9D6E5;\n"
"border-radius:5px;\n"
"border: 2px solid #61A5C2;\n"
"}")
        self.label_checklist_company_data.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_checklist)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.stackedWidget.addWidget(self.widget)
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 10, 371, 51))
        font8 = QFont()
        font8.setFamily(u"Bahnschrift SemiLight")
        font8.setPointSize(16)
        font8.setBold(True)
        self.label_title.setFont(font8)
        self.label_title.setStyleSheet(u"background-color: #89c2d9; \n"
"border-radius: 10px; \n"
"border: 3px solid #61A5C2")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_downloadstockdata = QLabel(self.centralwidget)
        self.label_downloadstockdata.setObjectName(u"label_downloadstockdata")
        self.label_downloadstockdata.setGeometry(QRect(1010, 10, 201, 21))
        font9 = QFont()
        font9.setFamily(u"Bahnschrift SemiLight")
        font9.setPointSize(10)
        font9.setBold(True)
        self.label_downloadstockdata.setFont(font9)
        self.label_downloadstockdata.setStyleSheet(u"background-color: #89c2d9;\n"
"border-radius: 10px;\n"
"border: 2px solid #61A5C2;")
        self.label_downloadstockdata.setAlignment(Qt.AlignCenter)
        self.pushButton_loadstockdata = QPushButton(self.centralwidget)
        self.pushButton_loadstockdata.setObjectName(u"pushButton_loadstockdata")
        self.pushButton_loadstockdata.setGeometry(QRect(1150, 40, 61, 21))
        self.pushButton_loadstockdata.setFont(font)
        self.pushButton_loadstockdata.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #89c2d9;\n"
"	border-radius: 5px; \n"
"	border:2px solid #61a5c2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#468FAF;\n"
"   border:2px solid #2C7DA0;\n"
"}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1010, 40, 131, 21))
        font10 = QFont()
        font10.setFamily(u"Bahnschrift SemiLight")
        font10.setPointSize(8)
        self.lineEdit.setFont(font10)
        self.lineEdit.setStyleSheet(u"background-color: #89c2d9;\n"
"border-radius: 5px; \n"
"border:2px solid #61a5c2;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.frame_pageselectors = QFrame(self.centralwidget)
        self.frame_pageselectors.setObjectName(u"frame_pageselectors")
        self.frame_pageselectors.setGeometry(QRect(390, 10, 611, 51))
        self.frame_pageselectors.setFont(font)
        self.frame_pageselectors.setStyleSheet(u"background-color: #89c2d9;\n"
"border-radius:10px;")
        self.frame_pageselectors.setFrameShape(QFrame.StyledPanel)
        self.frame_pageselectors.setFrameShadow(QFrame.Raised)
        self.pushButton_dataview = QPushButton(self.frame_pageselectors)
        self.pushButton_dataview.setObjectName(u"pushButton_dataview")
        self.pushButton_dataview.setGeometry(QRect(250, 10, 111, 31))
        self.pushButton_dataview.setFont(font2)
        self.pushButton_dataview.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #61A5C2;\n"
"	border-radius: 5px; \n"
"	border:2px solid #2C7DA0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#2C7DA0;\n"
"   border:2px solid #2A6F97;\n"
"}")
        self.pushButton_overview = QPushButton(self.frame_pageselectors)
        self.pushButton_overview.setObjectName(u"pushButton_overview")
        self.pushButton_overview.setGeometry(QRect(10, 10, 111, 31))
        self.pushButton_overview.setFont(font2)
        self.pushButton_overview.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #61A5C2;\n"
"	border-radius: 5px; \n"
"	border:2px solid #2C7DA0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#2C7DA0;\n"
"   border:2px solid #2A6F97;\n"
"}")
        self.pushButton_chartview = QPushButton(self.frame_pageselectors)
        self.pushButton_chartview.setObjectName(u"pushButton_chartview")
        self.pushButton_chartview.setGeometry(QRect(130, 10, 111, 31))
        self.pushButton_chartview.setFont(font2)
        self.pushButton_chartview.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #61A5C2;\n"
"	border-radius: 5px; \n"
"	border:2px solid #2C7DA0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#2C7DA0;\n"
"   border:2px solid #2A6F97;\n"
"}")
        self.pushButton_forecast = QPushButton(self.frame_pageselectors)
        self.pushButton_forecast.setObjectName(u"pushButton_forecast")
        self.pushButton_forecast.setGeometry(QRect(370, 10, 111, 31))
        self.pushButton_forecast.setFont(font2)
        self.pushButton_forecast.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #61A5C2;\n"
"	border-radius: 5px; \n"
"	border:2px solid #2C7DA0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#2C7DA0;\n"
"   border:2px solid #2A6F97;\n"
"}")
        self.pushButton_checklist = QPushButton(self.frame_pageselectors)
        self.pushButton_checklist.setObjectName(u"pushButton_checklist")
        self.pushButton_checklist.setGeometry(QRect(490, 10, 111, 31))
        self.pushButton_checklist.setFont(font2)
        self.pushButton_checklist.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: #61A5C2;\n"
"	border-radius: 5px; \n"
"	border:2px solid #2C7DA0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color:#2C7DA0;\n"
"   border:2px solid #2A6F97;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_chartview.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stock Analizer Tool", None))

        __sortingEnabled = self.listWidget_companylist.isSortingEnabled()
        self.listWidget_companylist.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_companylist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"INTC", None));
        self.listWidget_companylist.setSortingEnabled(__sortingEnabled)

        self.label_companylistsubheader.setText(QCoreApplication.translate("MainWindow", u"Click company to view", None))
        self.label_companylistheader.setText(QCoreApplication.translate("MainWindow", u"Companies", None))
        self.label_metrics.setText(QCoreApplication.translate("MainWindow", u"Metrics / Stock Data", None))
        self.label_lastprice.setText(QCoreApplication.translate("MainWindow", u"Last Price", None))
        self.label_lastprice_data.setText(QCoreApplication.translate("MainWindow", u"$52.97", None))
        self.label_52weekhigh_data.setText(QCoreApplication.translate("MainWindow", u"$68.49", None))
        self.label_52weekhigh.setText(QCoreApplication.translate("MainWindow", u"52 Week High", None))
        self.label_52weeklow_data.setText(QCoreApplication.translate("MainWindow", u"$43.61", None))
        self.label_52weeklow.setText(QCoreApplication.translate("MainWindow", u"52 Week Low", None))
        self.label_5yearavgyield_data.setText(QCoreApplication.translate("MainWindow", u"%2.5", None))
        self.label_sharesoutstanding_data.setText(QCoreApplication.translate("MainWindow", u"4,038,000,128", None))
        self.label_currentyield_data.setText(QCoreApplication.translate("MainWindow", u"%2.47", None))
        self.label_sharediv_data.setText(QCoreApplication.translate("MainWindow", u"$1.392", None))
        self.label_beta_data.setText(QCoreApplication.translate("MainWindow", u"0.603917", None))
        self.label_50dayma_data.setText(QCoreApplication.translate("MainWindow", u"$56.42", None))
        self.label_enterprisevalue_data.setText(QCoreApplication.translate("MainWindow", u"240,543,744,000", None))
        self.label_200dayma_data.setText(QCoreApplication.translate("MainWindow", u"$58.79", None))
        self.label_200dayma.setText(QCoreApplication.translate("MainWindow", u"200 Day MA", None))
        self.label_50dayma.setText(QCoreApplication.translate("MainWindow", u"50 Day MA", None))
        self.label_5yearavgyield.setText(QCoreApplication.translate("MainWindow", u"5Yr Avg Yield", None))
        self.label_currentyield.setText(QCoreApplication.translate("MainWindow", u"Current Yield", None))
        self.label_sharediv.setText(QCoreApplication.translate("MainWindow", u"Share. Div", None))
        self.label_beta.setText(QCoreApplication.translate("MainWindow", u"Beta", None))
        self.label_enterprisevalue.setText(QCoreApplication.translate("MainWindow", u"Enterprise Value (EV)", None))
        self.label_sharesoutstanding.setText(QCoreApplication.translate("MainWindow", u"Shares Outstanding", None))
        self.label_targetmed_data.setText(QCoreApplication.translate("MainWindow", u"$67", None))
        self.label_targetmed.setText(QCoreApplication.translate("MainWindow", u"Target Med", None))
        self.label_targethigh.setText(QCoreApplication.translate("MainWindow", u"Target High", None))
        self.label_targetmean.setText(QCoreApplication.translate("MainWindow", u"Target Mean", None))
        self.label_targetmean_data.setText(QCoreApplication.translate("MainWindow", u"$64.58", None))
        self.label_targethigh_data.setText(QCoreApplication.translate("MainWindow", u"$85", None))
        self.label_targetlow_data.setText(QCoreApplication.translate("MainWindow", u"$40", None))
        self.label_targetlow.setText(QCoreApplication.translate("MainWindow", u"Target Low", None))
        self.label_bookvalue.setText(QCoreApplication.translate("MainWindow", u"Book Value", None))
        self.label_bookvalue_data.setText(QCoreApplication.translate("MainWindow", u"19.764", None))
        self.label_pricebook_data.setText(QCoreApplication.translate("MainWindow", u"2.6816435", None))
        self.label_pricebook.setText(QCoreApplication.translate("MainWindow", u"Price / Book", None))
        self.label_avgvolume_data.setText(QCoreApplication.translate("MainWindow", u"24,783,431", None))
        self.label_rps.setText(QCoreApplication.translate("MainWindow", u"RPS", None))
        self.label_evebitda.setText(QCoreApplication.translate("MainWindow", u"EV/EBITDA", None))
        self.label_evebitda_data.setText(QCoreApplication.translate("MainWindow", u"6.938", None))
        self.label_evr_data.setText(QCoreApplication.translate("MainWindow", u"3.095", None))
        self.label_evr.setText(QCoreApplication.translate("MainWindow", u"EV/R", None))
        self.label_rps_data.setText(QCoreApplication.translate("MainWindow", u"$18.742", None))
        self.label_avgvolume.setText(QCoreApplication.translate("MainWindow", u"Avg Volume", None))
        self.label_marketcap_data.setText(QCoreApplication.translate("MainWindow", u"$214,014,001,152", None))
        self.label_sector.setText(QCoreApplication.translate("MainWindow", u"Sector", None))
        self.label_industry.setText(QCoreApplication.translate("MainWindow", u"Industry", None))
        self.label_company_data.setText(QCoreApplication.translate("MainWindow", u"Intel Corporation", None))
        self.label_companylistheader_3.setText(QCoreApplication.translate("MainWindow", u"Last Update: 07-24-2021", None))
        self.label_industry_data.setText(QCoreApplication.translate("MainWindow", u"Semiconductors", None))
        self.textBrowser_description_data.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Intel Corporation designs, manufactures, and sells essential technologies for the cloud, smart, and connected devices for retail, industrial, and consumer uses worldwide. The company operates through DCG, IOTG, Mobileye, NSG, PSG, CCG, and All Other segments. It offers platform products, such as central processing units and chipsets, and system-on-chip and multichip packages; and non-platform or adjacent products comprising accelerators, boards and systems, connectivity products, and memory and storage products. The company also provides"
                        " Internet of Things products, including high-performance compute solutions for targeted verticals and embedded applications; and computer vision and machine learning-based sensing, data analysis, localization, mapping, and driving policy technology. It serves original equipment manufacturers, original design manufacturers, and cloud service providers. Intel Corporation has a strategic partnership with MILA to develop and apply advances in artificial intelligence methods for enhancing the search in the space of drugs. The company was founded in 1968 and is headquartered in Santa Clara, California.</p></body></html>", None))
        self.label_marketcap.setText(QCoreApplication.translate("MainWindow", u"Market Cap", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Buisness Summery / Company Description", None))
        self.label_company.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_sector_data.setText(QCoreApplication.translate("MainWindow", u"Technology", None))
        self.label_companylistheader_2.setText(QCoreApplication.translate("MainWindow", u"Company Overview", None))
        self.label_chartview_quad_apply1.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.comboBox_chartview_chartviewselector_2.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_chartviewselector_2.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_chartviewselector_2.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_2.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_2.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.comboBox_chartview_chartviewselector_3.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_chartviewselector_3.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_chartviewselector_3.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_3.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_3.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.label_chartview_quad_apply2.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.label_chartview_quad_apply4.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.comboBox_chartview_chartviewselector_4.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_chartviewselector_4.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_chartviewselector_4.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_4.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_4.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.label_chartview_quad_apply3.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.comboBox_chartview_chartviewselector_5.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_chartviewselector_5.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_chartviewselector_5.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_5.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_chartviewselector_5.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.label_chartview_quad_chart1.setText(QCoreApplication.translate("MainWindow", u"Chart 1", None))
        self.label_chartview_quad_chart2.setText(QCoreApplication.translate("MainWindow", u"Chart 2", None))
        self.label_chartview_quad_chart3.setText(QCoreApplication.translate("MainWindow", u"Chart 3", None))
        self.label_chartview_quad_chart4.setText(QCoreApplication.translate("MainWindow", u"Chart 4", None))
        self.label_chartview_split_chart2.setText(QCoreApplication.translate("MainWindow", u"Chart 2", None))
        self.comboBox_chartview_splitchartviewselector1.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_splitchartviewselector1.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_splitchartviewselector1.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_splitchartviewselector1.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_splitchartviewselector1.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.pushButton_chartview_split_apply2.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.comboBox_chartview_splitchartviewselector2.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_splitchartviewselector2.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_splitchartviewselector2.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_splitchartviewselector2.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_splitchartviewselector2.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.pushButton_chartview_split_apply1.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.label_chartview_split_chart1.setText(QCoreApplication.translate("MainWindow", u"Chart 1", None))
        self.label_chartview_split_datainview1.setText(QCoreApplication.translate("MainWindow", u"Data Currently in View", None))

        __sortingEnabled1 = self.listWidget_chartview_split_selection1.isSortingEnabled()
        self.listWidget_chartview_split_selection1.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_chartview_split_selection1.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"OPERATING_REVENUE", None));
        self.listWidget_chartview_split_selection1.setSortingEnabled(__sortingEnabled1)

        self.label_chartview_split_currentlyviewing1.setText(QCoreApplication.translate("MainWindow", u"Currently Viewing", None))
        self.label_chartview_split_datainview2.setText(QCoreApplication.translate("MainWindow", u"Data Currently in View", None))
        self.label_chartview_split_currentlyviewing2.setText(QCoreApplication.translate("MainWindow", u"Currently Viewing", None))
        self.pushButton_chartview_single_apply1.setText(QCoreApplication.translate("MainWindow", u"Apply Selection", None))
        self.label_chartview_single_chart1.setText(QCoreApplication.translate("MainWindow", u"Chart 1", None))
        self.comboBox_chartview_single_chartselector1.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_chartview_single_chartselector1.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_chartview_single_chartselector1.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_chartview_single_chartselector1.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_chartview_single_chartselector1.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.label_chartview_companyname.setText(QCoreApplication.translate("MainWindow", u"Intel Corperation", None))
        self.comboBox_chartview_chartviewselector.setItemText(0, QCoreApplication.translate("MainWindow", u"SPLIT VIEW", None))
        self.comboBox_chartview_chartviewselector.setItemText(1, QCoreApplication.translate("MainWindow", u"SINGLE VIEW", None))
        self.comboBox_chartview_chartviewselector.setItemText(2, QCoreApplication.translate("MainWindow", u"QUAD VIEW", None))

        self.label_chartview_datatypes.setText(QCoreApplication.translate("MainWindow", u"Data Types", None))

        __sortingEnabled2 = self.listWidget_chartview_datatypeslist.isSortingEnabled()
        self.listWidget_chartview_datatypeslist.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_chartview_datatypeslist.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"OPERATING_REVENUE", None));
        ___qlistwidgetitem3 = self.listWidget_chartview_datatypeslist.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"COST_OF_GOODS_SOLD", None));
        ___qlistwidgetitem4 = self.listWidget_chartview_datatypeslist.item(2)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"GROSS_PROFIT", None));
        ___qlistwidgetitem5 = self.listWidget_chartview_datatypeslist.item(3)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SG_AND_A_EXPENSE", None));
        ___qlistwidgetitem6 = self.listWidget_chartview_datatypeslist.item(4)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"RESEARCH_AND_DEVELOPMENT_EXPENSE", None));
        ___qlistwidgetitem7 = self.listWidget_chartview_datatypeslist.item(5)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"SPECIAL_INCOME_AND_CHARGES", None));
        ___qlistwidgetitem8 = self.listWidget_chartview_datatypeslist.item(6)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"OPERATING_INTEREST_EXPENSE", None));
        ___qlistwidgetitem9 = self.listWidget_chartview_datatypeslist.item(7)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"NET_OPERATING_INTEREST_INCOME", None));
        ___qlistwidgetitem10 = self.listWidget_chartview_datatypeslist.item(8)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TOTAL_OPERATING_EXPENSES", None));
        ___qlistwidgetitem11 = self.listWidget_chartview_datatypeslist.item(9)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"OPERATING_INCOME", None));
        ___qlistwidgetitem12 = self.listWidget_chartview_datatypeslist.item(10)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"OTHER_INCOME_AND_EXPENSES", None));
        ___qlistwidgetitem13 = self.listWidget_chartview_datatypeslist.item(11)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"PRE_TAX_INCOME", None));
        ___qlistwidgetitem14 = self.listWidget_chartview_datatypeslist.item(12)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"PROVISION_FOR_INCOME_TAXES", None));
        ___qlistwidgetitem15 = self.listWidget_chartview_datatypeslist.item(13)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"INCOME_FROM_CONTINUING_OPERATIONS", None));
        ___qlistwidgetitem16 = self.listWidget_chartview_datatypeslist.item(14)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NORMALIZED_INCOME", None));
        ___qlistwidgetitem17 = self.listWidget_chartview_datatypeslist.item(15)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"EBITDA", None));
        ___qlistwidgetitem18 = self.listWidget_chartview_datatypeslist.item(16)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"RECONCILED_DEPRECIATION", None));
        ___qlistwidgetitem19 = self.listWidget_chartview_datatypeslist.item(17)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"EBIT", None));
        ___qlistwidgetitem20 = self.listWidget_chartview_datatypeslist.item(18)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"EPS_BASIC_FROM_CONTINUING_OPERATIONS", None));
        ___qlistwidgetitem21 = self.listWidget_chartview_datatypeslist.item(19)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"NORMALIZED_BASIC_EPS", None));
        ___qlistwidgetitem22 = self.listWidget_chartview_datatypeslist.item(20)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"EPS_DILUTED_FROM_CONTINUING_OPERATIONS", None));
        ___qlistwidgetitem23 = self.listWidget_chartview_datatypeslist.item(21)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"NORMALIZED_DILUTED_EPS", None));
        ___qlistwidgetitem24 = self.listWidget_chartview_datatypeslist.item(22)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"AVERAGE_BASIC_SHARES_OUTSTANDING", None));
        ___qlistwidgetitem25 = self.listWidget_chartview_datatypeslist.item(23)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"AVERAGE_DILUTED_SHARES_OUTSTANDING", None));
        ___qlistwidgetitem26 = self.listWidget_chartview_datatypeslist.item(24)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"DIVIDEND_PER_SHARE", None));
        ___qlistwidgetitem27 = self.listWidget_chartview_datatypeslist.item(25)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"OTHER_OPERATING_EXPENSES", None));
        ___qlistwidgetitem28 = self.listWidget_chartview_datatypeslist.item(26)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"CASH_AND_EQUIVALENTS", None));
        ___qlistwidgetitem29 = self.listWidget_chartview_datatypeslist.item(27)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"SHORT_TERM_INVESTMENTS", None));
        ___qlistwidgetitem30 = self.listWidget_chartview_datatypeslist.item(28)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"CASH_AND_SHORT_TERM_INVESTMENTS", None));
        ___qlistwidgetitem31 = self.listWidget_chartview_datatypeslist.item(29)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ACCOUNTS_RECEIVABLES", None));
        ___qlistwidgetitem32 = self.listWidget_chartview_datatypeslist.item(30)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"TOTAL_RECEIVABLES", None));
        ___qlistwidgetitem33 = self.listWidget_chartview_datatypeslist.item(31)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"RAW_MATERIALS", None));
        ___qlistwidgetitem34 = self.listWidget_chartview_datatypeslist.item(32)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"WORK_IN_PROCESS", None));
        ___qlistwidgetitem35 = self.listWidget_chartview_datatypeslist.item(33)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"FINISHED_GOODS", None));
        ___qlistwidgetitem36 = self.listWidget_chartview_datatypeslist.item(34)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"INVENTORIES", None));
        ___qlistwidgetitem37 = self.listWidget_chartview_datatypeslist.item(35)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"OTHER_CURRENT_ASSETS", None));
        ___qlistwidgetitem38 = self.listWidget_chartview_datatypeslist.item(36)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"TOTAL_CURRENT_ASSETS", None));
        ___qlistwidgetitem39 = self.listWidget_chartview_datatypeslist.item(37)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"PROPERTIES", None));
        ___qlistwidgetitem40 = self.listWidget_chartview_datatypeslist.item(38)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"MACHINE_FURNITURE_AND_EQUIPMENT", None));
        ___qlistwidgetitem41 = self.listWidget_chartview_datatypeslist.item(39)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"CONSTRUCTION_IN_PROGRESS", None));
        ___qlistwidgetitem42 = self.listWidget_chartview_datatypeslist.item(40)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"GROSS_PP_AND_E", None));
        ___qlistwidgetitem43 = self.listWidget_chartview_datatypeslist.item(41)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"ACCUMULATED_D_AND_A", None));
        ___qlistwidgetitem44 = self.listWidget_chartview_datatypeslist.item(42)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"NET_PP_AND_E", None));
        ___qlistwidgetitem45 = self.listWidget_chartview_datatypeslist.item(43)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"GOODWILL", None));
        ___qlistwidgetitem46 = self.listWidget_chartview_datatypeslist.item(44)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"OTHER_INTANGIBLE_ASSETS", None));
        ___qlistwidgetitem47 = self.listWidget_chartview_datatypeslist.item(45)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"GOODWILL_AND_INTANGIBLES", None));
        ___qlistwidgetitem48 = self.listWidget_chartview_datatypeslist.item(46)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_INVESTMENTS", None));
        ___qlistwidgetitem49 = self.listWidget_chartview_datatypeslist.item(47)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_RECEIVABLES", None));
        ___qlistwidgetitem50 = self.listWidget_chartview_datatypeslist.item(48)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_DEFERRED_ASSETS", None));
        ___qlistwidgetitem51 = self.listWidget_chartview_datatypeslist.item(49)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("MainWindow", u"OTHER_LONG_TERM_ASSETS", None));
        ___qlistwidgetitem52 = self.listWidget_chartview_datatypeslist.item(50)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("MainWindow", u"TOTAL_LONG_TERM_ASSETS", None));
        ___qlistwidgetitem53 = self.listWidget_chartview_datatypeslist.item(51)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("MainWindow", u"TOTAL_ASSETS", None));
        ___qlistwidgetitem54 = self.listWidget_chartview_datatypeslist.item(52)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("MainWindow", u"ACCOUNTS_PAYABLE", None));
        ___qlistwidgetitem55 = self.listWidget_chartview_datatypeslist.item(53)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("MainWindow", u"TOTAL_PAYABLES", None));
        ___qlistwidgetitem56 = self.listWidget_chartview_datatypeslist.item(54)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("MainWindow", u"ACCRUED_EXPENSES", None));
        ___qlistwidgetitem57 = self.listWidget_chartview_datatypeslist.item(55)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("MainWindow", u"PAYABLES_AND_ACCRUED_EXPENSES", None));
        ___qlistwidgetitem58 = self.listWidget_chartview_datatypeslist.item(56)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("MainWindow", u"OTHER_CURRENT_BORROWINGS", None));
        ___qlistwidgetitem59 = self.listWidget_chartview_datatypeslist.item(57)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("MainWindow", u"CURRENT_PORTION_OF_LONG_TERM_DEBT", None));
        ___qlistwidgetitem60 = self.listWidget_chartview_datatypeslist.item(58)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("MainWindow", u"CURRENT_DEFERREDREVEUE", None));
        ___qlistwidgetitem61 = self.listWidget_chartview_datatypeslist.item(59)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("MainWindow", u"OTHER_CURRENT_LIABILITIES", None));
        ___qlistwidgetitem62 = self.listWidget_chartview_datatypeslist.item(60)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("MainWindow", u"TOTAL_CURRENT_LIABILITIES", None));
        ___qlistwidgetitem63 = self.listWidget_chartview_datatypeslist.item(61)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("MainWindow", u"NON_CURRENT_PORTION_OF_LONG_TERM_DEBT", None));
        ___qlistwidgetitem64 = self.listWidget_chartview_datatypeslist.item(62)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_DEFERRED_TAX_LIABILITIES", None));
        ___qlistwidgetitem65 = self.listWidget_chartview_datatypeslist.item(63)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("MainWindow", u"NON_CURRENT_DEFERRED_LIABILITIES", None));
        ___qlistwidgetitem66 = self.listWidget_chartview_datatypeslist.item(64)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("MainWindow", u"OTHER_LONG_TERM_LIABILITIES", None));
        ___qlistwidgetitem67 = self.listWidget_chartview_datatypeslist.item(65)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("MainWindow", u"TOTAL_LONG_TERM_LIABILITIES", None));
        ___qlistwidgetitem68 = self.listWidget_chartview_datatypeslist.item(66)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("MainWindow", u"TOTAL_LIABILITIES", None));
        ___qlistwidgetitem69 = self.listWidget_chartview_datatypeslist.item(67)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("MainWindow", u"TOTAL_CAPITAL_STOCK", None));
        ___qlistwidgetitem70 = self.listWidget_chartview_datatypeslist.item(68)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("MainWindow", u"RETAINED_EARNINGS", None));
        ___qlistwidgetitem71 = self.listWidget_chartview_datatypeslist.item(69)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("MainWindow", u"ACCRUED_COMPREHENSIVE_INC", None));
        ___qlistwidgetitem72 = self.listWidget_chartview_datatypeslist.item(70)
        ___qlistwidgetitem72.setText(QCoreApplication.translate("MainWindow", u"SHAREHOLDERS_EQUITY", None));
        ___qlistwidgetitem73 = self.listWidget_chartview_datatypeslist.item(71)
        ___qlistwidgetitem73.setText(QCoreApplication.translate("MainWindow", u"LAND_AND_IMPROVEMENTS", None));
        ___qlistwidgetitem74 = self.listWidget_chartview_datatypeslist.item(72)
        ___qlistwidgetitem74.setText(QCoreApplication.translate("MainWindow", u"CURRENT_TAX_PAYABLE", None));
        ___qlistwidgetitem75 = self.listWidget_chartview_datatypeslist.item(73)
        ___qlistwidgetitem75.setText(QCoreApplication.translate("MainWindow", u"NET_INCOME", None));
        ___qlistwidgetitem76 = self.listWidget_chartview_datatypeslist.item(74)
        ___qlistwidgetitem76.setText(QCoreApplication.translate("MainWindow", u"OPERATING_GAINS_LOSSES", None));
        ___qlistwidgetitem77 = self.listWidget_chartview_datatypeslist.item(75)
        ___qlistwidgetitem77.setText(QCoreApplication.translate("MainWindow", u"TOTAL_DEPRECIATION_AND_AMORTIZATION", None));
        ___qlistwidgetitem78 = self.listWidget_chartview_datatypeslist.item(76)
        ___qlistwidgetitem78.setText(QCoreApplication.translate("MainWindow", u"DEFERRED_TAXES", None));
        ___qlistwidgetitem79 = self.listWidget_chartview_datatypeslist.item(77)
        ___qlistwidgetitem79.setText(QCoreApplication.translate("MainWindow", u"STOCK_BASED_COMPENSATION", None));
        ___qlistwidgetitem80 = self.listWidget_chartview_datatypeslist.item(78)
        ___qlistwidgetitem80.setText(QCoreApplication.translate("MainWindow", u"OTHER_NONCASH_ITEMS", None));
        ___qlistwidgetitem81 = self.listWidget_chartview_datatypeslist.item(79)
        ___qlistwidgetitem81.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_RECEIVABLES", None));
        ___qlistwidgetitem82 = self.listWidget_chartview_datatypeslist.item(80)
        ___qlistwidgetitem82.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_INVENTORIES", None));
        ___qlistwidgetitem83 = self.listWidget_chartview_datatypeslist.item(81)
        ___qlistwidgetitem83.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_PAYABLES_AND_ACCRUED_EXPENSE", None));
        ___qlistwidgetitem84 = self.listWidget_chartview_datatypeslist.item(82)
        ___qlistwidgetitem84.setText(QCoreApplication.translate("MainWindow", u"CHANGES_IN_OTHER_WORKING_CAP", None));
        ___qlistwidgetitem85 = self.listWidget_chartview_datatypeslist.item(83)
        ___qlistwidgetitem85.setText(QCoreApplication.translate("MainWindow", u"CHANGES_IN_WORKING_CAPITAL", None));
        ___qlistwidgetitem86 = self.listWidget_chartview_datatypeslist.item(84)
        ___qlistwidgetitem86.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_OPERATIONS", None));
        ___qlistwidgetitem87 = self.listWidget_chartview_datatypeslist.item(85)
        ___qlistwidgetitem87.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_CAPITAL_EXPENDITURES", None));
        ___qlistwidgetitem88 = self.listWidget_chartview_datatypeslist.item(86)
        ___qlistwidgetitem88.setText(QCoreApplication.translate("MainWindow", u"FREE_CASH_FLOW", None));
        ___qlistwidgetitem89 = self.listWidget_chartview_datatypeslist.item(87)
        ___qlistwidgetitem89.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_PP_AND_E", None));
        ___qlistwidgetitem90 = self.listWidget_chartview_datatypeslist.item(88)
        ___qlistwidgetitem90.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_INTANGIBLES", None));
        ___qlistwidgetitem91 = self.listWidget_chartview_datatypeslist.item(89)
        ___qlistwidgetitem91.setText(QCoreApplication.translate("MainWindow", u"ACQUISITIONS_AND_DISPOSITIONS", None));
        ___qlistwidgetitem92 = self.listWidget_chartview_datatypeslist.item(90)
        ___qlistwidgetitem92.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_INVESTING", None));
        ___qlistwidgetitem93 = self.listWidget_chartview_datatypeslist.item(91)
        ___qlistwidgetitem93.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_LONG_TERM_DEBT", None));
        ___qlistwidgetitem94 = self.listWidget_chartview_datatypeslist.item(92)
        ___qlistwidgetitem94.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_SHORT_TERM_DEBT", None));
        ___qlistwidgetitem95 = self.listWidget_chartview_datatypeslist.item(93)
        ___qlistwidgetitem95.setText(QCoreApplication.translate("MainWindow", u"NET_DEBT_ISSUANCE", None));
        ___qlistwidgetitem96 = self.listWidget_chartview_datatypeslist.item(94)
        ___qlistwidgetitem96.setText(QCoreApplication.translate("MainWindow", u"COMMON_STOCK_PAYMENTS", None));
        ___qlistwidgetitem97 = self.listWidget_chartview_datatypeslist.item(95)
        ___qlistwidgetitem97.setText(QCoreApplication.translate("MainWindow", u"NET_COMMON_EQUITY_ISSUED_PURCHASED", None));
        ___qlistwidgetitem98 = self.listWidget_chartview_datatypeslist.item(96)
        ___qlistwidgetitem98.setText(QCoreApplication.translate("MainWindow", u"TOTAL_COMMON_DIVIDENDS_PAID", None));
        ___qlistwidgetitem99 = self.listWidget_chartview_datatypeslist.item(97)
        ___qlistwidgetitem99.setText(QCoreApplication.translate("MainWindow", u"TOTAL_DIVIDENDS_PAID", None));
        ___qlistwidgetitem100 = self.listWidget_chartview_datatypeslist.item(98)
        ___qlistwidgetitem100.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_OTHER_FINANCING_ACTIVITIES", None));
        ___qlistwidgetitem101 = self.listWidget_chartview_datatypeslist.item(99)
        ___qlistwidgetitem101.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_FINANCING", None));
        ___qlistwidgetitem102 = self.listWidget_chartview_datatypeslist.item(100)
        ___qlistwidgetitem102.setText(QCoreApplication.translate("MainWindow", u"BEGINNING_CASH", None));
        ___qlistwidgetitem103 = self.listWidget_chartview_datatypeslist.item(101)
        ___qlistwidgetitem103.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_CASH", None));
        ___qlistwidgetitem104 = self.listWidget_chartview_datatypeslist.item(102)
        ___qlistwidgetitem104.setText(QCoreApplication.translate("MainWindow", u"CASH_FOREIGN_EXCHANGE_ADJUSTMENT", None));
        ___qlistwidgetitem105 = self.listWidget_chartview_datatypeslist.item(103)
        ___qlistwidgetitem105.setText(QCoreApplication.translate("MainWindow", u"ENDING_CASH", None));
        ___qlistwidgetitem106 = self.listWidget_chartview_datatypeslist.item(104)
        ___qlistwidgetitem106.setText(QCoreApplication.translate("MainWindow", u"ISSUANCE_OF_DEBT", None));
        ___qlistwidgetitem107 = self.listWidget_chartview_datatypeslist.item(105)
        ___qlistwidgetitem107.setText(QCoreApplication.translate("MainWindow", u"DEBT_REPAYMENT", None));
        ___qlistwidgetitem108 = self.listWidget_chartview_datatypeslist.item(106)
        ___qlistwidgetitem108.setText(QCoreApplication.translate("MainWindow", u"REPURCHASE_OF_CAPITAL_STOCK", None));
        ___qlistwidgetitem109 = self.listWidget_chartview_datatypeslist.item(107)
        ___qlistwidgetitem109.setText(QCoreApplication.translate("MainWindow", u"COMMON_STOCK_ISSUANCE", None));
        self.listWidget_chartview_datatypeslist.setSortingEnabled(__sortingEnabled2)

        self.label_chartview_datatypesdesc.setText(QCoreApplication.translate("MainWindow", u"Select Data Type's", None))
        self.label_chartview_datatypesdesc_2.setText(QCoreApplication.translate("MainWindow", u"Select Data Type's", None))

        __sortingEnabled3 = self.listWidget_chartview_datatypeslist_2.isSortingEnabled()
        self.listWidget_chartview_datatypeslist_2.setSortingEnabled(False)
        ___qlistwidgetitem110 = self.listWidget_chartview_datatypeslist_2.item(0)
        ___qlistwidgetitem110.setText(QCoreApplication.translate("MainWindow", u"OPERATING_REVENUE", None));
        ___qlistwidgetitem111 = self.listWidget_chartview_datatypeslist_2.item(1)
        ___qlistwidgetitem111.setText(QCoreApplication.translate("MainWindow", u"COST_OF_GOODS_SOLD", None));
        ___qlistwidgetitem112 = self.listWidget_chartview_datatypeslist_2.item(2)
        ___qlistwidgetitem112.setText(QCoreApplication.translate("MainWindow", u"GROSS_PROFIT", None));
        ___qlistwidgetitem113 = self.listWidget_chartview_datatypeslist_2.item(3)
        ___qlistwidgetitem113.setText(QCoreApplication.translate("MainWindow", u"SG_AND_A_EXPENSE", None));
        ___qlistwidgetitem114 = self.listWidget_chartview_datatypeslist_2.item(4)
        ___qlistwidgetitem114.setText(QCoreApplication.translate("MainWindow", u"RESEARCH_AND_DEVELOPMENT_EXPENSE", None));
        ___qlistwidgetitem115 = self.listWidget_chartview_datatypeslist_2.item(5)
        ___qlistwidgetitem115.setText(QCoreApplication.translate("MainWindow", u"SPECIAL_INCOME_AND_CHARGES", None));
        ___qlistwidgetitem116 = self.listWidget_chartview_datatypeslist_2.item(6)
        ___qlistwidgetitem116.setText(QCoreApplication.translate("MainWindow", u"OPERATING_INTEREST_EXPENSE", None));
        ___qlistwidgetitem117 = self.listWidget_chartview_datatypeslist_2.item(7)
        ___qlistwidgetitem117.setText(QCoreApplication.translate("MainWindow", u"NET_OPERATING_INTEREST_INCOME", None));
        ___qlistwidgetitem118 = self.listWidget_chartview_datatypeslist_2.item(8)
        ___qlistwidgetitem118.setText(QCoreApplication.translate("MainWindow", u"TOTAL_OPERATING_EXPENSES", None));
        ___qlistwidgetitem119 = self.listWidget_chartview_datatypeslist_2.item(9)
        ___qlistwidgetitem119.setText(QCoreApplication.translate("MainWindow", u"OPERATING_INCOME", None));
        ___qlistwidgetitem120 = self.listWidget_chartview_datatypeslist_2.item(10)
        ___qlistwidgetitem120.setText(QCoreApplication.translate("MainWindow", u"OTHER_INCOME_AND_EXPENSES", None));
        ___qlistwidgetitem121 = self.listWidget_chartview_datatypeslist_2.item(11)
        ___qlistwidgetitem121.setText(QCoreApplication.translate("MainWindow", u"PRE_TAX_INCOME", None));
        ___qlistwidgetitem122 = self.listWidget_chartview_datatypeslist_2.item(12)
        ___qlistwidgetitem122.setText(QCoreApplication.translate("MainWindow", u"PROVISION_FOR_INCOME_TAXES", None));
        ___qlistwidgetitem123 = self.listWidget_chartview_datatypeslist_2.item(13)
        ___qlistwidgetitem123.setText(QCoreApplication.translate("MainWindow", u"INCOME_FROM_CONTINUING_OPERATIONS", None));
        ___qlistwidgetitem124 = self.listWidget_chartview_datatypeslist_2.item(14)
        ___qlistwidgetitem124.setText(QCoreApplication.translate("MainWindow", u"NORMALIZED_INCOME", None));
        ___qlistwidgetitem125 = self.listWidget_chartview_datatypeslist_2.item(15)
        ___qlistwidgetitem125.setText(QCoreApplication.translate("MainWindow", u"EBITDA", None));
        ___qlistwidgetitem126 = self.listWidget_chartview_datatypeslist_2.item(16)
        ___qlistwidgetitem126.setText(QCoreApplication.translate("MainWindow", u"RECONCILED_DEPRECIATION", None));
        ___qlistwidgetitem127 = self.listWidget_chartview_datatypeslist_2.item(17)
        ___qlistwidgetitem127.setText(QCoreApplication.translate("MainWindow", u"EBIT", None));
        ___qlistwidgetitem128 = self.listWidget_chartview_datatypeslist_2.item(18)
        ___qlistwidgetitem128.setText(QCoreApplication.translate("MainWindow", u"EPS_BASIC_FROM_CONTINUING_OPERATIONS", None));
        ___qlistwidgetitem129 = self.listWidget_chartview_datatypeslist_2.item(19)
        ___qlistwidgetitem129.setText(QCoreApplication.translate("MainWindow", u"NORMALIZED_BASIC_EPS", None));
        ___qlistwidgetitem130 = self.listWidget_chartview_datatypeslist_2.item(20)
        ___qlistwidgetitem130.setText(QCoreApplication.translate("MainWindow", u"EPS_DILUTED_FROM_CONTINUING_OPERATIONS", None));
        ___qlistwidgetitem131 = self.listWidget_chartview_datatypeslist_2.item(21)
        ___qlistwidgetitem131.setText(QCoreApplication.translate("MainWindow", u"NORMALIZED_DILUTED_EPS", None));
        ___qlistwidgetitem132 = self.listWidget_chartview_datatypeslist_2.item(22)
        ___qlistwidgetitem132.setText(QCoreApplication.translate("MainWindow", u"AVERAGE_BASIC_SHARES_OUTSTANDING", None));
        ___qlistwidgetitem133 = self.listWidget_chartview_datatypeslist_2.item(23)
        ___qlistwidgetitem133.setText(QCoreApplication.translate("MainWindow", u"AVERAGE_DILUTED_SHARES_OUTSTANDING", None));
        ___qlistwidgetitem134 = self.listWidget_chartview_datatypeslist_2.item(24)
        ___qlistwidgetitem134.setText(QCoreApplication.translate("MainWindow", u"DIVIDEND_PER_SHARE", None));
        ___qlistwidgetitem135 = self.listWidget_chartview_datatypeslist_2.item(25)
        ___qlistwidgetitem135.setText(QCoreApplication.translate("MainWindow", u"OTHER_OPERATING_EXPENSES", None));
        ___qlistwidgetitem136 = self.listWidget_chartview_datatypeslist_2.item(26)
        ___qlistwidgetitem136.setText(QCoreApplication.translate("MainWindow", u"CASH_AND_EQUIVALENTS", None));
        ___qlistwidgetitem137 = self.listWidget_chartview_datatypeslist_2.item(27)
        ___qlistwidgetitem137.setText(QCoreApplication.translate("MainWindow", u"SHORT_TERM_INVESTMENTS", None));
        ___qlistwidgetitem138 = self.listWidget_chartview_datatypeslist_2.item(28)
        ___qlistwidgetitem138.setText(QCoreApplication.translate("MainWindow", u"CASH_AND_SHORT_TERM_INVESTMENTS", None));
        ___qlistwidgetitem139 = self.listWidget_chartview_datatypeslist_2.item(29)
        ___qlistwidgetitem139.setText(QCoreApplication.translate("MainWindow", u"ACCOUNTS_RECEIVABLES", None));
        ___qlistwidgetitem140 = self.listWidget_chartview_datatypeslist_2.item(30)
        ___qlistwidgetitem140.setText(QCoreApplication.translate("MainWindow", u"TOTAL_RECEIVABLES", None));
        ___qlistwidgetitem141 = self.listWidget_chartview_datatypeslist_2.item(31)
        ___qlistwidgetitem141.setText(QCoreApplication.translate("MainWindow", u"RAW_MATERIALS", None));
        ___qlistwidgetitem142 = self.listWidget_chartview_datatypeslist_2.item(32)
        ___qlistwidgetitem142.setText(QCoreApplication.translate("MainWindow", u"WORK_IN_PROCESS", None));
        ___qlistwidgetitem143 = self.listWidget_chartview_datatypeslist_2.item(33)
        ___qlistwidgetitem143.setText(QCoreApplication.translate("MainWindow", u"FINISHED_GOODS", None));
        ___qlistwidgetitem144 = self.listWidget_chartview_datatypeslist_2.item(34)
        ___qlistwidgetitem144.setText(QCoreApplication.translate("MainWindow", u"INVENTORIES", None));
        ___qlistwidgetitem145 = self.listWidget_chartview_datatypeslist_2.item(35)
        ___qlistwidgetitem145.setText(QCoreApplication.translate("MainWindow", u"OTHER_CURRENT_ASSETS", None));
        ___qlistwidgetitem146 = self.listWidget_chartview_datatypeslist_2.item(36)
        ___qlistwidgetitem146.setText(QCoreApplication.translate("MainWindow", u"TOTAL_CURRENT_ASSETS", None));
        ___qlistwidgetitem147 = self.listWidget_chartview_datatypeslist_2.item(37)
        ___qlistwidgetitem147.setText(QCoreApplication.translate("MainWindow", u"PROPERTIES", None));
        ___qlistwidgetitem148 = self.listWidget_chartview_datatypeslist_2.item(38)
        ___qlistwidgetitem148.setText(QCoreApplication.translate("MainWindow", u"MACHINE_FURNITURE_AND_EQUIPMENT", None));
        ___qlistwidgetitem149 = self.listWidget_chartview_datatypeslist_2.item(39)
        ___qlistwidgetitem149.setText(QCoreApplication.translate("MainWindow", u"CONSTRUCTION_IN_PROGRESS", None));
        ___qlistwidgetitem150 = self.listWidget_chartview_datatypeslist_2.item(40)
        ___qlistwidgetitem150.setText(QCoreApplication.translate("MainWindow", u"GROSS_PP_AND_E", None));
        ___qlistwidgetitem151 = self.listWidget_chartview_datatypeslist_2.item(41)
        ___qlistwidgetitem151.setText(QCoreApplication.translate("MainWindow", u"ACCUMULATED_D_AND_A", None));
        ___qlistwidgetitem152 = self.listWidget_chartview_datatypeslist_2.item(42)
        ___qlistwidgetitem152.setText(QCoreApplication.translate("MainWindow", u"NET_PP_AND_E", None));
        ___qlistwidgetitem153 = self.listWidget_chartview_datatypeslist_2.item(43)
        ___qlistwidgetitem153.setText(QCoreApplication.translate("MainWindow", u"GOODWILL", None));
        ___qlistwidgetitem154 = self.listWidget_chartview_datatypeslist_2.item(44)
        ___qlistwidgetitem154.setText(QCoreApplication.translate("MainWindow", u"OTHER_INTANGIBLE_ASSETS", None));
        ___qlistwidgetitem155 = self.listWidget_chartview_datatypeslist_2.item(45)
        ___qlistwidgetitem155.setText(QCoreApplication.translate("MainWindow", u"GOODWILL_AND_INTANGIBLES", None));
        ___qlistwidgetitem156 = self.listWidget_chartview_datatypeslist_2.item(46)
        ___qlistwidgetitem156.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_INVESTMENTS", None));
        ___qlistwidgetitem157 = self.listWidget_chartview_datatypeslist_2.item(47)
        ___qlistwidgetitem157.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_RECEIVABLES", None));
        ___qlistwidgetitem158 = self.listWidget_chartview_datatypeslist_2.item(48)
        ___qlistwidgetitem158.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_DEFERRED_ASSETS", None));
        ___qlistwidgetitem159 = self.listWidget_chartview_datatypeslist_2.item(49)
        ___qlistwidgetitem159.setText(QCoreApplication.translate("MainWindow", u"OTHER_LONG_TERM_ASSETS", None));
        ___qlistwidgetitem160 = self.listWidget_chartview_datatypeslist_2.item(50)
        ___qlistwidgetitem160.setText(QCoreApplication.translate("MainWindow", u"TOTAL_LONG_TERM_ASSETS", None));
        ___qlistwidgetitem161 = self.listWidget_chartview_datatypeslist_2.item(51)
        ___qlistwidgetitem161.setText(QCoreApplication.translate("MainWindow", u"TOTAL_ASSETS", None));
        ___qlistwidgetitem162 = self.listWidget_chartview_datatypeslist_2.item(52)
        ___qlistwidgetitem162.setText(QCoreApplication.translate("MainWindow", u"ACCOUNTS_PAYABLE", None));
        ___qlistwidgetitem163 = self.listWidget_chartview_datatypeslist_2.item(53)
        ___qlistwidgetitem163.setText(QCoreApplication.translate("MainWindow", u"TOTAL_PAYABLES", None));
        ___qlistwidgetitem164 = self.listWidget_chartview_datatypeslist_2.item(54)
        ___qlistwidgetitem164.setText(QCoreApplication.translate("MainWindow", u"ACCRUED_EXPENSES", None));
        ___qlistwidgetitem165 = self.listWidget_chartview_datatypeslist_2.item(55)
        ___qlistwidgetitem165.setText(QCoreApplication.translate("MainWindow", u"PAYABLES_AND_ACCRUED_EXPENSES", None));
        ___qlistwidgetitem166 = self.listWidget_chartview_datatypeslist_2.item(56)
        ___qlistwidgetitem166.setText(QCoreApplication.translate("MainWindow", u"OTHER_CURRENT_BORROWINGS", None));
        ___qlistwidgetitem167 = self.listWidget_chartview_datatypeslist_2.item(57)
        ___qlistwidgetitem167.setText(QCoreApplication.translate("MainWindow", u"CURRENT_PORTION_OF_LONG_TERM_DEBT", None));
        ___qlistwidgetitem168 = self.listWidget_chartview_datatypeslist_2.item(58)
        ___qlistwidgetitem168.setText(QCoreApplication.translate("MainWindow", u"CURRENT_DEFERREDREVEUE", None));
        ___qlistwidgetitem169 = self.listWidget_chartview_datatypeslist_2.item(59)
        ___qlistwidgetitem169.setText(QCoreApplication.translate("MainWindow", u"OTHER_CURRENT_LIABILITIES", None));
        ___qlistwidgetitem170 = self.listWidget_chartview_datatypeslist_2.item(60)
        ___qlistwidgetitem170.setText(QCoreApplication.translate("MainWindow", u"TOTAL_CURRENT_LIABILITIES", None));
        ___qlistwidgetitem171 = self.listWidget_chartview_datatypeslist_2.item(61)
        ___qlistwidgetitem171.setText(QCoreApplication.translate("MainWindow", u"NON_CURRENT_PORTION_OF_LONG_TERM_DEBT", None));
        ___qlistwidgetitem172 = self.listWidget_chartview_datatypeslist_2.item(62)
        ___qlistwidgetitem172.setText(QCoreApplication.translate("MainWindow", u"LONG_TERM_DEFERRED_TAX_LIABILITIES", None));
        ___qlistwidgetitem173 = self.listWidget_chartview_datatypeslist_2.item(63)
        ___qlistwidgetitem173.setText(QCoreApplication.translate("MainWindow", u"NON_CURRENT_DEFERRED_LIABILITIES", None));
        ___qlistwidgetitem174 = self.listWidget_chartview_datatypeslist_2.item(64)
        ___qlistwidgetitem174.setText(QCoreApplication.translate("MainWindow", u"OTHER_LONG_TERM_LIABILITIES", None));
        ___qlistwidgetitem175 = self.listWidget_chartview_datatypeslist_2.item(65)
        ___qlistwidgetitem175.setText(QCoreApplication.translate("MainWindow", u"TOTAL_LONG_TERM_LIABILITIES", None));
        ___qlistwidgetitem176 = self.listWidget_chartview_datatypeslist_2.item(66)
        ___qlistwidgetitem176.setText(QCoreApplication.translate("MainWindow", u"TOTAL_LIABILITIES", None));
        ___qlistwidgetitem177 = self.listWidget_chartview_datatypeslist_2.item(67)
        ___qlistwidgetitem177.setText(QCoreApplication.translate("MainWindow", u"TOTAL_CAPITAL_STOCK", None));
        ___qlistwidgetitem178 = self.listWidget_chartview_datatypeslist_2.item(68)
        ___qlistwidgetitem178.setText(QCoreApplication.translate("MainWindow", u"RETAINED_EARNINGS", None));
        ___qlistwidgetitem179 = self.listWidget_chartview_datatypeslist_2.item(69)
        ___qlistwidgetitem179.setText(QCoreApplication.translate("MainWindow", u"ACCRUED_COMPREHENSIVE_INC", None));
        ___qlistwidgetitem180 = self.listWidget_chartview_datatypeslist_2.item(70)
        ___qlistwidgetitem180.setText(QCoreApplication.translate("MainWindow", u"SHAREHOLDERS_EQUITY", None));
        ___qlistwidgetitem181 = self.listWidget_chartview_datatypeslist_2.item(71)
        ___qlistwidgetitem181.setText(QCoreApplication.translate("MainWindow", u"LAND_AND_IMPROVEMENTS", None));
        ___qlistwidgetitem182 = self.listWidget_chartview_datatypeslist_2.item(72)
        ___qlistwidgetitem182.setText(QCoreApplication.translate("MainWindow", u"CURRENT_TAX_PAYABLE", None));
        ___qlistwidgetitem183 = self.listWidget_chartview_datatypeslist_2.item(73)
        ___qlistwidgetitem183.setText(QCoreApplication.translate("MainWindow", u"NET_INCOME", None));
        ___qlistwidgetitem184 = self.listWidget_chartview_datatypeslist_2.item(74)
        ___qlistwidgetitem184.setText(QCoreApplication.translate("MainWindow", u"OPERATING_GAINS_LOSSES", None));
        ___qlistwidgetitem185 = self.listWidget_chartview_datatypeslist_2.item(75)
        ___qlistwidgetitem185.setText(QCoreApplication.translate("MainWindow", u"TOTAL_DEPRECIATION_AND_AMORTIZATION", None));
        ___qlistwidgetitem186 = self.listWidget_chartview_datatypeslist_2.item(76)
        ___qlistwidgetitem186.setText(QCoreApplication.translate("MainWindow", u"DEFERRED_TAXES", None));
        ___qlistwidgetitem187 = self.listWidget_chartview_datatypeslist_2.item(77)
        ___qlistwidgetitem187.setText(QCoreApplication.translate("MainWindow", u"STOCK_BASED_COMPENSATION", None));
        ___qlistwidgetitem188 = self.listWidget_chartview_datatypeslist_2.item(78)
        ___qlistwidgetitem188.setText(QCoreApplication.translate("MainWindow", u"OTHER_NONCASH_ITEMS", None));
        ___qlistwidgetitem189 = self.listWidget_chartview_datatypeslist_2.item(79)
        ___qlistwidgetitem189.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_RECEIVABLES", None));
        ___qlistwidgetitem190 = self.listWidget_chartview_datatypeslist_2.item(80)
        ___qlistwidgetitem190.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_INVENTORIES", None));
        ___qlistwidgetitem191 = self.listWidget_chartview_datatypeslist_2.item(81)
        ___qlistwidgetitem191.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_PAYABLES_AND_ACCRUED_EXPENSE", None));
        ___qlistwidgetitem192 = self.listWidget_chartview_datatypeslist_2.item(82)
        ___qlistwidgetitem192.setText(QCoreApplication.translate("MainWindow", u"CHANGES_IN_OTHER_WORKING_CAP", None));
        ___qlistwidgetitem193 = self.listWidget_chartview_datatypeslist_2.item(83)
        ___qlistwidgetitem193.setText(QCoreApplication.translate("MainWindow", u"CHANGES_IN_WORKING_CAPITAL", None));
        ___qlistwidgetitem194 = self.listWidget_chartview_datatypeslist_2.item(84)
        ___qlistwidgetitem194.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_OPERATIONS", None));
        ___qlistwidgetitem195 = self.listWidget_chartview_datatypeslist_2.item(85)
        ___qlistwidgetitem195.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_CAPITAL_EXPENDITURES", None));
        ___qlistwidgetitem196 = self.listWidget_chartview_datatypeslist_2.item(86)
        ___qlistwidgetitem196.setText(QCoreApplication.translate("MainWindow", u"FREE_CASH_FLOW", None));
        ___qlistwidgetitem197 = self.listWidget_chartview_datatypeslist_2.item(87)
        ___qlistwidgetitem197.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_PP_AND_E", None));
        ___qlistwidgetitem198 = self.listWidget_chartview_datatypeslist_2.item(88)
        ___qlistwidgetitem198.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_INTANGIBLES", None));
        ___qlistwidgetitem199 = self.listWidget_chartview_datatypeslist_2.item(89)
        ___qlistwidgetitem199.setText(QCoreApplication.translate("MainWindow", u"ACQUISITIONS_AND_DISPOSITIONS", None));
        ___qlistwidgetitem200 = self.listWidget_chartview_datatypeslist_2.item(90)
        ___qlistwidgetitem200.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_INVESTING", None));
        ___qlistwidgetitem201 = self.listWidget_chartview_datatypeslist_2.item(91)
        ___qlistwidgetitem201.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_LONG_TERM_DEBT", None));
        ___qlistwidgetitem202 = self.listWidget_chartview_datatypeslist_2.item(92)
        ___qlistwidgetitem202.setText(QCoreApplication.translate("MainWindow", u"NET_CHANGE_IN_SHORT_TERM_DEBT", None));
        ___qlistwidgetitem203 = self.listWidget_chartview_datatypeslist_2.item(93)
        ___qlistwidgetitem203.setText(QCoreApplication.translate("MainWindow", u"NET_DEBT_ISSUANCE", None));
        ___qlistwidgetitem204 = self.listWidget_chartview_datatypeslist_2.item(94)
        ___qlistwidgetitem204.setText(QCoreApplication.translate("MainWindow", u"COMMON_STOCK_PAYMENTS", None));
        ___qlistwidgetitem205 = self.listWidget_chartview_datatypeslist_2.item(95)
        ___qlistwidgetitem205.setText(QCoreApplication.translate("MainWindow", u"NET_COMMON_EQUITY_ISSUED_PURCHASED", None));
        ___qlistwidgetitem206 = self.listWidget_chartview_datatypeslist_2.item(96)
        ___qlistwidgetitem206.setText(QCoreApplication.translate("MainWindow", u"TOTAL_COMMON_DIVIDENDS_PAID", None));
        ___qlistwidgetitem207 = self.listWidget_chartview_datatypeslist_2.item(97)
        ___qlistwidgetitem207.setText(QCoreApplication.translate("MainWindow", u"TOTAL_DIVIDENDS_PAID", None));
        ___qlistwidgetitem208 = self.listWidget_chartview_datatypeslist_2.item(98)
        ___qlistwidgetitem208.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_OTHER_FINANCING_ACTIVITIES", None));
        ___qlistwidgetitem209 = self.listWidget_chartview_datatypeslist_2.item(99)
        ___qlistwidgetitem209.setText(QCoreApplication.translate("MainWindow", u"CASH_FROM_FINANCING", None));
        ___qlistwidgetitem210 = self.listWidget_chartview_datatypeslist_2.item(100)
        ___qlistwidgetitem210.setText(QCoreApplication.translate("MainWindow", u"BEGINNING_CASH", None));
        ___qlistwidgetitem211 = self.listWidget_chartview_datatypeslist_2.item(101)
        ___qlistwidgetitem211.setText(QCoreApplication.translate("MainWindow", u"CHANGE_IN_CASH", None));
        ___qlistwidgetitem212 = self.listWidget_chartview_datatypeslist_2.item(102)
        ___qlistwidgetitem212.setText(QCoreApplication.translate("MainWindow", u"CASH_FOREIGN_EXCHANGE_ADJUSTMENT", None));
        ___qlistwidgetitem213 = self.listWidget_chartview_datatypeslist_2.item(103)
        ___qlistwidgetitem213.setText(QCoreApplication.translate("MainWindow", u"ENDING_CASH", None));
        ___qlistwidgetitem214 = self.listWidget_chartview_datatypeslist_2.item(104)
        ___qlistwidgetitem214.setText(QCoreApplication.translate("MainWindow", u"ISSUANCE_OF_DEBT", None));
        ___qlistwidgetitem215 = self.listWidget_chartview_datatypeslist_2.item(105)
        ___qlistwidgetitem215.setText(QCoreApplication.translate("MainWindow", u"DEBT_REPAYMENT", None));
        ___qlistwidgetitem216 = self.listWidget_chartview_datatypeslist_2.item(106)
        ___qlistwidgetitem216.setText(QCoreApplication.translate("MainWindow", u"REPURCHASE_OF_CAPITAL_STOCK", None));
        ___qlistwidgetitem217 = self.listWidget_chartview_datatypeslist_2.item(107)
        ___qlistwidgetitem217.setText(QCoreApplication.translate("MainWindow", u"COMMON_STOCK_ISSUANCE", None));
        self.listWidget_chartview_datatypeslist_2.setSortingEnabled(__sortingEnabled3)

        self.label_chartview_datatypes_2.setText(QCoreApplication.translate("MainWindow", u"Data Types", None))
        ___qtablewidgetitem = self.tableWidget_dataview_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"2020", None));
        ___qtablewidgetitem1 = self.tableWidget_dataview_1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2019", None));
        ___qtablewidgetitem2 = self.tableWidget_dataview_1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2018", None));
        ___qtablewidgetitem3 = self.tableWidget_dataview_1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2017", None));
        ___qtablewidgetitem4 = self.tableWidget_dataview_1.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2016", None));
        ___qtablewidgetitem5 = self.tableWidget_dataview_1.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2015", None));
        ___qtablewidgetitem6 = self.tableWidget_dataview_1.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2014", None));
        ___qtablewidgetitem7 = self.tableWidget_dataview_1.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2013", None));
        ___qtablewidgetitem8 = self.tableWidget_dataview_1.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2012", None));
        ___qtablewidgetitem9 = self.tableWidget_dataview_1.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2011", None));
        ___qtablewidgetitem10 = self.tableWidget_dataview_1.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"2010", None));
        ___qtablewidgetitem11 = self.tableWidget_dataview_1.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2009", None));
        ___qtablewidgetitem12 = self.tableWidget_dataview_1.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Operating Revenue", None));
        ___qtablewidgetitem13 = self.tableWidget_dataview_1.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Annualized Change%", None));

        __sortingEnabled4 = self.tableWidget_dataview_1.isSortingEnabled()
        self.tableWidget_dataview_1.setSortingEnabled(False)
        self.tableWidget_dataview_1.setSortingEnabled(__sortingEnabled4)

        self.label_dataview_company.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_dataview_company_data.setText(QCoreApplication.translate("MainWindow", u"Intel Corporation", None))
        self.label_dataview_loadeddata.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.label_dataview_selecteddatatype.setText(QCoreApplication.translate("MainWindow", u"Change in Payables and Accrued Expense", None))
        ___qtablewidgetitem14 = self.tableWidget_dataview_2.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"2030", None));
        ___qtablewidgetitem15 = self.tableWidget_dataview_2.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2029", None));
        ___qtablewidgetitem16 = self.tableWidget_dataview_2.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"2028", None));
        ___qtablewidgetitem17 = self.tableWidget_dataview_2.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2027", None));
        ___qtablewidgetitem18 = self.tableWidget_dataview_2.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"2026", None));
        ___qtablewidgetitem19 = self.tableWidget_dataview_2.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"2025", None));
        ___qtablewidgetitem20 = self.tableWidget_dataview_2.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"2024", None));
        ___qtablewidgetitem21 = self.tableWidget_dataview_2.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"2023", None));
        ___qtablewidgetitem22 = self.tableWidget_dataview_2.horizontalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"2022", None));
        ___qtablewidgetitem23 = self.tableWidget_dataview_2.horizontalHeaderItem(9)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2021", None));
        ___qtablewidgetitem24 = self.tableWidget_dataview_2.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Operating Revenue", None));
        ___qtablewidgetitem25 = self.tableWidget_dataview_2.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Annualized Change%", None));
        self.label_dataview_projectforward.setText(QCoreApplication.translate("MainWindow", u"Project Forward", None))
        self.label_dataview_change.setText(QCoreApplication.translate("MainWindow", u"Change %", None))
        self.checkBox_dataview_applychange.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_dataview_throttle.setText(QCoreApplication.translate("MainWindow", u"Throttle %", None))
        self.checkBox_dataview_applythrottle.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.comboBox_dataview_avgofyears.setItemText(0, QCoreApplication.translate("MainWindow", u"All Years", None))
        self.comboBox_dataview_avgofyears.setItemText(1, QCoreApplication.translate("MainWindow", u"10 Years", None))
        self.comboBox_dataview_avgofyears.setItemText(2, QCoreApplication.translate("MainWindow", u"5 Years", None))

        self.label_dataview_avgof.setText(QCoreApplication.translate("MainWindow", u"Avg % Of", None))
        self.comboBox_dataview_projectyears.setItemText(0, QCoreApplication.translate("MainWindow", u"10 Years", None))
        self.comboBox_dataview_projectyears.setItemText(1, QCoreApplication.translate("MainWindow", u"7 Years", None))
        self.comboBox_dataview_projectyears.setItemText(2, QCoreApplication.translate("MainWindow", u"5 Years", None))

        self.comboBox_dataview_chartselector.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_dataview_chartselector.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_dataview_chartselector.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_dataview_chartselector.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_dataview_chartselector.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.label_dataview_visualized.setText(QCoreApplication.translate("MainWindow", u"Visualized", None))
        ___qtablewidgetitem26 = self.tableWidget_forecast1.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2031", None));
        ___qtablewidgetitem27 = self.tableWidget_forecast1.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2030", None));
        ___qtablewidgetitem28 = self.tableWidget_forecast1.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"2029", None));
        ___qtablewidgetitem29 = self.tableWidget_forecast1.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"2028", None));
        ___qtablewidgetitem30 = self.tableWidget_forecast1.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"2027", None));
        ___qtablewidgetitem31 = self.tableWidget_forecast1.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"2026", None));
        ___qtablewidgetitem32 = self.tableWidget_forecast1.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"2025", None));
        ___qtablewidgetitem33 = self.tableWidget_forecast1.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"2024", None));
        ___qtablewidgetitem34 = self.tableWidget_forecast1.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"2022", None));
        ___qtablewidgetitem35 = self.tableWidget_forecast1.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"2021", None));
        ___qtablewidgetitem36 = self.tableWidget_forecast1.verticalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Future EBITDA", None));
        ___qtablewidgetitem37 = self.tableWidget_forecast1.verticalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem38 = self.tableWidget_forecast1.verticalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Enterprise Value", None));
        ___qtablewidgetitem39 = self.tableWidget_forecast1.verticalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem40 = self.tableWidget_forecast1.verticalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Projected Debt", None));
        ___qtablewidgetitem41 = self.tableWidget_forecast1.verticalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem42 = self.tableWidget_forecast1.verticalHeaderItem(6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Shr. Outstanding", None));
        ___qtablewidgetitem43 = self.tableWidget_forecast1.verticalHeaderItem(7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem44 = self.tableWidget_forecast1.verticalHeaderItem(8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Market Cap", None));
        ___qtablewidgetitem45 = self.tableWidget_forecast1.verticalHeaderItem(9)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem46 = self.tableWidget_forecast1.verticalHeaderItem(10)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Projected FCF", None));
        ___qtablewidgetitem47 = self.tableWidget_forecast1.verticalHeaderItem(11)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem48 = self.tableWidget_forecast1.verticalHeaderItem(12)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"FCF/Share", None));
        ___qtablewidgetitem49 = self.tableWidget_forecast1.verticalHeaderItem(13)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem50 = self.tableWidget_forecast1.verticalHeaderItem(14)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Avg Yield %", None));
        ___qtablewidgetitem51 = self.tableWidget_forecast1.verticalHeaderItem(15)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"EV/EBITDA $", None));
        ___qtablewidgetitem52 = self.tableWidget_forecast1.verticalHeaderItem(16)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        ___qtablewidgetitem53 = self.tableWidget_forecast1.verticalHeaderItem(17)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"FCF/Share $", None));
        ___qtablewidgetitem54 = self.tableWidget_forecast1.verticalHeaderItem(18)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Annualized %", None));
        self.label_forecast_2.setText(QCoreApplication.translate("MainWindow", u"Forecast", None))
        self.label_forecast_company_data.setText(QCoreApplication.translate("MainWindow", u"Intel Corporation", None))
        self.label_forecast.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.label_forecast_throttle_9.setText(QCoreApplication.translate("MainWindow", u"Throttle %", None))
        self.comboBox_forecast_avgofyears.setItemText(0, QCoreApplication.translate("MainWindow", u"All Years", None))
        self.comboBox_forecast_avgofyears.setItemText(1, QCoreApplication.translate("MainWindow", u"10 Years", None))
        self.comboBox_forecast_avgofyears.setItemText(2, QCoreApplication.translate("MainWindow", u"5 Years", None))
        self.comboBox_forecast_avgofyears.setItemText(3, QCoreApplication.translate("MainWindow", u"3 Years", None))

        self.checkBox_forecast_enabledfcf.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_forecast_throttle_12.setText(QCoreApplication.translate("MainWindow", u"Free CashFlow", None))
        self.label_forecast_throttle_13.setText(QCoreApplication.translate("MainWindow", u"Avgs. From", None))
        self.label_forecast_throttle_14.setText(QCoreApplication.translate("MainWindow", u"Forecast Fwd.", None))
        self.comboBox_forecast_projectyears.setItemText(0, QCoreApplication.translate("MainWindow", u"10 Years", None))
        self.comboBox_forecast_projectyears.setItemText(1, QCoreApplication.translate("MainWindow", u"7 Years", None))
        self.comboBox_forecast_projectyears.setItemText(2, QCoreApplication.translate("MainWindow", u"5 Years", None))

        self.checkBox_forecast_enabledebitda.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_forecast_throttle_15.setText(QCoreApplication.translate("MainWindow", u"EBITDA", None))
        self.label_forecast_throttle_16.setText(QCoreApplication.translate("MainWindow", u"Throttle %", None))
        self.label_forecast_throttle_19.setText(QCoreApplication.translate("MainWindow", u"Throttle Variable", None))
        self.checkBox_forecast_enabledfcfyield.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_forecast_throttle_17.setText(QCoreApplication.translate("MainWindow", u"FCF Yield", None))
        self.label_forecast_throttle_18.setText(QCoreApplication.translate("MainWindow", u"Throttle %", None))
        self.label_forecast_throttle_20.setText(QCoreApplication.translate("MainWindow", u"Lock/Limit Variable", None))
        self.checkBox_forecast_enabledshares.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_forecast_throttle.setText(QCoreApplication.translate("MainWindow", u"Shares Out.", None))
        self.label_forecast_throttle_2.setText(QCoreApplication.translate("MainWindow", u"Throttle %", None))
        self.checkBox_forecast_lockenabled_ebitda.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.checkBox_forecast_lockenabled_fcf.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_forecast_throttle_3.setText(QCoreApplication.translate("MainWindow", u"Free CashFlow", None))
        self.label_forecast_throttle_4.setText(QCoreApplication.translate("MainWindow", u"FCF Yield", None))
        self.label_forecast_throttle_5.setText(QCoreApplication.translate("MainWindow", u"Shares Out.", None))
        self.checkBox_forecast_lockenabled_fcfyield.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.checkBox_forecast_lockenabled_shares.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_forecast_throttle_6.setText(QCoreApplication.translate("MainWindow", u"EBITDA", None))
        self.label_forecast_throttle_7.setText(QCoreApplication.translate("MainWindow", u"Lock/Limit %", None))
        self.label_forecast_throttle_8.setText(QCoreApplication.translate("MainWindow", u"Lock/Limit %", None))
        self.label_forecast_throttle_10.setText(QCoreApplication.translate("MainWindow", u"Lock/Limit %", None))
        self.label_forecast_throttle_11.setText(QCoreApplication.translate("MainWindow", u"Lock/Limit %", None))
        self.label_forecast_throttle_21.setText(QCoreApplication.translate("MainWindow", u"Throttle Variable", None))
        self.label_forecast_throttle_22.setText(QCoreApplication.translate("MainWindow", u"Data Will Override Forecast", None))
        self.comboBox_forecast_charttype1.setItemText(0, QCoreApplication.translate("MainWindow", u"STANDARD BAR CHART", None))
        self.comboBox_forecast_charttype1.setItemText(1, QCoreApplication.translate("MainWindow", u"STACKED BAR CHART", None))
        self.comboBox_forecast_charttype1.setItemText(2, QCoreApplication.translate("MainWindow", u"LINE PLOT CHART", None))
        self.comboBox_forecast_charttype1.setItemText(3, QCoreApplication.translate("MainWindow", u"STEM PLOT CHART", None))
        self.comboBox_forecast_charttype1.setItemText(4, QCoreApplication.translate("MainWindow", u"STACKED AREA CHART", None))

        self.label_forecast_3.setText(QCoreApplication.translate("MainWindow", u"Visualized", None))
        self.comboBox_forecast_chartselector1.setItemText(0, QCoreApplication.translate("MainWindow", u"Future Share Price", None))
        self.comboBox_forecast_chartselector1.setItemText(1, QCoreApplication.translate("MainWindow", u"Future CashFlow", None))
        self.comboBox_forecast_chartselector1.setItemText(2, QCoreApplication.translate("MainWindow", u"Future Enterprise Value", None))
        self.comboBox_forecast_chartselector1.setItemText(3, QCoreApplication.translate("MainWindow", u"Future Shares Outstanding", None))

        self.label_checklist_8.setText(QCoreApplication.translate("MainWindow", u"Profit Growth", None))
        self.label_checklist_24.setText(QCoreApplication.translate("MainWindow", u"Revenue Growth", None))
        self.label_checklist_23.setText(QCoreApplication.translate("MainWindow", u"Earnings Growth", None))
        self.label_checklist_22.setText(QCoreApplication.translate("MainWindow", u"CashFlow Growth", None))
        self.label_checklist_21.setText(QCoreApplication.translate("MainWindow", u"Assets > Liabilities", None))
        self.label_checklist_20.setText(QCoreApplication.translate("MainWindow", u"Assets Growing", None))
        self.label_checklist_19.setText(QCoreApplication.translate("MainWindow", u"Fair Liabilities", None))
        self.label_checklist_18.setText(QCoreApplication.translate("MainWindow", u"Fair P/E Ratio", None))
        self.label_checklist_17.setText(QCoreApplication.translate("MainWindow", u"Fair P/FCF Ratio", None))
        self.label_checklist_16.setText(QCoreApplication.translate("MainWindow", u"Shares Decreasing", None))
        self.label_checklist_15.setText(QCoreApplication.translate("MainWindow", u"Solid Moat", None))
        self.label_checklist_14.setText(QCoreApplication.translate("MainWindow", u"Solid Managment", None))
        self.label_checklist_13.setText(QCoreApplication.translate("MainWindow", u"Insider Buying", None))
        self.label_checklist_11.setText(QCoreApplication.translate("MainWindow", u"Standard Pointers", None))
        self.label_checklist_10.setText(QCoreApplication.translate("MainWindow", u"Bonus Pointers", None))
        self.checkBox_checklist_passprofit.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passrevenue.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passearnings.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passassetsvsliabilties.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passassests.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passfcf.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passpe.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passshares.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passsolidmoat.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passsolidmanagment.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passfairfcfratio.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passfairliabilities.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.checkBox_checklist_passinsiderbuying.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.comboBox_checklist_avgyeras.setItemText(0, QCoreApplication.translate("MainWindow", u"10 Years", None))
        self.comboBox_checklist_avgyeras.setItemText(1, QCoreApplication.translate("MainWindow", u"5 Years", None))
        self.comboBox_checklist_avgyeras.setItemText(2, QCoreApplication.translate("MainWindow", u"7 Years", None))
        self.comboBox_checklist_avgyeras.setItemText(3, QCoreApplication.translate("MainWindow", u"All Years", None))

        self.label_checklist_fairliabilties.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklist_assetgrowth.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklist_assetliabilties.setText(QCoreApplication.translate("MainWindow", u"1.3x", None))
        self.label_checklist_fcfgrowth.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklist_earningsgrowth.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklist_revgrowth.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklist_profitgrowth.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklistfcfratio.setText(QCoreApplication.translate("MainWindow", u"10.6", None))
        self.checkBox_checklist_passsolidmargin.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.label_checklist_12.setText(QCoreApplication.translate("MainWindow", u"Solid Profit Margin", None))
        self.label_checklist_profitmargin.setText(QCoreApplication.translate("MainWindow", u"56%", None))
        self.label_checklist_shares.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.label_checklist_passes.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_checklist_fails.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_checklist_25.setText(QCoreApplication.translate("MainWindow", u"PASS | FAIL", None))
        self.label_checklist_9.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_checklist_pe.setText(QCoreApplication.translate("MainWindow", u"10.6", None))
        self.label_checklist_39.setText(QCoreApplication.translate("MainWindow", u"Visualized", None))
        ___qtablewidgetitem55 = self.tableWidget_checklist_prices.horizontalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Mean", None));
        ___qtablewidgetitem56 = self.tableWidget_checklist_prices.horizontalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem57 = self.tableWidget_checklist_prices.horizontalHeaderItem(2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Med", None));
        ___qtablewidgetitem58 = self.tableWidget_checklist_prices.horizontalHeaderItem(3)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Low", None));
        ___qtablewidgetitem59 = self.tableWidget_checklist_prices.verticalHeaderItem(0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Average", None));
        ___qtablewidgetitem60 = self.tableWidget_checklist_prices.verticalHeaderItem(1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"EV/EBITDA", None));
        ___qtablewidgetitem61 = self.tableWidget_checklist_prices.verticalHeaderItem(2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"FCFE/SHR", None));
        ___qtablewidgetitem62 = self.tableWidget_checklist_prices.verticalHeaderItem(3)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem63 = self.tableWidget_checklist_prices.verticalHeaderItem(4)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"TipRanks", None));
        ___qtablewidgetitem64 = self.tableWidget_checklist_prices.verticalHeaderItem(5)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Simply Wst", None));
        ___qtablewidgetitem65 = self.tableWidget_checklist_prices.verticalHeaderItem(6)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"WSJ", None));
        self.label_checklist_40.setText(QCoreApplication.translate("MainWindow", u"Calculate Price", None))
        self.label_checklist_41.setText(QCoreApplication.translate("MainWindow", u"Discount/Value Chart", None))
        self.label_checklist_32.setText(QCoreApplication.translate("MainWindow", u"Extreme Value", None))
        self.label_checklist_31.setText(QCoreApplication.translate("MainWindow", u"Heavily Undervalued", None))
        self.label_checklist_30.setText(QCoreApplication.translate("MainWindow", u"Slightly Undervalued", None))
        self.label_checklist_29.setText(QCoreApplication.translate("MainWindow", u"Fairly Valued", None))
        self.label_checklist_28.setText(QCoreApplication.translate("MainWindow", u"Slightly Overvalued", None))
        self.label_checklist_26.setText(QCoreApplication.translate("MainWindow", u"Heavily Overvalued", None))
        self.label_checklist_27.setText(QCoreApplication.translate("MainWindow", u"10% to -10%", None))
        self.label_checklist_38.setText(QCoreApplication.translate("MainWindow", u"Discount > 25%", None))
        self.label_checklist_37.setText(QCoreApplication.translate("MainWindow", u"15% to 10%", None))
        self.label_checklist_36.setText(QCoreApplication.translate("MainWindow", u"-10% to -15%", None))
        self.label_checklist_35.setText(QCoreApplication.translate("MainWindow", u"25% to 16%", None))
        self.label_checklist_34.setText(QCoreApplication.translate("MainWindow", u"-16% to -25% ", None))
        self.label_checklist_33.setText(QCoreApplication.translate("MainWindow", u"Margin Of Saftey", None))
        self.label_checklist_4.setText(QCoreApplication.translate("MainWindow", u"Current Price", None))
        self.label_checklist_currentprice.setText(QCoreApplication.translate("MainWindow", u"$53", None))
        self.label_checklist_6.setText(QCoreApplication.translate("MainWindow", u"Forecast Return", None))
        self.label_checklist.setText(QCoreApplication.translate("MainWindow", u"Current Value", None))
        self.label_checklist_currentvalue.setText(QCoreApplication.translate("MainWindow", u"$60", None))
        self.label_checklist_2.setText(QCoreApplication.translate("MainWindow", u"Points", None))
        self.label_checklist_3.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
        self.label_checklist_rating.setText(QCoreApplication.translate("MainWindow", u"Slightly Undervalued", None))
        self.label_checklist_points.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_checklist_5.setText(QCoreApplication.translate("MainWindow", u"Price Rating", None))
        self.label_checklist_discount.setText(QCoreApplication.translate("MainWindow", u"%20", None))
        self.label_checklist_7.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_checklist_company_data.setText(QCoreApplication.translate("MainWindow", u"Intel Corporation", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Stock Analizer Tool", None))
        self.label_downloadstockdata.setText(QCoreApplication.translate("MainWindow", u"Download Stock Data", None))
        self.pushButton_loadstockdata.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Ticker Symbol", None))
        self.pushButton_dataview.setText(QCoreApplication.translate("MainWindow", u"Data View", None))
        self.pushButton_overview.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.pushButton_chartview.setText(QCoreApplication.translate("MainWindow", u"Chart View", None))
        self.pushButton_forecast.setText(QCoreApplication.translate("MainWindow", u"Forecast", None))
        self.pushButton_checklist.setText(QCoreApplication.translate("MainWindow", u"CheckList", None))
    # retranslateUi

