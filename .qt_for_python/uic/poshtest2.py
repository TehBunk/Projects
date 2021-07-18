# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'poshtest2.ui'
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
        MainWindow.resize(522, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_email = QLineEdit(self.centralwidget)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(275, 10, 161, 21))
        self.pushButton_startstop = QPushButton(self.centralwidget)
        self.pushButton_startstop.setObjectName(u"pushButton_startstop")
        self.pushButton_startstop.setGeometry(QRect(440, 40, 75, 23))
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(210, 10, 71, 25))
        font = QFont()
        font.setPointSize(16)
        self.label_email.setFont(font)
        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(275, 40, 161, 21))
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(173, 40, 101, 25))
        self.label_password.setFont(font)
        self.checkBox_savelogin = QCheckBox(self.centralwidget)
        self.checkBox_savelogin.setObjectName(u"checkBox_savelogin")
        self.checkBox_savelogin.setGeometry(QRect(440, 10, 81, 17))
        self.doubleSpinBox_speed = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_speed.setObjectName(u"doubleSpinBox_speed")
        self.doubleSpinBox_speed.setGeometry(QRect(170, 100, 171, 20))
        self.spinBox_followamount = QSpinBox(self.centralwidget)
        self.spinBox_followamount.setObjectName(u"spinBox_followamount")
        self.spinBox_followamount.setGeometry(QRect(170, 130, 170, 20))
        self.label_followedusers = QLabel(self.centralwidget)
        self.label_followedusers.setObjectName(u"label_followedusers")
        self.label_followedusers.setGeometry(QRect(90, 100, 71, 25))
        self.label_followedusers.setFont(font)
        self.label_followedusers_2 = QLabel(self.centralwidget)
        self.label_followedusers_2.setObjectName(u"label_followedusers_2")
        self.label_followedusers_2.setGeometry(QRect(10, 130, 221, 25))
        self.label_followedusers_2.setFont(font)
        self.label_followedusers_3 = QLabel(self.centralwidget)
        self.label_followedusers_3.setObjectName(u"label_followedusers_3")
        self.label_followedusers_3.setGeometry(QRect(370, 100, 151, 25))
        self.label_followedusers_3.setFont(font)
        self.lcdNumber_followed = QLCDNumber(self.centralwidget)
        self.lcdNumber_followed.setObjectName(u"lcdNumber_followed")
        self.lcdNumber_followed.setGeometry(QRect(370, 130, 141, 21))
        self.listView_followed = QListView(self.centralwidget)
        self.listView_followed.setObjectName(u"listView_followed")
        self.listView_followed.setGeometry(QRect(10, 160, 501, 341))
        self.label_description = QLabel(self.centralwidget)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 514, 501, 121))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_description.setFont(font1)
        self.label_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_licence = QLabel(self.centralwidget)
        self.label_licence.setObjectName(u"label_licence")
        self.label_licence.setGeometry(QRect(350, 580, 121, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_licence.setFont(font2)
        self.dateTimeEdit_expiration = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_expiration.setObjectName(u"dateTimeEdit_expiration")
        self.dateTimeEdit_expiration.setGeometry(QRect(460, 580, 51, 22))
        self.dateTimeEdit_expiration.setReadOnly(True)
        self.dateTimeEdit_expiration.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.checkBox_randomizespeed = QCheckBox(self.centralwidget)
        self.checkBox_randomizespeed.setObjectName(u"checkBox_randomizespeed")
        self.checkBox_randomizespeed.setGeometry(QRect(10, 100, 70, 31))
        self.label_searchterm_5 = QLabel(self.centralwidget)
        self.label_searchterm_5.setObjectName(u"label_searchterm_5")
        self.label_searchterm_5.setGeometry(QRect(15, 70, 251, 25))
        self.label_searchterm_5.setFont(font)
        self.label_searchterm_5.setStyleSheet(u"")
        self.lineEdit_searchterm_3 = QLineEdit(self.centralwidget)
        self.lineEdit_searchterm_3.setObjectName(u"lineEdit_searchterm_3")
        self.lineEdit_searchterm_3.setGeometry(QRect(275, 70, 161, 21))
        self.frame_logo = QFrame(self.centralwidget)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setGeometry(QRect(10, 10, 151, 51))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_startstop.setText(QCoreApplication.translate("MainWindow", u"Begin", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.checkBox_savelogin.setText(QCoreApplication.translate("MainWindow", u"Save Login?", None))
        self.label_followedusers.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        self.label_followedusers_2.setText(QCoreApplication.translate("MainWindow", u"Follow Amount:", None))
        self.label_followedusers_3.setText(QCoreApplication.translate("MainWindow", u"Followed Users", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Recommended speed: .08\n"
"Leave follow amount 0 for infinite follows\n"
"Buy me here: link", None))
        self.label_licence.setText(QCoreApplication.translate("MainWindow", u"Licence Valid Until:", None))
        self.dateTimeEdit_expiration.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.checkBox_randomizespeed.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.label_searchterm_5.setText(QCoreApplication.translate("MainWindow", u"Profile Link / Search Term:", None))
    # retranslateUi

