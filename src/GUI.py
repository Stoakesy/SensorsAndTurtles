# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RobotTuning(object):
    def setupUi(self, RobotTuning):
        RobotTuning.setObjectName("RobotTuning")
        RobotTuning.resize(456, 425)
        self.centralwidget = QtWidgets.QWidget(RobotTuning)
        self.centralwidget.setObjectName("centralwidget")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(20, 330, 131, 51))
        self.Stop.setObjectName("Stop")
        self.AV_Slider = QtWidgets.QSlider(self.centralwidget)
        self.AV_Slider.setGeometry(QtCore.QRect(140, 60, 160, 16))
        self.AV_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.AV_Slider.setObjectName("AV_Slider")
        self.AV_Slider.setMinimum(0)
        self.AV_Slider.setMaximum(100)
        self.AV_Slider.setValue(0)
        self.LV_Slider = QtWidgets.QSlider(self.centralwidget)
        self.LV_Slider.setGeometry(QtCore.QRect(140, 100, 160, 16))
        self.LV_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.LV_Slider.setObjectName("LV_Slider")
        self.LV_Slider.setMinimum(0)
        self.LV_Slider.setMaximum(100)
        self.LV_Slider.setValue(50)
        self.LV_Slider.valueChanged.connect
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(140, 140, 160, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(140, 180, 160, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(140, 220, 160, 16))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(140, 260, 160, 16))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(160, 330, 131, 51))
        self.Reset.setObjectName("Reset")
        self.Resume = QtWidgets.QPushButton(self.centralwidget)
        self.Resume.setGeometry(QtCore.QRect(300, 330, 131, 51))
        self.Resume.setObjectName("Resume")
        self.AV_Label = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label.setGeometry(QtCore.QRect(20, 50, 121, 21))
        self.AV_Label.setObjectName("AV_Label")
        self.LV_Label = QtWidgets.QLabel(self.centralwidget)
        self.LV_Label.setGeometry(QtCore.QRect(20, 90, 111, 21))
        self.LV_Label.setObjectName("LV_Label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 50, 41, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 90, 41, 31))
        self.lineEdit_2.setObjectName("lineEdit_2") 
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 130, 41, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 170, 41, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 210, 41, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 250, 41, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        RobotTuning.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RobotTuning)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 22))
        self.menubar.setObjectName("menubar")
        RobotTuning.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RobotTuning)
        self.statusbar.setObjectName("statusbar")
        RobotTuning.setStatusBar(self.statusbar)

        self.retranslateUi(RobotTuning)
        QtCore.QMetaObject.connectSlotsByName(RobotTuning)

    def retranslateUi(self, RobotTuning):
        _translate = QtCore.QCoreApplication.translate
        RobotTuning.setWindowTitle(_translate("RobotTuning", "MainWindow"))
        self.Stop.setText(_translate("RobotTuning", "Stop"))
        self.Reset.setText(_translate("RobotTuning", "Reset"))
        self.Resume.setText(_translate("RobotTuning", "Resume"))
        self.AV_Label.setText(_translate("RobotTuning", "Angular Velocity:"))
        self.LV_Label.setText(_translate("RobotTuning", "Linear Velocity:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotTuning = QtWidgets.QMainWindow()
    ui = Ui_RobotTuning()
    ui.setupUi(RobotTuning)
    RobotTuning.show()
    sys.exit(app.exec_())

