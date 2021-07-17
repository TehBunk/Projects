# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poshtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from backend import value_changed
from backend import RUNNING, SPEED
from backend import FOLLOW_COUNT, clicked_start
from backcall import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 464)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(243, 464))
        MainWindow.setMaximumSize(QtCore.QSize(243, 464))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(243, 464))
        self.centralwidget.setMaximumSize(QtCore.QSize(243, 464))
        self.centralwidget.setObjectName("centralwidget")

        self.setup_content()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_content(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 229, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vlayout_all = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_all.setContentsMargins(0, 0, 0, 0)
        self.vlayout_all.setSpacing(0)
        self.vlayout_all.setObjectName("vlayout_all")
        self.label_searchterm = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_searchterm.setFont(font)
        self.label_searchterm.setObjectName("label_searchterm")
        self.vlayout_all.addWidget(self.label_searchterm)
        self.hlayout_1 = QtWidgets.QHBoxLayout()
        self.hlayout_1.setObjectName("hlayout_1")
        self.lineEdit_searchterm = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.lineEdit_searchterm.setObjectName("lineEdit_searchterm")
        self.hlayout_1.addWidget(self.lineEdit_searchterm)
        self.pushButton_startstop = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.pushButton_startstop.setObjectName("pushButton_startstop")
        self.pushButton_startstop.clicked.connect(lambda: clicked_start(self))
        self.hlayout_1.addWidget(self.pushButton_startstop)
        self.vlayout_all.addLayout(self.hlayout_1)
        self.label_followpermin = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_followpermin.setFont(font)
        self.label_followpermin.setObjectName("label_followpermin")
        self.vlayout_all.addWidget(self.label_followpermin)
        self.hlayout3 = QtWidgets.QHBoxLayout()
        self.hlayout3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hlayout3.setObjectName("hlayout3")
        self.horizontalSlider_speed = QtWidgets.QSlider(
            self.verticalLayoutWidget)
        self.horizontalSlider_speed.setMinimum(1)
        self.horizontalSlider_speed.setMaximum(10)
        self.horizontalSlider_speed.setPageStep(1)
        self.horizontalSlider_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_speed.setInvertedAppearance(False)
        self.horizontalSlider_speed.setInvertedControls(False)
        self.horizontalSlider_speed.setTickInterval(1)
        self.horizontalSlider_speed.setObjectName("horizontalSlider_speed")
        self.horizontalSlider_speed.valueChanged.connect(
            lambda: value_changed(self))
        self.hlayout3.addWidget(self.horizontalSlider_speed)
        self.label_speed = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_speed.setMinimumSize(QtCore.QSize(25, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.hlayout3.addWidget(self.label_speed)
        self.vlayout_all.addLayout(self.hlayout3)
        self.hlayout_2 = QtWidgets.QHBoxLayout()
        self.hlayout_2.setObjectName("hlayout_2")
        self.label_followedusers = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_followedusers.setFont(font)
        self.label_followedusers.setObjectName("label_followedusers")
        self.hlayout_2.addWidget(self.label_followedusers)
        self.lcdNumber_followed = QtWidgets.QLCDNumber(
            self.verticalLayoutWidget)
        self.lcdNumber_followed.setObjectName("lcdNumber_followed")
        self.hlayout_2.addWidget(self.lcdNumber_followed)
        self.vlayout_all.addLayout(self.hlayout_2)
        self.listWidget_followed = QtWidgets.QListWidget(
            self.verticalLayoutWidget)
        self.listWidget_followed.setObjectName("listView_followed")
        self.vlayout_all.addWidget(self.listWidget_followed)
        self.vlayout_all.setStretch(5, 6)
        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PoshBot"))
        self.label_searchterm.setText(_translate("MainWindow", "Search Term"))
        self.pushButton_startstop.setText(_translate("MainWindow", "Start"))
        self.label_followpermin.setText(
            _translate("MainWindow", "Follows Per Minute"))
        self.label_speed.setText(_translate(
            "MainWindow", f"{self.horizontalSlider_speed.value()}"))
        self.label_followedusers.setText(
            _translate("MainWindow", "Followed Users"))


# RUNNING THE PROGRAM
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())