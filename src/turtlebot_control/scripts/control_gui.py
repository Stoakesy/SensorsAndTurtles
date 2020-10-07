# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

max_linear_velocity = 0.26
max_angular_velocity = 1.82
max_slowTurnMultiplier = 1
max_hysteresis = 1
max_purePursuit = 90
max_angular = 0.5
max_goalDistance  = 0.5

default_linear_velocity = 0.13
default_angular_velocity = 0.91
default_slowTurnMultiplier = 0.2
default_hysteresis = 0.5
default_purePursuit = 45
default_angular = 0.05
default_goalDistance = 0.25

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

        ##################### INITIAL VALUES #####################
        self.linear_velocity = default_linear_velocity
        self.angular_velocity = default_angular_velocity
        self.slowTurnMultiplier = default_slowTurnMultiplier
        self.hysteresis = default_hysteresis
        self.purePursuit = default_purePursuit
        self.angular = default_angular
        self.goalDistance = default_goalDistance
        self.isActive = 1.0

        ##################### VARIABLES #####################
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

        # Angular Velocity
        self.AV_Label = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.AV_Label.setObjectName("AV_Label")

        self.AVSlider = QtWidgets.QSlider(self.centralwidget)
        self.AVSlider.setGeometry(QtCore.QRect(170, 90, 160, 16))
        self.AVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AVSlider.setObjectName("AVSlider")
        self.AVSlider.valueChanged.connect(self.avChanged)

        self.AngVel = QtWidgets.QLineEdit(self.centralwidget)
        self.AngVel.setGeometry(QtCore.QRect(340, 80, 91, 31))
        self.AngVel.setObjectName("AngVel")
        self.AngVel.returnPressed.connect(self.avTextChanged)

        # Slow Turn Multiplier
        self.AV_Label_2 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_2.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.AV_Label_2.setObjectName("AV_Label_2")

        self.SlowTurnSlider = QtWidgets.QSlider(self.centralwidget)
        self.SlowTurnSlider.setGeometry(QtCore.QRect(170, 130, 160, 16))
        self.SlowTurnSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SlowTurnSlider.setObjectName("SlowTurnSlider")
        self.SlowTurnSlider.valueChanged.connect(self.slowTurnChanged)

        self.SlowTurn = QtWidgets.QLineEdit(self.centralwidget)
        self.SlowTurn.setGeometry(QtCore.QRect(340, 120, 91, 31))
        self.SlowTurn.setObjectName("SlowTurn")
        self.SlowTurn.returnPressed.connect(self.slowTurnTextChanged)

        #Hysterisis
        self.AV_Label_3 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_3.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.AV_Label_3.setObjectName("AV_Label_3")

        self.HysterisisSlider = QtWidgets.QSlider(self.centralwidget)
        self.HysterisisSlider.setGeometry(QtCore.QRect(170, 170, 160, 16))
        self.HysterisisSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HysterisisSlider.setObjectName("HysterisisSlider")
        self.HysterisisSlider.valueChanged.connect(self.hysterisisChanged)

        self.Hysterisis = QtWidgets.QLineEdit(self.centralwidget)
        self.Hysterisis.setGeometry(QtCore.QRect(340, 160, 91, 31))
        self.Hysterisis.setObjectName("Hysterisis")
        self.Hysterisis.returnPressed.connect(self.hysterisisTextChanged)

        #Pure Pursuit
        self.AV_Label_4 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_4.setGeometry(QtCore.QRect(20, 200, 121, 21))
        self.AV_Label_4.setObjectName("AV_Label_4")

        self.PurePursuitSlider = QtWidgets.QSlider(self.centralwidget)
        self.PurePursuitSlider.setGeometry(QtCore.QRect(170, 210, 160, 16))
        self.PurePursuitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PurePursuitSlider.setObjectName("PurePursuitSlider")
        self.PurePursuitSlider.valueChanged.connect(self.purePursuitChanged)

        self.PurePursuit = QtWidgets.QLineEdit(self.centralwidget)
        self.PurePursuit.setGeometry(QtCore.QRect(340, 200, 91, 31))
        self.PurePursuit.setObjectName("PurePursuit")
        self.PurePursuit.returnPressed.connect(self.purePursuitTextChanged)

        #Angular Threshold
        self.AV_Label_5 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_5.setGeometry(QtCore.QRect(20, 240, 141, 21))
        self.AV_Label_5.setObjectName("AV_Label_5")

        self.AngularThresholdSlider = QtWidgets.QSlider(self.centralwidget)
        self.AngularThresholdSlider.setGeometry(QtCore.QRect(170, 250, 160, 16))
        self.AngularThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AngularThresholdSlider.setObjectName("AngularThresholdSlider")
        self.AngularThresholdSlider.valueChanged.connect(self.angularChanged)

        self.AngularThreshold = QtWidgets.QLineEdit(self.centralwidget)
        self.AngularThreshold.setGeometry(QtCore.QRect(340, 240, 91, 31))
        self.AngularThreshold.setObjectName("AngularThreshold")
        self.AngularThreshold.returnPressed.connect(self.angularTextChanged)

        #Goal Distance
        self.AV_Label_6 = QtWidgets.QLabel(self.centralwidget)
        self.AV_Label_6.setGeometry(QtCore.QRect(20, 280, 121, 21))
        self.AV_Label_6.setObjectName("AV_Label_6")

        self.GoalDistanceSlider = QtWidgets.QSlider(self.centralwidget)
        self.GoalDistanceSlider.setGeometry(QtCore.QRect(170, 290, 160, 16))
        self.GoalDistanceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GoalDistanceSlider.setObjectName("GoalDistanceSlider")
        self.GoalDistanceSlider.valueChanged.connect(self.goalDistChanged)

        self.GoalDistance = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalDistance.setGeometry(QtCore.QRect(340, 280, 91, 31))
        self.GoalDistance.setObjectName("GoalDistance")
        self.GoalDistance.returnPressed.connect(self.goalDistTextChanged)

        

        #############################################

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
        self.resetPressed()

        ##################### FUNCTIONS #####################

    def retranslateUi(self, RobotTuning):
        _translate = QtCore.QCoreApplication.translate
        RobotTuning.setWindowTitle(_translate("RobotTuning", "Robot Control"))
        self.Stop.setText(_translate("RobotTuning", "Stop"))
        self.Reset.setText(_translate("RobotTuning", "Reset"))
        self.Resume.setText(_translate("RobotTuning", "Resume"))
        self.AV_Label.setText(_translate("RobotTuning", "Angular Velocity:"))
        self.LV_Label.setText(_translate("RobotTuning", "Linear Velocity:"))
        # self.LinVel.setText(_translate("RobotTuning", f"{default_linear_velocity}"))
        # self.AngVel.setText(_translate("RobotTuning", f"{default_angular_velocity}"))
        # self.SlowTurn.setText(_translate("RobotTuning", f"{default_slowTurnMultiplier}"))
        # self.Hysterisis.setText(_translate("RobotTuning", f"{default_hysteresis}"))
        # self.PurePursuit.setText(_translate("RobotTuning", f"{default_purePursuit}"))
        # self.AngularThreshold.setText(_translate("RobotTuning", f"{default_angular}"))
        # self.GoalDistance.setText(_translate("RobotTuning", f"{default_goalDistance}"))
        self.AV_Label_2.setText(_translate("RobotTuning", "Slow Turn Multiplier:"))
        self.AV_Label_3.setText(_translate("RobotTuning", "Hysterisis:"))
        self.AV_Label_4.setText(_translate("RobotTuning", "Pure Pursuit:"))
        self.AV_Label_5.setText(_translate("RobotTuning", "Angular Threshold:"))
        self.AV_Label_6.setText(_translate("RobotTuning", "Goal Distance:"))

    def resetPressed(self):
        self.LinVel.setText(f"{default_linear_velocity}")
        self.AngVel.setText(f"{default_angular_velocity}")
        self.SlowTurn.setText(f"{default_slowTurnMultiplier}")
        self.Hysterisis.setText(f"{default_hysteresis}")
        self.PurePursuit.setText(f"{default_purePursuit}")
        self.AngularThreshold.setText(f"{default_angular}")
        self.GoalDistance.setText(f"{default_goalDistance}")

        self.lvTextChanged()
        self.avTextChanged()
        self.slowTurnTextChanged()
        self.hysterisisTextChanged()
        self.purePursuitTextChanged()
        self.angularTextChanged()
        self.goalDistTextChanged()

    def stopPressed(self):
        print("Stopped pressed")
        self.isActive = 0.0

    def resumePressed(self):
        print("Resume pressed")
        self.isActive = 1.0

    def mapValue(self, sliderValue, maxValue):
        return maxValue * (sliderValue / 100.0)
    
    def mapToSlider(self, valueText, maxValue):
        try:
            valueFloat = float(valueText)
        except ValueError:
            return False
        return valueFloat * (100.0 / maxValue)
    
    #############SLIDER2BOX####################
    def updateBox(self, box, slider, max_value):
        value = self.mapValue(slider.value(), max_value)
        box.setText("{:.2f}".format(value))
        return value

    def lvChanged(self):
        self.linear_velocity = self.updateBox(self.LinVel, self.LVSlider, max_linear_velocity)
        
    def avChanged(self):
        self.angular_velocity = self.updateBox(self.AngVel, self.AVSlider, max_angular_velocity)

    def slowTurnChanged(self):
        self.slowTurnMultiplier = self.updateBox(self.SlowTurn, self.SlowTurnSlider, max_slowTurnMultiplier)

    def hysterisisChanged(self):
        self.hysteresis = self.updateBox(self.Hysterisis, self.HysterisisSlider, max_hysteresis)

    def purePursuitChanged(self):
        self.purePursuit = self.updateBox(self.PurePursuit, self.PurePursuitSlider, max_purePursuit)

    def angularChanged(self):
        self.angular = self.updateBox(self.AngularThreshold, self.AngularThresholdSlider, max_angular)

    def goalDistChanged(self):
        self.goalDistance = self.updateBox(self.GoalDistance, self.GoalDistanceSlider, max_goalDistance)

    #############BOX2SLIDER####################

    def lvTextChanged(self):
        self.LVSlider.setValue(self.mapToSlider(self.LinVel.text(), max_linear_velocity))

    def avTextChanged(self):
        self.AVSlider.setValue(self.mapToSlider(self.AngVel.text(), max_angular_velocity))

    def slowTurnTextChanged(self):
        self.SlowTurnSlider.setValue(self.mapToSlider(self.SlowTurn.text(), max_slowTurnMultiplier))

    def hysterisisTextChanged(self):
        self.HysterisisSlider.setValue(self.mapToSlider(self.Hysterisis.text(), max_hysteresis))

    def purePursuitTextChanged(self):
        self.PurePursuitSlider.setValue(self.mapToSlider(self.PurePursuit.text(), max_purePursuit))

    def angularTextChanged(self):
        self.AngularThresholdSlider.setValue(self.mapToSlider(self.AngularThreshold.text(), max_angular))

    def goalDistTextChanged(self):
        self.GoalDistanceSlider.setValue(self.mapToSlider(self.GoalDistance.text(), max_goalDistance))
    
    def isStopped(self):
        return not self.isActive

    def getParameters(self):
        return "{0:.4f},{1:.4f},{2:.4f},{3:.4f},{4:.4f},{5:.4f},{6:.4f},{7:.4f}".format(
            self.linear_velocity,
            self.angular_velocity,
            self.slowTurnMultiplier,
            self.hysteresis,
            self.purePursuit,
            self.angular,
            self.goalDistance,
            self.isActive
        )
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotTuning = QtWidgets.QMainWindow()
    ui = Ui_RobotTuning()
    ui.setupUi(RobotTuning)
    RobotTuning.show()
    sys.exit(app.exec_())

