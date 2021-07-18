# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'poshtest.ui'
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
        MainWindow.resize(243, 464)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(243, 464))
        MainWindow.setMaximumSize(QSize(243, 464))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(243, 464))
        self.centralwidget.setMaximumSize(QSize(243, 464))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 229, 441))
        self.vlayout_all = QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_all.setSpacing(0)
        self.vlayout_all.setObjectName(u"vlayout_all")
        self.vlayout_all.setContentsMargins(0, 0, 0, 0)
        self.label_searchterm = QLabel(self.verticalLayoutWidget)
        self.label_searchterm.setObjectName(u"label_searchterm")
        font = QFont()
        font.setPointSize(16)
        self.label_searchterm.setFont(font)

        self.vlayout_all.addWidget(self.label_searchterm)

        self.hlayout_1 = QHBoxLayout()
        self.hlayout_1.setObjectName(u"hlayout_1")
        self.lineEdit_searchterm = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_searchterm.setObjectName(u"lineEdit_searchterm")

        self.hlayout_1.addWidget(self.lineEdit_searchterm)

        self.pushButton_startstop = QPushButton(self.verticalLayoutWidget)
        self.pushButton_startstop.setObjectName(u"pushButton_startstop")

        self.hlayout_1.addWidget(self.pushButton_startstop)


        self.vlayout_all.addLayout(self.hlayout_1)

        self.label_followpermin = QLabel(self.verticalLayoutWidget)
        self.label_followpermin.setObjectName(u"label_followpermin")
        self.label_followpermin.setFont(font)

        self.vlayout_all.addWidget(self.label_followpermin)

        self.hlayout3 = QHBoxLayout()
        self.hlayout3.setObjectName(u"hlayout3")
        self.hlayout3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSlider_speed = QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_speed.setObjectName(u"horizontalSlider_speed")
        self.horizontalSlider_speed.setMinimum(1)
        self.horizontalSlider_speed.setMaximum(10)
        self.horizontalSlider_speed.setPageStep(1)
        self.horizontalSlider_speed.setOrientation(Qt.Horizontal)
        self.horizontalSlider_speed.setInvertedAppearance(False)
        self.horizontalSlider_speed.setInvertedControls(False)
        self.horizontalSlider_speed.setTickInterval(1)

        self.hlayout3.addWidget(self.horizontalSlider_speed)

        self.label_speed = QLabel(self.verticalLayoutWidget)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setMinimumSize(QSize(25, 0))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.label_speed.setFont(font1)
        self.label_speed.setAlignment(Qt.AlignCenter)

        self.hlayout3.addWidget(self.label_speed)


        self.vlayout_all.addLayout(self.hlayout3)

        self.hlayout_2 = QHBoxLayout()
        self.hlayout_2.setObjectName(u"hlayout_2")
        self.label_followedusers = QLabel(self.verticalLayoutWidget)
        self.label_followedusers.setObjectName(u"label_followedusers")
        self.label_followedusers.setFont(font)

        self.hlayout_2.addWidget(self.label_followedusers)

        self.lcdNumber_followed = QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_followed.setObjectName(u"lcdNumber_followed")

        self.hlayout_2.addWidget(self.lcdNumber_followed)


        self.vlayout_all.addLayout(self.hlayout_2)

        self.listView_followed = QListView(self.verticalLayoutWidget)
        self.listView_followed.setObjectName(u"listView_followed")

        self.vlayout_all.addWidget(self.listView_followed)

        self.vlayout_all.setStretch(5, 6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PoshBot", None))
        self.label_searchterm.setText(QCoreApplication.translate("MainWindow", u"Search Term", None))
        self.pushButton_startstop.setText(QCoreApplication.translate("MainWindow", u"Begin", None))
        self.label_followpermin.setText(QCoreApplication.translate("MainWindow", u"Follows Per Minute", None))
        self.label_speed.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_followedusers.setText(QCoreApplication.translate("MainWindow", u"Followed Users", None))
    # retranslateUi

