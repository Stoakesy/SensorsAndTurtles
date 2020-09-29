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

#include "geometry_msgs/Pose.h"
#include "geometry_msgs/Twist.h"
#include <cmath>
#include <atomic>
#include <mutex>

/**
 * @brief Struct to hold information about the robot.
 */
struct TargetPose
{
  geometry_msgs::Pose pose; /**< Container holding the robot's data. */
  std::mutex mtx;                       /**< Mutex to enable thread safe operations. */
};


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
class PathFollowing
{
  public:
    /**
     * @brief Constructor for PathFollowing class
     * 
     */
    PathFollowing();

    /**
     * @brief Sets the target pose for the robot to go to
     * 
     * @param target_pose Target pose of the robot
     * 
     * @return true if the operation was successful
     */
    bool setTargetPose(geometry_msgs::Pose target_pose);

    /**
     * @brief Returns the required velocity of the robot to reach a given pose
     * 
     * @param velocity Reference to the required velocity of the robot to reach the next pose
     * @param use_pure_pursuit flag to indicate if pure pursuit should be used
     * 
     * @return true if the operation was successful
     */
    bool calculateVelocity(geometry_msgs::Twist &velocity, bool use_pure_pursuit);

  private:
    const double ANGULAR_THRESHOLD_RATIO = 0.05;
    const double HYSTERESIS_LEVEL = 0.5;
    const double MAX_LINEAR_VELOCITY = 1.0;
    const double MAX_ANGULAR_VELOCITY_FAST = 3.0;
    const double MAX_ANGULAR_VELOCITY_SLOW = 0.5;
    const double PURE_PURSUIT_THRESHOLD = M_PI_4;
    const double ROBOT_RADIUS = 0.1;
    double hysteresis_factor_;
    double previous_heading_;
    TargetPose target_pose_;
};

#endif // PATH_FOLLOWING_H