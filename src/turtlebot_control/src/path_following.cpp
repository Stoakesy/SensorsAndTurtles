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

bool PathFollowing::updateParameters(const char* parameters)
{
  bool success = false;
  std::list<std::string> values;
  std::string next_value = "";
  for (unsigned int i = 0; i < strlen(parameters); ++i)
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
  std::list<double> convertedValues;
    for(auto it = values.begin(); it != values.end(); ++it)
    {
        std::string nextValue = values.front();
        values.pop_front();
        double result = std::stod(nextValue);
        convertedValues.push_back(result);
    }

  if (convertedValues.size() == EXPECTED_NUMBER_OF_PARAMETERS)
  {
    ANGULAR_THRESHOLD_RATIO = convertedValues.front();
    convertedValues.pop_front();
    HYSTERESIS_LEVEL = convertedValues.front();
    convertedValues.pop_front();
    MAX_LINEAR_VELOCITY = convertedValues.front();
    convertedValues.pop_front();
    MAX_ANGULAR_VELOCITY_FAST = convertedValues.front();
    convertedValues.pop_front();
    MAX_ANGULAR_VELOCITY_SLOW = convertedValues.front();
    convertedValues.pop_front();
    PURE_PURSUIT_THRESHOLD = convertedValues.front();
    convertedValues.pop_front();
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

  // If close to goal, rotate to correct orientation
  bool within_z = (fabs(goal.position.z) < ROBOT_RADIUS);
  bool within_x = (fabs(goal.position.x) < ROBOT_RADIUS);
  if (within_z && within_x)
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

  if (within_z && within_x)
  {
    velocity.angular.z = direction * MAX_ANGULAR_VELOCITY_FAST;
    std::cout << "Target is close to goal. Rotating at " << velocity.angular.z << " rad/s" << std::endl << std::endl;
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