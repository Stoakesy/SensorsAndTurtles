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

#ifndef PATH_FOLLOWING_H
#define PATH_FOLLOWING_H

#include "robot_data.h"
#include "geometry_msgs/Pose.h"
#include "geometry_msgs/Twist.h"
#include <cmath>

/**
 * @brief Enum indicating a direction.
 */
typedef enum
{
  STRAIGHT = 0, /**< Straight (not turning). */
  CCW = 1,      /**< Counter-clockwise (assumed to be the positive direction). */
  CW = -1       /**< Clockwise (assumed to be the negative direction). */
} TurnDirection_t;

/**
 * @class PathFollowing
 * @brief This class holds the main algorithms used to calculate the robot's required 
 * linear and angular velocity
 */
class PathFollowing: public RobotData
{
  public:
    /**
     * @brief Constructor for PathFollowing class
     * 
     * @param buffer_size The maximum number of data points that will be stored
     */
    PathFollowing(int buffer_size);

    /**
     * @brief Returns the required velocity of the robot to reach a given pose
     * 
     * @param velocity Reference to the required velocity of the robot to reach the next pose
     * @param goal Goal pose of the robot
     * @param use_pure_pursuit flag to indicate if pure pursuit should be used
     * 
     * @return true if the operation was successful
     */
    bool calculateVelocity(geometry_msgs::Twist &velocity, geometry_msgs::Pose goal, bool use_pure_pursuit);

  private:
    const double ANGULAR_THRESHOLD_RATIO = 0.05;
    const double HYSTERESIS_LEVEL = 0.5;
    const double MAX_LINEAR_VELOCITY = 1.0;
    const double MAX_ANGULAR_VELOCITY_FAST = 3.0;
    const double MAX_ANGULAR_VELOCITY_SLOW = 0.5;
    const double PURE_PURSUIT_THRESHOLD = M_PI_4;
    double hysteresis_factor_;
    double previous_heading_;
};

#endif // PATH_FOLLOWING_H