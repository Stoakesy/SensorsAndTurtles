/*!
 * @file main.cpp
 * @brief
 *         Main module.
 *         This module contains user's application code.
 *
 * @author Jacob Vartanian
 * @date 2020-09-25
 */         
/*!
 *  @addtogroup main_module main module documentation
 *  @{
 */         
/* MODULE main */

#include "ros/ros.h"
#include "control.h"

/*!
 * @brief Main method to initialise the ros node and start the control thread
*/
int main(int argc, char **argv)
{
  // Use Pure Pursuit
  bool use_pure_pursuit = true;

  // Use Pure Pursuit
  bool use_p_controller = true;

  // Initialise this ROS node
  ros::init(argc, argv, "path_following");
  ros::NodeHandle nh;

  // Start the threads contained in the control class
  std::shared_ptr<Control> gc(new Control(nh, use_pure_pursuit, use_p_controller));
  std::thread main_thread(&Control::mainThread,gc);

  // Handle callbacks
  ros::spin();

  // Clean up everything, shutdown ROS and rejoin the thread
  ros::shutdown();
  main_thread.join();

  return 0;
}