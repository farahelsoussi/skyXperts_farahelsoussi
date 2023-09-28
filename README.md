# skyXperts_farahelsoussi
## Prerequistes 
This task was done on ROS melodic using a binocular astra camera 
# Setup ROS as described in this link http://wiki.ros.org/ROS/Installation
# Setup Astra Camera for ROS http://wiki.ros.org/astra_camera
# make sure you created a workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace
# create a custom package
$ cd ~/catkin_ws/src
$ catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
dependencies could be std_msgs rospy rocpp or other dependencies
$ cd ~/catkin_ws
$ catkin_make
$ . ~/catkin_ws/devel/setup.bash
# navigate via terminal to the package then src then scripts
# clone this repo
# make sure that files are executable if not you can run the following command
$ chmod +x [filename]
# navigate into each directory and follow the README file in each to know how to run each code
