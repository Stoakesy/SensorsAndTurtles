import rospy
from std_msgs.msg import String
import sys
from GUI2 import Ui_RobotTuning
from PyQt5 import QtWidgets
import threading

isActive = True

def initNode():
    rospy.init_node('control_parameters_node', anonymous=True)

def messagePublisherThread():
    pub = rospy.Publisher('/control_parameters', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    global isActive
    while not rospy.is_shutdown() and isActive:
        dataString = "1,2,3,4,5,6,7,8"
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
    rosThread = threading.Thread(target=messagePublisherThread)
    rosThread.start()
    exitCode = app.exec_()
    global isActive
    isActive = False
    rosThread.join()
    sys.exit(exitCode)

if __name__ == '__main__':
    main()