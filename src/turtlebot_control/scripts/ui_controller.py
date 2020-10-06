#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys
from control_gui import Ui_RobotTuning
from PyQt5 import QtWidgets
import threading

isActive = True

def initNode():
    rospy.init_node('control_parameters', anonymous=True)

def messagePublisherThread(ui):
    pub = rospy.Publisher('/control_parameters', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    global isActive
    while not rospy.is_shutdown() and isActive:
        dataString = ui.getParameters()
        rospy.loginfo(dataString)
        pub.publish(dataString)
        rate.sleep()

def main():
    initNode()
    app = QtWidgets.QApplication(sys.argv)
    RobotTuning = QtWidgets.QMainWindow()
    ui = Ui_RobotTuning()
    ui.setupUi(RobotTuning)    
    RobotTuning.show()
    rosThread = threading.Thread(target=messagePublisherThread, args=[ui])
    rosThread.start()
    exitCode = app.exec_()
    global isActive
    isActive = False
    rosThread.join()
    sys.exit(exitCode)

if __name__ == '__main__':
    main()