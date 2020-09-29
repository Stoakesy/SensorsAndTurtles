/*! @file
 *
 *  @brief Class containing the main algorithms used to calculate the robot's actions:
 *
 *  This class contains functions that will be used to determine the required velocity
 *  of the robot to reach the next path.
 *
 *  @author Jacob Vartanian
 *  @date 2020-09-25
 */

/*!
 * @addtogroup PathFollowing_module Path following module documentation
 * @{
 */

#include "path_following.h"

PathFollowing::PathFollowing():
  hysteresis_factor_(0)
{
  
}

bool PathFollowing::setTargetPose(geometry_msgs::Pose target_pose)
{
  target_pose_.mtx.lock();
  target_pose_.pose = target_pose;
  target_pose_.mtx.unlock();
  return true;
}

bool PathFollowing::getZeroVelocity(geometry_msgs::Twist &velocity)
{
  velocity.linear.x = 0;
  velocity.linear.y = 0;
  velocity.linear.z = 0;
  velocity.angular.x = 0;
  velocity.angular.y = 0;
  velocity.angular.z = 0;
  return true;
}

bool PathFollowing::calculateVelocity(geometry_msgs::Twist &velocity, bool use_pure_pursuit)
{
  target_pose_.mtx.lock();
  geometry_msgs::Pose goal = target_pose_.pose;
  target_pose_.mtx.unlock();
  bool success = true;
  double desired_heading = (atan2(goal.position.y, goal.position.x));

  TurnDirection_t direction = STRAIGHT;

  // Reset velocity
  velocity.linear.x = 0;
  velocity.angular.z = 0;

  // If close to goal, rotate to correct orientation
  bool within_x = (fabs(goal.position.x) < ROBOT_RADIUS);
  bool within_y = (fabs(goal.position.y) < ROBOT_RADIUS);
  if (within_x && within_y)
  {
    desired_heading = goal.orientation.z;
  }

  if (desired_heading < 0)
  {
    if (M_PI + desired_heading > 0)
    {
      direction = CW;
    }
    else
    {
      direction = CCW;
    }
  }
  else
  {
    if (desired_heading - M_PI < 0)
    {
      direction = CCW;
    }
    else
    {
      direction = CW;
    }
  }

  if (within_x && within_y)
  {
    velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_FAST;
    return success;
  }
  else
  {
    if (fabs(desired_heading) < (ANGULAR_THRESHOLD_RATIO * (1 + hysteresis_factor_)))
    {
      // Drive
      velocity.linear.x = MAX_LINEAR_VELOCITY;
      hysteresis_factor_ = HYSTERESIS_LEVEL;
    }
    else
    {
      hysteresis_factor_ = 0;
      // Turn
      velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_SLOW;
    }
  }

  // Pure Pursuit
  if ((fabs(desired_heading) < PURE_PURSUIT_THRESHOLD) && use_pure_pursuit)
  {
    double numerator = (
      pow(goal.position.x, 2) +
      pow(goal.position.y, 2)
    );

    double radius = numerator / (2 * (goal.position.y));

    velocity.linear.x = MAX_LINEAR_VELOCITY;
    velocity.angular.z = MAX_LINEAR_VELOCITY / radius;
  }
  return success;
}