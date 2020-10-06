# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

max_linear_velocity = 0.26

class Ui_RobotTuning(object):
    def setupUi(self, RobotTuning):
        RobotTuning.setObjectName("RobotTuning")
        RobotTuning.resize(453, 472)
        self.centralwidget = QtWidgets.QWidget(RobotTuning)
        self.centralwidget.setObjectName("centralwidget")

        ##################### BUTTONS #####################
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(20, 360, 131, 51))
        self.Stop.setObjectName("Stop")
        self.Stop.clicked.connect(self.stopPressed)

        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(160, 360, 131, 51))
        self.Reset.setObjectName("Reset")
        self.Reset.clicked.connect(self.resetPressed)

        self.Resume = QtWidgets.QPushButton(self.centralwidget)
        self.Resume.setGeometry(QtCore.QRect(300, 360, 131, 51))
        self.Resume.setObjectName("Resume")
        self.Resume.clicked.connect(self.resumePressed)

        ##################### SLIDERS #####################
        # Linear Velocity
        self.LV_Label = QtWidgets.QLabel(self.centralwidget)
        self.LV_Label.setGeometry(QtCore.QRect(20, 40, 111, 21))
        self.LV_Label.setObjectName("LV_Label")

        self.LVSlider = QtWidgets.QSlider(self.centralwidget)
        self.LVSlider.setGeometry(QtCore.QRect(170, 50, 160, 16))
        self.LVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.LVSlider.setObjectName("LVSlider")
        self.LVSlider.valueChanged.connect(self.lvChanged)

        self.LinVel = QtWidgets.QLineEdit(self.centralwidget)
        self.LinVel.setGeometry(QtCore.QRect(340, 40, 91, 31))
        self.LinVel.setObjectName("LinVel")
        self.LinVel.returnPressed.connect(self.lvTextChanged)




        self.AVSlider = QtWidgets.QSlider(self.centralwidget)
        self.AVSlider.setGeometry(QtCore.QRect(170, 90, 160, 16))
        self.AVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AVSlider.setObjectName("AVSlider")

        self.SlowTurnSlider = QtWidgets.QSlider(self.centralwidget)
        self.SlowTurnSlider.setGeometry(QtCore.QRect(170, 130, 160, 16))
        self.SlowTurnSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SlowTurnSlider.setObjectName("SlowTurnSlider")

        self.HysterisisSlider = QtWidgets.QSlider(self.centralwidget)
        self.HysterisisSlider.setGeometry(QtCore.QRect(170, 170, 160, 16))
        self.HysterisisSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HysterisisSlider.setObjectName("HysterisisSlider")
        
        self.PurePursuitSlider = QtWidgets.QSlider(self.centralwidget)
        self.PurePursuitSlider.setGeometry(QtCore.QRect(170, 210, 160, 16))
        self.PurePursuitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PurePursuitSlider.setObjectName("PurePursuitSlider")

        self.AngularThresholdSlider = QtWidgets.QSlider(self.centralwidget)
        self.AngularThresholdSlider.setGeometry(QtCore.QRect(170, 250, 160, 16))
        self.AngularThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AngularThresholdSlider.setObjectName("AngularThresholdSlider")

        self.GoalDistanceSlider = QtWidgets.QSlider(self.centralwidget)
        self.GoalDistanceSlider.setGeometry(QtCore.QRect(170, 290, 160, 16))
        self.GoalDistanceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GoalDistanceSlider.setObjectName("GoalDistanceSlider")

        self.AV_Label = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.AV_Label.setObjectName("AV_Label")


        self.AngVel = QtWidgets.QLineEdit(self.centralwidget)
        self.AngVel.setGeometry(QtCore.QRect(340, 80, 91, 31))
        self.AngVel.setObjectName("AngVel")

        self.SlowTurn = QtWidgets.QLineEdit(self.centralwidget)
        self.SlowTurn.setGeometry(QtCore.QRect(340, 120, 91, 31))
        self.SlowTurn.setObjectName("SlowTurn")

        self.Hysterisis = QtWidgets.QLineEdit(self.centralwidget)
        self.Hysterisis.setGeometry(QtCore.QRect(340, 160, 91, 31))
        self.Hysterisis.setObjectName("Hysterisis")

        self.PurePursuit = QtWidgets.QLineEdit(self.centralwidget)
        self.PurePursuit.setGeometry(QtCore.QRect(340, 200, 91, 31))
        self.PurePursuit.setObjectName("PurePursuit")

        self.AngularThreshold = QtWidgets.QLineEdit(self.centralwidget)
        self.AngularThreshold.setGeometry(QtCore.QRect(340, 240, 91, 31))
        self.AngularThreshold.setObjectName("AngularThreshold")

        self.GoalDistance = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalDistance.setGeometry(QtCore.QRect(340, 280, 91, 31))
        self.GoalDistance.setObjectName("GoalDistance")


        self.AV_Label_2 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_2.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.AV_Label_2.setObjectName("AV_Label_2")

        self.AV_Label_3 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_3.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.AV_Label_3.setObjectName("AV_Label_3")

        self.AV_Label_4 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_4.setGeometry(QtCore.QRect(20, 200, 121, 21))
        self.AV_Label_4.setObjectName("AV_Label_4")

        self.AV_Label_5 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_5.setGeometry(QtCore.QRect(20, 240, 141, 21))
        self.AV_Label_5.setObjectName("AV_Label_5")

        self.AV_Label_6 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_6.setGeometry(QtCore.QRect(20, 280, 121, 21))
        self.AV_Label_6.setObjectName("AV_Label_6")

        RobotTuning.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RobotTuning)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 22))
        self.menubar.setObjectName("menubar")
        RobotTuning.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RobotTuning)
        self.statusbar.setObjectName("statusbar")
        RobotTuning.setStatusBar(self.statusbar)

        self.retranslateUi(RobotTuning)
        QtCore.QMetaObject.connectSlotsByName(RobotTuning)

    def retranslateUi(self, RobotTuning):
        _translate = QtCore.QCoreApplication.translate
        RobotTuning.setWindowTitle(_translate("RobotTuning", "Robot Control"))
        self.Stop.setText(_translate("RobotTuning", "Stop"))
        self.Reset.setText(_translate("RobotTuning", "Reset"))
        self.Resume.setText(_translate("RobotTuning", "Resume"))
        self.AV_Label.setText(_translate("RobotTuning", "Angular Velocity:"))
        self.LV_Label.setText(_translate("RobotTuning", "Linear Velocity:"))
        self.AngVel.setText(_translate("RobotTuning", "0.91"))
        self.SlowTurn.setText(_translate("RobotTuning", "0.2"))
        self.Hysterisis.setText(_translate("RobotTuning", "0.5"))
        self.PurePursuit.setText(_translate("RobotTuning", "45"))
        self.AngularThreshold.setText(_translate("RobotTuning", "0.05"))
        self.GoalDistance.setText(_translate("RobotTuning", "0.25"))
        self.LinVel.setText(_translate("RobotTuning", "0.13"))
        self.AV_Label_2.setText(_translate("RobotTuning", "Slow Turn Multiplier:"))
        self.AV_Label_3.setText(_translate("RobotTuning", "Hysterisis:"))
        self.AV_Label_4.setText(_translate("RobotTuning", "Pure Pursuit:"))
        self.AV_Label_5.setText(_translate("RobotTuning", "Angular Threshold:"))
        self.AV_Label_6.setText(_translate("RobotTuning", "Goal Distance:"))

    def stopPressed(self):
        print("Stopped pressed")

    def resetPressed(self):
        print("Reset pressed")

    def resumePressed(self):
        print("Resume pressed")

    def mapValue(self, sliderValue, maxValue):
        return maxValue * (sliderValue / 100.0)
    
    def mapToSlider(self, valueText, maxValue):
        try:
            valueFloat = float(valueText)
        except ValueError:
            return False
        return valueFloat * (100.0 / maxValue)

    def lvChanged(self):
        value = self.mapValue(self.LVSlider.value(), max_linear_velocity)
        self.LinVel.setText("{:.2f}".format(value))

    def lvTextChanged(self):
        self.LVSlider.setValue(self.mapToSlider(self.LinVel.text(), max_linear_velocity))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotTuning = QtWidgets.QMainWindow()
    ui = Ui_RobotTuning()
    ui.setupUi(RobotTuning)
    RobotTuning.show()
    sys.exit(app.exec_())

