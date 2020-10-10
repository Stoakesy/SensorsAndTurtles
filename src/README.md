# Turtlebot Following Project

The following is instructions on how to test and demonstrate the code used within this project WITHOUT the use of real hardware.

As real hardware is used for this project instead of a simulation, a rosbag file with real input data is provided to test the project.

The code provided within the zip package is all that is required to execute this demo. The complete project files, including calibration images and other resources used for debugging can be found on the [GitHub Repository](https://github.com/Stoakesy/SensorsAndTurtles)

## System Requirements

For this project, MATLAB R2020b is required. This is because of the use of the function `readAprilTag()` found in the computer vision toolbox, which was introduced from this release.

 - `MATLAB` Release: `R2020b`
   - Computer Vision Toolbox
   - Image Processing Toolbox
   - ROS Toolbox

C++ is used for the turtlebot control algorithms and requires the following CMake version or later

 - `CMake` minimum version: `2.8.3`

Python3 with PyQT is used for a graphical user interface. This is required to run the turtlebot as a safety feature, as the turtlebot will not be able to start unless this interface is present (as it is used to stop the robot).

 - `Python3` minimum version `3.6.9`
 - `PyQT` version `5.9.2` (requires `pip3` to install)

Note, later versions of PyQT may be unstable, and hence it is recommended to install version 5.9.2. To install pip3 and PyQT, run the following:

```
sudo apt-get update
sudo apt-get install python3-pip
pip3 install PyQt5==5.9.2
```

If you receive an error when installing PyQT, additional packages may need to be installed (such as `setuptools`). This can be installed using `pip3`.

If for any reason the python GUI cannot be started, the system can still be demonstrated by playing back the GUI ROS data from the ROS bag file (see "Executing the Demo" below)

The project was tested using `Ubuntu 16.04` and `18.04` with their recommended ROS versions. `Ubuntu 16.04` was used with the real hardware.

## Compiling

Move the files provided in `src` into  `~/catkin_ws/src/`

Run `catkin_make`

Source the `setup.bash` file using `source ~/catkin_ws/devel/setup.bash`

## Initialising the Environment

Open `MATLAB R2020b` and add the folder `~/catkin_ws/src/img_process` to the MATLAB path

In a new terminal window, start ROS using `roscore`

In the MATLAB command window, run `rosinit`. This will ensure the ROS environment started will be connected to MATLAB's ROS environment.

In a new terminal window, run the turtlebot control ROS node using

`rosrun turtlebot_control turtlebot_control_main`

You should notice the output velocity is printed on the screen, which should be 0.

In a new terminal window, run the GUI ROS node using

`rosrun turtlebot_control ui_controller.py`

You should notice the output on the `turtlebot_control_main` ROS node change to display more information.

## Executing the Demo

To execute the demo, the image data needs to be published and processed. The image processing script requires the image ROS topic to be active, and hence the ROS bag data needs to be published before this.

In the real hardware, image data is being published consistantly, hence this is only a limitation for the sake of this demonstration without hardware.

The provided ROS bag file `turtlebot_following_demo.bag` contains data relating to all the topics. For the sake of this demonstration, we only require data to be published to the topic `/camera/color/image_raw`. To do this, run the following command:

`rosbag play ~/catkin_ws/src/rosbag/turtlebot_following_demo.bag --topics /camera/color/image_raw`

If the python GUI above could not be initialised, playback the data published from this by adding the topic `/control_parameters` as an additional topic to playback.

This will playback the image data for approximately 45 seconds. You can pause the publishing of data using the `space` key on the keyboard.

You can view the images being published using built in ROS tools such as `rqt` or `image_view`. It is recommended to use `rqt` for image viewing as it seems to run smoother when using the image visualisation tools in `rqt`.

While the ROS bag file is running, execute the MATLAB script, `img_processing.m` using the MATLAB command window. If there is an error, check that data is being published to the `/camera/color/image_raw` topic and that the ROS environment has been setup correctly. You may need to run `rosshutdown` and `rosinit` again in the MATLAB command window.

## Verification of Demo

The output of the ROS node `turtlebot_control_main` shows how the turtlebot is behaving, including the direction it is moving, what course of action it is taking and its linear and angular velocity. This can be verified by viewing the published images on `rqt` and checking that the output makes sense according to the images.

It may also be desired to adjust some of the parameters in the GUI, or test the `Stop` button. If this is done, be aware that the turtlebot behaviour will change virtually, which won't be reflected on the input images, as this was taken using the default parameters.