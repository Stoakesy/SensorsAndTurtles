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
  it_(nh),
  robot_stopped_(true),
  use_pure_pursuit_(use_pure_pursuit),
  next_goal_(new Goal())
{
  // Initialise publishers and subscribers
  odom_sub_ = nh_.subscribe("robot_0/odom", 1000, &Control::odomCallback,this);
  path_sub_ = nh_.subscribe("robot_0/target_pose", 10, &Control::pathCallback,this);
  velocity_pub_ = nh_.advertise<geometry_msgs::Twist>("robot_0/cmd_vel", 1);

  ros::NodeHandle pn("~");
}

Control::~Control()
{
  
}

void Control::poseCallback(const geometry_msgs::PoseArrayConstPtr & msg)
{
  // Get the array of poses for the robot to follow
  ROS_INFO("New path received");
  ROS_INFO_STREAM("Received path has:" << msg->poses.size() << "elements");

  // Add the series of poses received from msg into the map data class object
  path_planning_.clearGoals();
  for (unsigned int i=0;i<msg->poses.size();i++)
  {
    path_planning_.addGoal(msg->poses.at(i));
  }

  if (optimise_path_)
  {
    geometry_msgs::Pose current_pose;
    robot_control_.getLatestData(current_pose);
    path_planning_.optimisePath(current_pose);
  }
}

void Control::odomCallback(const nav_msgs::OdometryConstPtr& msg)
{
  // Get the latest robot pose from the odometry message and add it to the robot pose data buffer
  geometry_msgs::Pose current_pose=msg->pose.pose;
  robot_control_.addData(current_pose);
}

void Control::mainThread(void)
{
  /**
  * The below loop runs until ros is shutdown
  */

  geometry_msgs::Twist velocity;
  geometry_msgs::Pose current_pose;

  while (ros::ok())
  {
    robot_control_.getLatestData(current_pose);
    if (path_planning_.getNextGoal(next_goal_, current_pose, velocity))
    {
      bool use_pure_pursuit = (use_pure_pursuit_ && (next_goal_->command != DRIVE_STRAIGHT));
      if (robot_control_.calculateVelocity(velocity, next_goal_->pose, use_pure_pursuit))
      {
        velocity_pub_.publish(velocity);
        robot_stopped_ = false;
      }
    }
    else
    {
      if (!robot_stopped_)
      {
        robot_stopped_ = true;
        velocity.angular.z = 0;
        velocity.linear.x = 0;
        velocity_pub_.publish(velocity);
        
        // Check if the robot completed the path or not
        Goal goal;
        bool goal_located = false;
        bool path_complete = false;
        path_planning_.getGoal(path_planning_.goalCount() - 1, goal);
        if (goal.state == PAST_GOAL)
        {
          path_complete = true;
        }
        else
        {
          for (int i = 0; i < path_planning_.goalCount(); i++)
          {
            path_planning_.getGoal(i, goal);
            if (goal.state == PAST_GOAL)
            {
              goal_located = true;
              break;
            }
          }
        }
        if (path_complete)
        {
          ROS_INFO("Path completed");
        }
        else if (goal_located)
        {
          ROS_INFO("Remaining path is not possible");
        }
        else
        {
          ROS_INFO("Path is not possible at all");
        }
      }
    }

    // This delay slows the loop down for the sake of readability
    std::this_thread::sleep_for (std::chrono::milliseconds(MAIN_THREAD_DELAY_MS));
  }
  std::cout << __func__ << " thread terminated" << std::endl;
}