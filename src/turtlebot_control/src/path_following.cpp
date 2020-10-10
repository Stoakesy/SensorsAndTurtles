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

PathFollowing::PathFollowing()
{
  
}

bool PathFollowing::setTargetPose(geometry_msgs::Pose target_pose)
{
  target_pose_.mtx.lock();
  target_pose_.pose = target_pose;
  target_pose_.mtx.unlock();
  return true;
}

bool PathFollowing::updateParameters(std::string parameters)
{
  bool success = false;
  std::vector<std::string> values;
  std::string next_value = "";
  for (unsigned int i = 0; i < parameters.length(); ++i)
  {
    if (parameters[i] == ',')
    {
      values.push_back(next_value);
      next_value = "";
    }
    else
    {
      next_value += parameters[i];
    }
  }
  values.push_back(next_value);
  std::vector<double> convertedValues;
    for(auto& it : values)
    {
        std::string nextValue = it;
        double result = std::stod(nextValue);
        convertedValues.push_back(result);
    }

  if (convertedValues.size() == EXPECTED_NUMBER_OF_PARAMETERS)
  {
    MAX_LINEAR_VELOCITY = convertedValues.at(0);
    MAX_ANGULAR_VELOCITY_FAST = convertedValues.at(1);
    MAX_ANGULAR_VELOCITY_SLOW = MAX_ANGULAR_VELOCITY_FAST * convertedValues.at(2);
    PURSUIT_THRESHOLD = convertedValues.at(3) * (M_PI / 180.0);
    STOPPING_DISTANCE = convertedValues.at(4);
    IS_ACTIVE = convertedValues.at(7);
    success = true;
  }
  return success;
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

bool PathFollowing::calculateVelocity(geometry_msgs::Twist &velocity)
{
  // ------------------- Get data -------------------
  // Initialise variables
  bool success = true;
  TurnDirection_t direction = STRAIGHT;
  getZeroVelocity(velocity);

  // If stop if pressed, don't drive
  if (!IS_ACTIVE)
  {
    return success;
  }

  // Otherwise, drive. First, work out where we are relative to the code
  std::cout << "---------------------------------------------------" << std::endl;
  target_pose_.mtx.lock();
  geometry_msgs::Pose goal = target_pose_.pose;
  target_pose_.mtx.unlock();
  double desired_heading = (atan2(goal.position.x, goal.position.z));
  std::cout << "Target is " << goal.position.z << "m in front and " << goal.position.x << "m right" << std::endl;
  std::cout << "Target angle is therefore: " << (desired_heading * 180.0 / M_PI) << " degrees clockwise" << std::endl;

  // Check if zero position (i.e. code not found)
  double total_position = fabs(goal.position.x) + fabs(goal.position.y) + fabs(goal.position.z);

  // Determine if close to goal
  bool within_z = (fabs(goal.position.z) < STOPPING_DISTANCE);
  bool within_x = (fabs(goal.position.x) < STOPPING_DISTANCE);

  // ------------------- Determine the desired heading -------------------
  // If goal not found, position is 0
  if (total_position == 0)
  {
    desired_heading = previous_heading_;
    std::cout << "Target not found." << std::endl;
  }
  // Else if close to goal, point to target
  else if (within_z && within_x)
  {
    desired_heading = goal.orientation.y;
    std::cout << "Target is close to goal. Rotating to target by " << (desired_heading * 180 / M_PI) << " degrees clockwise" << std::endl;
  }
  else
  // Else drive to target
  {
    std::cout << "Target is NOT close to goal. Rotating to target by " << (desired_heading * 180 / M_PI) << " degrees clockwise" << std::endl;
  }
  
  // ------------------- Determine which direction to turn -------------------
  if (desired_heading < 0)
  {
    std::cout << "Robot turning CCW" << std::endl;
    direction = CCW;
  }
  else
  {
    std::cout << "Robot turning CW" << std::endl;
    direction = CW;
  }
  previous_heading_ = desired_heading;

  // ------------------- Determine pursuit strategy -------------------
  // If close to target (or tag not found), rotate only
  if (within_z && within_x)
  {
    velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_FAST;
    std::cout << "Rotating at " << velocity.angular.z << " rad/s" << std::endl << std::endl;
    return success;
  }
  // If not close to target, drive with linear velocity
  else
  {
    double angle_ratio = fabs(desired_heading) / PURSUIT_THRESHOLD;
    // If within angle, use proportional controller
    if (angle_ratio < 1.0)
    {
      velocity.linear.x = MAX_LINEAR_VELOCITY * (1.0 - angle_ratio);
      velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_SLOW * angle_ratio;
      std::cout << "Target within threshold. Angular ratio of " << angle_ratio << std::endl << std::endl;
    }
    // If outside of angle, simply turn
    else
    {
      velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_SLOW;
      std::cout << "Target NOT within threshold. Turning slowly at " << velocity.angular.z << " rad/s" << std::endl << std::endl;
    }
  }
  return success;
}