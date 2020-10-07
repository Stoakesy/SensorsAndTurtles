# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

max_linear_velocity = 0.26
max_angular_velocity = 1.82
max_slow_turn_multiplier = 1
max_pursuit_angle = 90
max_stop_distance  = 0.5
max_reserved_a = 1
max_reserved_b = 1

default_linear_velocity = 0.13
default_angular_velocity = 0.91
default_slow_turn_multiplier = 0.2
default_pursuit_angle = 45
default_stop_distance = 0.25
default_reserved_a = 0.5
default_reserved_b = 0.5

class RobotTuningUI(object):
    def setupUi(self, RobotTuning):
        RobotTuning.setObjectName("RobotTuning")
        RobotTuning.resize(453, 472)
        self.centralwidget = QtWidgets.QWidget(RobotTuning)
        self.centralwidget.setObjectName("centralwidget")

        ##################### BUTTONS #####################
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(20, 360, 131, 51))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_stop.clicked.connect(self.stop_pressed)

        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(160, 360, 131, 51))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.clicked.connect(self.reset_pressed)

        self.btn_resume = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resume.setGeometry(QtCore.QRect(300, 360, 131, 51))
        self.btn_resume.setObjectName("btn_resume")
        self.btn_resume.clicked.connect(self.resume_pressed)

        ##################### INITIAL VALUES #####################
        self.linear_velocity = default_linear_velocity
        self.angular_velocity = default_angular_velocity
        self.slow_turn_multiplier = default_slow_turn_multiplier
        self.pursuit_angle = default_pursuit_angle
        self.stop_distance = default_stop_distance
        self.reserved_a = default_reserved_a
        self.reserved_b = default_reserved_b
        self.is_active = 1.0

        ##################### VARIABLES #####################
        # Linear Velocity
        self.lbl_linear_velocity = QtWidgets.QLabel(self.centralwidget)
        self.lbl_linear_velocity.setGeometry(QtCore.QRect(20, 40, 111, 21))
        self.lbl_linear_velocity.setObjectName("lbl_linear_velocity")

        self.sld_linear_velocity = QtWidgets.QSlider(self.centralwidget)
        self.sld_linear_velocity.setGeometry(QtCore.QRect(170, 50, 160, 16))
        self.sld_linear_velocity.setOrientation(QtCore.Qt.Horizontal)
        self.sld_linear_velocity.setObjectName("sld_linear_velocity")
        self.sld_linear_velocity.valueChanged.connect(self.linear_velocity_slider_changed)

        self.txt_linear_velocity = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_linear_velocity.setGeometry(QtCore.QRect(340, 40, 91, 31))
        self.txt_linear_velocity.setObjectName("txt_linear_velocity")
        self.txt_linear_velocity.returnPressed.connect(self.linear_velocity_text_changed)

        # Angular Velocity
        self.lbl_angular_velocity = QtWidgets.QLabel(self.centralwidget)
        self.lbl_angular_velocity.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.lbl_angular_velocity.setObjectName("lbl_angular_velocity")

        self.sld_angular_velocity = QtWidgets.QSlider(self.centralwidget)
        self.sld_angular_velocity.setGeometry(QtCore.QRect(170, 90, 160, 16))
        self.sld_angular_velocity.setOrientation(QtCore.Qt.Horizontal)
        self.sld_angular_velocity.setObjectName("sld_angular_velocity")
        self.sld_angular_velocity.valueChanged.connect(self.angular_velocity_slider_changed)

        self.txt_angular_velocity = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_angular_velocity.setGeometry(QtCore.QRect(340, 80, 91, 31))
        self.txt_angular_velocity.setObjectName("txt_angular_velocity")
        self.txt_angular_velocity.returnPressed.connect(self.angular_velocity_text_changed)

        # Slow Turn Multiplier
        self.lbl_slow_turn_multiplier = QtWidgets.QLabel(self.centralwidget)
        self.lbl_slow_turn_multiplier.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.lbl_slow_turn_multiplier.setObjectName("lbl_slow_turn_multiplier")

        self.sld_slow_turn_multiplier = QtWidgets.QSlider(self.centralwidget)
        self.sld_slow_turn_multiplier.setGeometry(QtCore.QRect(170, 130, 160, 16))
        self.sld_slow_turn_multiplier.setOrientation(QtCore.Qt.Horizontal)
        self.sld_slow_turn_multiplier.setObjectName("sld_slow_turn_multiplier")
        self.sld_slow_turn_multiplier.valueChanged.connect(self.slow_turn_multiplier_slider_changed)

        self.txt_slow_turn_multiplier = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_slow_turn_multiplier.setGeometry(QtCore.QRect(340, 120, 91, 31))
        self.txt_slow_turn_multiplier.setObjectName("txt_slow_turn_multiplier")
        self.txt_slow_turn_multiplier.returnPressed.connect(self.slow_turn_multiplier_text_changed)

        # Pursuit Angle Threshold
        self.lbl_pursuit_angle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pursuit_angle.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.lbl_pursuit_angle.setObjectName("lbl_pursuit_angle")

        self.sld_pursuit_angle = QtWidgets.QSlider(self.centralwidget)
        self.sld_pursuit_angle.setGeometry(QtCore.QRect(170, 170, 160, 16))
        self.sld_pursuit_angle.setOrientation(QtCore.Qt.Horizontal)
        self.sld_pursuit_angle.setObjectName("sld_pursuit_angle")
        self.sld_pursuit_angle.valueChanged.connect(self.pursuit_angle_slider_changed)

        self.txt_pursuit_angle = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pursuit_angle.setGeometry(QtCore.QRect(340, 160, 91, 31))
        self.txt_pursuit_angle.setObjectName("txt_pursuit_angle")
        self.txt_pursuit_angle.returnPressed.connect(self.pursuit_angle_text_changed)

        # Stopping Distance
        self.lbl_stop_distance = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stop_distance.setGeometry(QtCore.QRect(20, 200, 121, 21))
        self.lbl_stop_distance.setObjectName("lbl_stop_distance")

        self.sld_stop_distance = QtWidgets.QSlider(self.centralwidget)
        self.sld_stop_distance.setGeometry(QtCore.QRect(170, 210, 160, 16))
        self.sld_stop_distance.setOrientation(QtCore.Qt.Horizontal)
        self.sld_stop_distance.setObjectName("sld_stop_distance")
        self.sld_stop_distance.valueChanged.connect(self.stop_distance_slider_changed)

        self.txt_stop_distance = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_stop_distance.setGeometry(QtCore.QRect(340, 200, 91, 31))
        self.txt_stop_distance.setObjectName("txt_stop_distance")
        self.txt_stop_distance.returnPressed.connect(self.stop_distance_text_changed)

        # Reserved A
        self.lbl_reserved_a = QtWidgets.QLabel(self.centralwidget)
        self.lbl_reserved_a.setGeometry(QtCore.QRect(20, 240, 141, 21))
        self.lbl_reserved_a.setObjectName("lbl_reserved_a")

        self.sld_reserved_a = QtWidgets.QSlider(self.centralwidget)
        self.sld_reserved_a.setGeometry(QtCore.QRect(170, 250, 160, 16))
        self.sld_reserved_a.setOrientation(QtCore.Qt.Horizontal)
        self.sld_reserved_a.setObjectName("sld_reserved_a")
        self.sld_reserved_a.valueChanged.connect(self.reserved_a_slider_changed)

        self.txt_reserved_a = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_reserved_a.setGeometry(QtCore.QRect(340, 240, 91, 31))
        self.txt_reserved_a.setObjectName("txt_reserved_a")
        self.txt_reserved_a.returnPressed.connect(self.reserved_a_text_changed)

        # Reserved B
        self.lbl_reserved_b = QtWidgets.QLabel(self.centralwidget)
        self.lbl_reserved_b.setGeometry(QtCore.QRect(20, 280, 121, 21))
        self.lbl_reserved_b.setObjectName("lbl_reserved_b")

        self.sld_reserved_b = QtWidgets.QSlider(self.centralwidget)
        self.sld_reserved_b.setGeometry(QtCore.QRect(170, 290, 160, 16))
        self.sld_reserved_b.setOrientation(QtCore.Qt.Horizontal)
        self.sld_reserved_b.setObjectName("sld_reserved_b")
        self.sld_reserved_b.valueChanged.connect(self.reserved_b_slider_changed)

        self.txt_reserved_b = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_reserved_b.setGeometry(QtCore.QRect(340, 280, 91, 31))
        self.txt_reserved_b.setObjectName("txt_reserved_b")
        self.txt_reserved_b.returnPressed.connect(self.reserved_b_text_changed)

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
        self.reset_pressed()

        ##################### FUNCTIONS #####################

    def retranslateUi(self, RobotTuning):
        _translate = QtCore.QCoreApplication.translate
        RobotTuning.setWindowTitle(_translate("RobotTuning", "Robot Control"))
        self.btn_stop.setText(_translate("RobotTuning", "Stop"))
        self.btn_reset.setText(_translate("RobotTuning", "Reset"))
        self.btn_resume.setText(_translate("RobotTuning", "Resume"))
        self.lbl_linear_velocity.setText(_translate("RobotTuning", "Linear Velocity:"))
        self.lbl_angular_velocity.setText(_translate("RobotTuning", "Angular Velocity:"))
        self.lbl_slow_turn_multiplier.setText(_translate("RobotTuning", "Slow Turn Multiplier:"))
        self.lbl_pursuit_angle.setText(_translate("RobotTuning", "Pursuit Angle:"))
        self.lbl_stop_distance.setText(_translate("RobotTuning", "Stop Distance:"))
        self.lbl_reserved_a.setText(_translate("RobotTuning", "RESERVED"))
        self.lbl_reserved_b.setText(_translate("RobotTuning", "RESERVED"))

    def reset_pressed(self):
        self.txt_linear_velocity.setText(f"{default_linear_velocity}")
        self.txt_angular_velocity.setText(f"{default_angular_velocity}")
        self.txt_slow_turn_multiplier.setText(f"{default_slow_turn_multiplier}")
        self.txt_pursuit_angle.setText(f"{default_pursuit_angle}")
        self.txt_stop_distance.setText(f"{default_stop_distance}")
        self.txt_reserved_a.setText(f"{default_reserved_a}")
        self.txt_reserved_b.setText(f"{default_reserved_b}")

        self.linear_velocity_text_changed()
        self.angular_velocity_text_changed()
        self.slow_turn_multiplier_text_changed()
        self.pursuit_angle_text_changed()
        self.stop_distance_text_changed()
        self.reserved_a_text_changed()
        self.reserved_b_text_changed()

    def stop_pressed(self):
        print("Stopped pressed")
        self.is_active = 0.0

    def resume_pressed(self):
        print("Resume pressed")
        self.is_active = 1.0

    def map_value(self, slider_value, max_value):
        return max_value * (slider_value / 100.0)
    
    def map_to_slider(self, value_text, max_value):
        try:
            value_float = float(value_text)
        except ValueError:
            return False
        return value_float * (100.0 / max_value)
    
    #############SLIDER2BOX####################
    def update_box(self, box, slider, max_value):
        value = self.map_value(slider.value(), max_value)
        box.setText("{:.2f}".format(value))
        return value

    def linear_velocity_slider_changed(self):
        self.linear_velocity = self.update_box(self.txt_linear_velocity, self.sld_linear_velocity, max_linear_velocity)
        
    def angular_velocity_slider_changed(self):
        self.angular_velocity = self.update_box(self.txt_angular_velocity, self.sld_angular_velocity, max_angular_velocity)

    def slow_turn_multiplier_slider_changed(self):
        self.slow_turn_multiplier = self.update_box(self.txt_slow_turn_multiplier, self.sld_slow_turn_multiplier, max_slow_turn_multiplier)

    def pursuit_angle_slider_changed(self):
        self.pursuit_angle = self.update_box(self.txt_pursuit_angle, self.sld_pursuit_angle, max_pursuit_angle)

    def stop_distance_slider_changed(self):
        self.stop_distance = self.update_box(self.txt_stop_distance, self.sld_stop_distance, max_stop_distance)

    def reserved_a_slider_changed(self):
        self.reserved_a = self.update_box(self.txt_reserved_a, self.sld_reserved_a, max_reserved_a)

    def reserved_b_slider_changed(self):
        self.reserved_b = self.update_box(self.txt_reserved_b, self.sld_reserved_b, max_reserved_b)

    #############BOX2SLIDER####################

    def linear_velocity_text_changed(self):
        self.sld_linear_velocity.setValue(self.map_to_slider(self.txt_linear_velocity.text(), max_linear_velocity))

    def angular_velocity_text_changed(self):
        self.sld_angular_velocity.setValue(self.map_to_slider(self.txt_angular_velocity.text(), max_angular_velocity))

    def slow_turn_multiplier_text_changed(self):
        self.sld_slow_turn_multiplier.setValue(self.map_to_slider(self.txt_slow_turn_multiplier.text(), max_slow_turn_multiplier))

    def pursuit_angle_text_changed(self):
        self.sld_pursuit_angle.setValue(self.map_to_slider(self.txt_pursuit_angle.text(), max_pursuit_angle))

    def stop_distance_text_changed(self):
        self.sld_stop_distance.setValue(self.map_to_slider(self.txt_stop_distance.text(), max_stop_distance))

    def reserved_a_text_changed(self):
        self.sld_reserved_a.setValue(self.map_to_slider(self.txt_reserved_a.text(), max_reserved_a))

    def reserved_b_text_changed(self):
        self.sld_reserved_b.setValue(self.map_to_slider(self.txt_reserved_b.text(), max_reserved_b))
    
    def is_stopped(self):
        return not self.is_active

    def get_parameters(self):
        return "{0:.4f},{1:.4f},{2:.4f},{3:.4f},{4:.4f},{5:.4f},{6:.4f},{7:.4f}".format(
            self.linear_velocity,
            self.angular_velocity,
            self.slow_turn_multiplier,
            self.pursuit_angle,
            self.stop_distance,
            self.reserved_a,
            self.reserved_b,
            self.is_active
        )
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    robot_tuning = QtWidgets.QMainWindow()
    ui = RobotTuningUI()
    ui.setupUi(robot_tuning)
    robot_tuning.show()
    sys.exit(app.exec_())
