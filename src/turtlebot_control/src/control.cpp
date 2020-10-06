/*! @file
 *
 *  @brief File containing the main control threads used in this program:
 *
 *  This file contains the control threads used in this program to handle passing data to
 *  and from this ROS node.
 *
 *  @author Jacob Vartanian
 *  @date 2020-09-25
 */

/*!
 * @addtogroup Control_module Control module documentation
 * @{
 */

#include "control.h"

Control::Control(ros::NodeHandle nh, bool use_pure_pursuit):
  nh_(nh),
  robot_stopped_(true),
  use_pure_pursuit_(use_pure_pursuit)
{
  // Initialise publishers and subscribers
  pose_sub_ = nh_.subscribe("target_pose", 10, &Control::poseCallback,this);
  param_sub_ = nh_.subscribe("control_parameters", 10, &Control::paramCallback,this);
  velocity_pub_ = nh_.advertise<geometry_msgs::Twist>("cmd_vel", 1);
  ros::NodeHandle pn("~");
}

Control::~Control()
{
  
}

void Control::poseCallback(const geometry_msgs::Pose & msg)
{
  // Get the pose for the robot to drive to
  // ROS_INFO("New pose received");
  geometry_msgs::Pose target_pose = msg;
  robot_control_.setTargetPose(target_pose);
}

void Control::paramCallback(const std_msgs::String::ConstPtr & msg)
{
  // Get the pose for the robot to drive to
  std::string parameters = msg->data.c_str();
  robot_control_.updateParameters(parameters);
}

void Control::mainThread(void)
{
  /**
  * The below loop runs until ros is shutdown
  */

  geometry_msgs::Twist velocity;

  while (ros::ok())
  {
    if (robot_control_.calculateVelocity(velocity, use_pure_pursuit_, use_p_controller_))
    {
      std::cout << "Final linear velocity " << velocity.linear.x << " m/s" << std::endl;
      std::cout << "Final angular velocity " << velocity.angular.z << " rad/s" << std::endl;
      velocity_pub_.publish(velocity);
      robot_stopped_ = false;
    }
    else
    {
      std::cout << "VELOCITY ERROR" << std::endl << std::endl;
    }
    // This delay slows the loop down for the sake of readability
    std::this_thread::sleep_for (std::chrono::milliseconds(MAIN_THREAD_DELAY_MS));
  }
  std::cout << __func__ << " thread terminated" << std::endl;
}