#include "ros/ros.h"
#include <vector>
#include <iostream>

// #define Image_X = ???;
// #define Image_Y = ???;
// #define Image_Z = ???;



using namespace std;

class Turtlebot{
    public:
    Turtlebot(ros::NodeHandle nh);
    ~Turtlebot();

    //DriveControl();

    void test();

    private:
    double Current_X, Current_Y, Current_Z;

}

void Turtlebot::test()
{
    geometry_msgs::twist test;

    test.linear.x = 0.01;
    test.angular.z = 0.5;

    cmd_vel_pub_.publish(test);
}


int main(int argc, char **argv)
{
      ros::init(argc, argv, "Turtlebot_follow");

      ros::NodeHandle nh;

      //ros::Subscriber sub = nh.subscribe("camera_data", 1000, camera_data);

      cmd_vel_pub_ = nh_.advertise<geometry_msgs::twist>("/tb1/cmd_vel",1);

      ros::spin();


      return 0;

}