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
    HYSTERESIS_LEVEL = convertedValues.at(3);
    PURE_PURSUIT_THRESHOLD = convertedValues.at(4);
    ANGULAR_THRESHOLD_RATIO = convertedValues.at(5);
    ROBOT_RADIUS = convertedValues.at(6);
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

bool PathFollowing::calculateVelocity(geometry_msgs::Twist &velocity, bool use_pure_pursuit)
{
  if (!IS_ACTIVE)
  {
    getZeroVelocity(velocity);
    return true;
  }
  std::cout << "---------------------------------------------------" << std::endl;
  target_pose_.mtx.lock();
  geometry_msgs::Pose goal = target_pose_.pose;
  target_pose_.mtx.unlock();
  bool success = true;
  double desired_heading = (atan2(goal.position.x, goal.position.z));
  std::cout << "Target is " << goal.position.z << "m in front and " << goal.position.x << "m right" << std::endl;
  std::cout << "Target angle is therefore: " << (desired_heading * 180 / M_PI) << " degrees clockwise" << std::endl;
  TurnDirection_t direction = STRAIGHT;

  // Reset velocity
  velocity.linear.x = 0;
  velocity.angular.z = 0;

  // Check if zero position
  double total_position = fabs(goal.position.x) + fabs(goal.position.y) + fabs(goal.position.z);

  // If close to goal, rotate to correct orientation
  bool within_z = (fabs(goal.position.z) < ROBOT_RADIUS);
  bool within_x = (fabs(goal.position.x) < ROBOT_RADIUS);
  if (total_position == 0)
  {
    desired_heading = previous_heading_;
    std::cout << "Target not found." << std::endl;
  }
  else if (within_z && within_x)
  {
    desired_heading = goal.orientation.y;
    std::cout << "Target is close to goal. Rotating to target by " << (desired_heading * 180 / M_PI) << " degrees clockwise" << std::endl;
  }
  else
  {
    std::cout << "Target is NOT close to goal. Rotating to target by " << (desired_heading * 180 / M_PI) << " degrees clockwise" << std::endl;
  }
  

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

  if (within_z && within_x)
  {
    velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_FAST;
    std::cout << "Rotating at " << velocity.angular.z << " rad/s" << std::endl << std::endl;
    return success;
  }
  else
  {
    if (fabs(desired_heading) < (ANGULAR_THRESHOLD_RATIO * (1 + hysteresis_factor_)))
    {
      // Drive
      velocity.linear.x = MAX_LINEAR_VELOCITY;
      hysteresis_factor_ = HYSTERESIS_LEVEL;
      std::cout << "Target within threshold. Driving at " << velocity.linear.x << " m/s" << std::endl;
    }
    else
    {
      hysteresis_factor_ = 0;
      // Turn
      velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_SLOW;
      std::cout << "Target NOT within threshold. Turning slowly at " << velocity.angular.z << " rad/s" << std::endl << std::endl;
      return success;
    }
  }

  // Pure Pursuit
  if ((fabs(desired_heading) < PURE_PURSUIT_THRESHOLD) && use_pure_pursuit)
  {
    std::cout << "Undertaking Pure Pursuit" << std::endl;
    double numerator = (
      pow(goal.position.z, 2) +
      pow(goal.position.x, 2)
    );

    double radius = numerator / (2 * (goal.position.x));

    velocity.linear.x = MAX_LINEAR_VELOCITY;
    velocity.angular.z = MAX_LINEAR_VELOCITY / radius;
  }
  else
  {
    std::cout << "No Pure Pursuit" << std::endl;
  }
  
  return success;
}