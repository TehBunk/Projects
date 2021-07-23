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
        MainWindow.resize(1080, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(1080, 720))
        icon = QIcon()
        icon.addFile(u"1x/attach_money.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: #a9d6e5")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 70, 911, 641))
        font = QFont()
        font.setFamily(u"Bahnschrift SemiLight")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color: #89c2d9;")
        self.page_overview = QWidget()
        self.page_overview.setObjectName(u"page_overview")
        self.page_overview.setStyleSheet(u"")
        self.label_company = QLabel(self.page_overview)
        self.label_company.setObjectName(u"label_company")
        self.label_company.setGeometry(QRect(10, 10, 101, 31))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiLight")
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_company.setFont(font1)
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
        self.label_company_data = QLabel(self.page_overview)
        self.label_company_data.setObjectName(u"label_company_data")
        self.label_company_data.setGeometry(QRect(120, 10, 341, 31))
        self.label_company_data.setFont(font1)
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
        self.label_sector = QLabel(self.page_overview)
        self.label_sector.setObjectName(u"label_sector")
        self.label_sector.setGeometry(QRect(10, 50, 101, 31))
        self.label_sector.setFont(font1)
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
        self.label_industry = QLabel(self.page_overview)
        self.label_industry.setObjectName(u"label_industry")
        self.label_industry.setGeometry(QRect(10, 90, 101, 31))
        self.label_industry.setFont(font1)
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
        self.label_marketcap = QLabel(self.page_overview)
        self.label_marketcap.setObjectName(u"label_marketcap")
        self.label_marketcap.setGeometry(QRect(10, 130, 101, 31))
        self.label_marketcap.setFont(font1)
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
        self.label_sector_data = QLabel(self.page_overview)
        self.label_sector_data.setObjectName(u"label_sector_data")
        self.label_sector_data.setGeometry(QRect(120, 50, 341, 31))
        self.label_sector_data.setFont(font1)
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
        self.label_industry_data = QLabel(self.page_overview)
        self.label_industry_data.setObjectName(u"label_industry_data")
        self.label_industry_data.setGeometry(QRect(120, 90, 341, 31))
        self.label_industry_data.setFont(font1)
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
        self.label_marketcap_data = QLabel(self.page_overview)
        self.label_marketcap_data.setObjectName(u"label_marketcap_data")
        self.label_marketcap_data.setGeometry(QRect(120, 130, 341, 31))
        self.label_marketcap_data.setFont(font1)
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
        self.label_description = QLabel(self.page_overview)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 170, 451, 31))
        self.label_description.setFont(font1)
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
        self.frame_overview_chartbackground = QFrame(self.page_overview)
        self.frame_overview_chartbackground.setObjectName(u"frame_overview_chartbackground")
        self.frame_overview_chartbackground.setGeometry(QRect(470, 10, 431, 191))
        font2 = QFont()
        font2.setPointSize(10)
        self.frame_overview_chartbackground.setFont(font2)
        self.frame_overview_chartbackground.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_chartbackground.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_chartbackground.setFrameShadow(QFrame.Raised)
        self.frame_overview_chart = QFrame(self.frame_overview_chartbackground)
        self.frame_overview_chart.setObjectName(u"frame_overview_chart")
        self.frame_overview_chart.setGeometry(QRect(10, 10, 411, 171))
        self.frame_overview_chart.setStyleSheet(u"border: none")
        self.frame_overview_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_chart.setFrameShadow(QFrame.Raised)
        self.frame_overview_backround = QFrame(self.page_overview)
        self.frame_overview_backround.setObjectName(u"frame_overview_backround")
        self.frame_overview_backround.setGeometry(QRect(10, 370, 891, 261))
        self.frame_overview_backround.setFont(font2)
        self.frame_overview_backround.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_backround.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_backround.setFrameShadow(QFrame.Raised)
        self.frame_overview_background_header = QFrame(self.frame_overview_backround)
        self.frame_overview_background_header.setObjectName(u"frame_overview_background_header")
        self.frame_overview_background_header.setGeometry(QRect(0, 0, 891, 51))
        self.frame_overview_background_header.setFont(font2)
        self.frame_overview_background_header.setStyleSheet(u"background-color: #61a5c2; \n"
"border-radius: 5px;\n"
"border: 2px solid #468FAF;\n"
"")
        self.frame_overview_background_header.setFrameShape(QFrame.StyledPanel)
        self.frame_overview_background_header.setFrameShadow(QFrame.Raised)
        self.label_metrics = QLabel(self.frame_overview_background_header)
        self.label_metrics.setObjectName(u"label_metrics")
        self.label_metrics.setGeometry(QRect(10, 10, 211, 31))
        self.label_metrics.setFont(font1)
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
        self.label_lastprice.setFont(font1)
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
        self.label_lastprice_data.setFont(font1)
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
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiLight")
        font3.setPointSize(11)
        font3.setBold(False)
        self.label_52weekhigh_data.setFont(font3)
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
        self.label_52weekhigh.setFont(font3)
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
        self.label_52weeklow_data.setFont(font3)
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
        self.label_52weeklow.setFont(font3)
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
        self.label_5yearavgyield_data.setFont(font3)
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
        self.label_sharesoutstanding_data.setFont(font3)
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
        self.label_currentyield_data.setFont(font3)
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
        self.label_sharediv_data.setFont(font3)
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
        self.label_beta_data.setFont(font3)
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
        self.label_50dayma_data.setFont(font3)
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
        self.label_enterprisevalue_data.setFont(font3)
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
        self.label_200dayma_data.setFont(font3)
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
        self.label_200dayma.setFont(font1)
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
        self.label_50dayma.setFont(font1)
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
        self.label_5yearavgyield.setFont(font1)
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
        self.label_currentyield.setFont(font1)
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
        self.label_sharediv.setFont(font1)
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
        self.label_beta.setFont(font1)
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
        self.label_enterprisevalue.setFont(font1)
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
        self.label_sharesoutstanding.setFont(font1)
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
        self.label_targetmed_data.setFont(font3)
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
        self.label_targetmed.setFont(font1)
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
        self.label_targethigh.setFont(font1)
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
        self.label_targetmean.setFont(font1)
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
        self.label_targetmean_data.setFont(font3)
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
        self.label_targethigh_data.setFont(font3)
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
        self.label_targetlow_data.setFont(font3)
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
        self.label_targetlow.setFont(font1)
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
        self.label_bookvalue.setFont(font1)
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
        self.label_bookvalue_data.setFont(font3)
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
        self.label_pricebook_data.setFont(font3)
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
        self.label_pricebook.setFont(font1)
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
        self.label_avgvolume_data.setFont(font3)
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
        self.label_rps.setFont(font1)
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
        self.label_evebitda.setFont(font1)
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
        self.label_evebitda_data.setFont(font3)
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
        self.label_evr_data.setFont(font3)
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
        self.label_evr.setFont(font1)
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
        self.label_rps_data.setFont(font3)
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
        self.label_avgvolume.setFont(font1)
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
        self.textBrowser_description_data = QTextBrowser(self.page_overview)
        self.textBrowser_description_data.setObjectName(u"textBrowser_description_data")
        self.textBrowser_description_data.setGeometry(QRect(10, 210, 891, 151))
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
        self.stackedWidget.addWidget(self.page_overview)
        self.page_dataview = QWidget()
        self.page_dataview.setObjectName(u"page_dataview")
        self.stackedWidget.addWidget(self.page_dataview)
        self.page_income = QWidget()
        self.page_income.setObjectName(u"page_income")
        self.stackedWidget.addWidget(self.page_income)
        self.page_balance = QWidget()
        self.page_balance.setObjectName(u"page_balance")
        self.stackedWidget.addWidget(self.page_balance)
        self.page_cashflow = QWidget()
        self.page_cashflow.setObjectName(u"page_cashflow")
        self.stackedWidget.addWidget(self.page_cashflow)
        self.page_debug = QWidget()
        self.page_debug.setObjectName(u"page_debug")
        self.stackedWidget.addWidget(self.page_debug)
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 10, 231, 51))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_title.setFont(font4)
        self.label_title.setStyleSheet(u"background-color: #89c2d9; \n"
"border-radius: 10px; \n"
"border: 3px solid #61A5C2")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_companylistheader = QLabel(self.centralwidget)
        self.label_companylistheader.setObjectName(u"label_companylistheader")
        self.label_companylistheader.setGeometry(QRect(10, 70, 141, 31))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiLight")
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_companylistheader.setFont(font5)
        self.label_companylistheader.setStyleSheet(u"background-color: #61a5c2;\n"
"border: 2px solid #468FAF;")
        self.label_companylistheader.setAlignment(Qt.AlignCenter)
        self.listWidget_companylist = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget_companylist)
        QListWidgetItem(self.listWidget_companylist)
        self.listWidget_companylist.setObjectName(u"listWidget_companylist")
        self.listWidget_companylist.setGeometry(QRect(10, 140, 141, 571))
        self.listWidget_companylist.setFont(font)
        self.listWidget_companylist.setStyleSheet(u"background-color: #61a5c2; \n"
"border: 2px solid #468FAF;\n"
"")
        self.label_companylistsubheader = QLabel(self.centralwidget)
        self.label_companylistsubheader.setObjectName(u"label_companylistsubheader")
        self.label_companylistsubheader.setGeometry(QRect(10, 110, 141, 21))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift SemiLight")
        font6.setPointSize(10)
        font6.setBold(False)
        self.label_companylistsubheader.setFont(font6)
        self.label_companylistsubheader.setStyleSheet(u"background-color: #61a5c2; border: 2px solid #468FAF;")
        self.label_companylistsubheader.setAlignment(Qt.AlignCenter)
        self.label_downloadstockdata = QLabel(self.centralwidget)
        self.label_downloadstockdata.setObjectName(u"label_downloadstockdata")
        self.label_downloadstockdata.setGeometry(QRect(870, 10, 201, 21))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift SemiLight")
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_downloadstockdata.setFont(font7)
        self.label_downloadstockdata.setStyleSheet(u"background-color: #89c2d9;\n"
"border-radius: 10px;\n"
"border: 2px solid #61A5C2;")
        self.label_downloadstockdata.setAlignment(Qt.AlignCenter)
        self.pushButton_loadstockdata = QPushButton(self.centralwidget)
        self.pushButton_loadstockdata.setObjectName(u"pushButton_loadstockdata")
        self.pushButton_loadstockdata.setGeometry(QRect(1010, 40, 61, 21))
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
        self.lineEdit.setGeometry(QRect(870, 40, 131, 21))
        font8 = QFont()
        font8.setFamily(u"Bahnschrift SemiLight")
        font8.setPointSize(8)
        self.lineEdit.setFont(font8)
        self.lineEdit.setStyleSheet(u"background-color: #89c2d9;\n"
"border-radius: 5px; \n"
"border:2px solid #61a5c2;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.frame_pageselectors = QFrame(self.centralwidget)
        self.frame_pageselectors.setObjectName(u"frame_pageselectors")
        self.frame_pageselectors.setGeometry(QRect(250, 10, 611, 51))
        self.frame_pageselectors.setFont(font)
        self.frame_pageselectors.setStyleSheet(u"background-color: #89c2d9;\n"
"border-radius:10px;")
        self.frame_pageselectors.setFrameShape(QFrame.StyledPanel)
        self.frame_pageselectors.setFrameShadow(QFrame.Raised)
        self.pushButton_cashflow = QPushButton(self.frame_pageselectors)
        self.pushButton_cashflow.setObjectName(u"pushButton_cashflow")
        self.pushButton_cashflow.setGeometry(QRect(490, 10, 111, 31))
        self.pushButton_cashflow.setFont(font5)
        self.pushButton_cashflow.setStyleSheet(u"QPushButton\n"
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
        self.pushButton_income = QPushButton(self.frame_pageselectors)
        self.pushButton_income.setObjectName(u"pushButton_income")
        self.pushButton_income.setGeometry(QRect(250, 10, 111, 31))
        self.pushButton_income.setFont(font5)
        self.pushButton_income.setStyleSheet(u"QPushButton\n"
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
        self.pushButton_overview.setFont(font5)
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
        self.pushButton_dataview = QPushButton(self.frame_pageselectors)
        self.pushButton_dataview.setObjectName(u"pushButton_dataview")
        self.pushButton_dataview.setGeometry(QRect(130, 10, 111, 31))
        self.pushButton_dataview.setFont(font5)
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
        self.pushButton_balance = QPushButton(self.frame_pageselectors)
        self.pushButton_balance.setObjectName(u"pushButton_balance")
        self.pushButton_balance.setGeometry(QRect(370, 10, 111, 31))
        self.pushButton_balance.setFont(font5)
        self.pushButton_balance.setStyleSheet(u"QPushButton\n"
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stock Analizer Tool", None))
        self.label_company.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_company_data.setText(QCoreApplication.translate("MainWindow", u"Intel Corporation", None))
        self.label_sector.setText(QCoreApplication.translate("MainWindow", u"Sector", None))
        self.label_industry.setText(QCoreApplication.translate("MainWindow", u"Industry", None))
        self.label_marketcap.setText(QCoreApplication.translate("MainWindow", u"Market Cap", None))
        self.label_sector_data.setText(QCoreApplication.translate("MainWindow", u"Technology", None))
        self.label_industry_data.setText(QCoreApplication.translate("MainWindow", u"Semiconductors", None))
        self.label_marketcap_data.setText(QCoreApplication.translate("MainWindow", u"$214,014,001,152", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Buisness Summery / Company Description", None))
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
        self.textBrowser_description_data.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Intel Corporation designs, manufactures, and sells essential technologies for the cloud, smart, and connected devices for retail, industrial, and consumer uses worldwide. The company operates through DCG, IOTG, Mobileye, NSG, PSG, CCG, and All Other segments. It offers platform products, such as central processing units and chipsets, and system-on-chip and multichip packages; and non-platform or adjacent products comprising accelerators, boards and systems, connectivity products, and memory and storage products. The company also provides"
                        " Internet of Things products, including high-performance compute solutions for targeted verticals and embedded applications; and computer vision and machine learning-based sensing, data analysis, localization, mapping, and driving policy technology. It serves original equipment manufacturers, original design manufacturers, and cloud service providers. Intel Corporation has a strategic partnership with MILA to develop and apply advances in artificial intelligence methods for enhancing the search in the space of drugs. The company was founded in 1968 and is headquartered in Santa Clara, California.</p></body></html>", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Stock Analizer Tool", None))
        self.label_companylistheader.setText(QCoreApplication.translate("MainWindow", u"Companies", None))

        __sortingEnabled = self.listWidget_companylist.isSortingEnabled()
        self.listWidget_companylist.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_companylist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"INTC", None));
        ___qlistwidgetitem1 = self.listWidget_companylist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"BTI", None));
        self.listWidget_companylist.setSortingEnabled(__sortingEnabled)

        self.label_companylistsubheader.setText(QCoreApplication.translate("MainWindow", u"Click company to view", None))
        self.label_downloadstockdata.setText(QCoreApplication.translate("MainWindow", u"Download Stock Data", None))
        self.pushButton_loadstockdata.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Ticker Symbol", None))
        self.pushButton_cashflow.setText(QCoreApplication.translate("MainWindow", u"Cashflow", None))
        self.pushButton_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.pushButton_overview.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.pushButton_dataview.setText(QCoreApplication.translate("MainWindow", u"Data View", None))
        self.pushButton_balance.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
    # retranslateUi

