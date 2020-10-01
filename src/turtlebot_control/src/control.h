/*! @file
 *
 *  @brief File the main control threads used in this program:
 *
 *  This file contains the control threads used in this program to handle passing data to
 *  and from this ROS node.
 *
 *  @author Jacob Vartanian
 *  @date 2020-09-25
 */

#ifndef CONTROL_H
#define CONTROL_H

#include "ros/ros.h"
#include "tf/transform_datatypes.h"

//ROS Message Types
#include "nav_msgs/Odometry.h"
#include "geometry_msgs/PoseArray.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Pose.h"
#include "geometry_msgs/Twist.h"

#include <sstream>
#include <iostream>
#include <string>

#include <thread>
#include <chrono>
#include <deque>
#include <mutex>
#include <random>
#include <atomic>

#include "path_following.h"

#define MAIN_THREAD_DELAY_MS 150

class Control
{
  public:
    /**
     * @brief Constructor for Control class
     * 
     * @param nh ROS node handler
     * @param use_pure_pursuit Flag indicating if pure pursuit should be used or not
    */
    Control(ros::NodeHandle nh, bool use_pure_pursuit);

    /**
     * @brief Destructor for Control class
    */
    ~Control();

    /**
     * @brief Callback function to handle receiving a new pose message
     * 
     * @param msg Refernce to the message received
    */
    void poseCallback(const geometry_msgs::Pose & msg);

    /**
     * @brief Callback function to handle receiving a new parameters message
     * 
     * @param msg Refernce to the message received
    */
    void paramCallback(const std_msgs::String::ConstPtr & msg);

    /**
     * @brief Thread containing the main algorithm used in this program
    */
    void mainThread(void);

  private:
    ros::NodeHandle nh_;
    
    ros::Subscriber odom_sub_;
    ros::Subscriber pose_sub_;
    ros::Subscriber param_sub_;
    ros::Publisher velocity_pub_;

    PathFollowing robot_control_;
    
    bool robot_stopped_;
    bool use_pure_pursuit_;
};

#endif // CONTROL_H