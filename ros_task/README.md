This task was done on ROS melodic using a binocular astra camera 
### Setup ROS as described in this link http://wiki.ros.org/ROS/Installation
### Setup Astra Camera for ROS http://wiki.ros.org/astra_camera
### setup rviz http://wiki.ros.org/rviz/UserGuide
### Make sure you created a workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace
### Create a custom package
$ cd ~/catkin_ws/src
$ catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
*dependencies could be std_msgs rospy rocpp or other dependencies* 
$ cd ~/catkin_ws
$ catkin_make
$ . ~/catkin_ws/devel/setup.bash
### navigate via the terminal to the package then src then scripts
### download the 2 codes
### Make sure that files are executable if not you can run the following command
$ chmod +x [filename]
## do the following commands to test the codes in separate terminals
$ roscore
$ roslaunch astra_camera astra.launch
Make sure that the topic /camera/rgb/image_raw is published using $ rostopic list
$ rosrun [pakagename] publisher node
$ rosrun [pakagename] subscriber node
Wait for the image window to show 
$ rviz
Set the fixed frame to camera topic 
And add two images and choose the /sharpened_image topic to be displayed





