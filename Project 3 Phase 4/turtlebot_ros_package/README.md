# Using A-star Algorithm on ROS Turtlebot


### Software Required
Ubuntu 18.04
ROS Melodic
For this project you will need to install the rospy, numpy, matplotlib and gazebo to run the simulations.


### Creating a catkin workspace and getting required packages
-> Creating Catkin workspace:
source /opt/ros/melodic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make

-> Getting Turtlebot3 Packages:
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git -b melodic-devel
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git -b melodic-devel
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git -b melodic-devel
cd ~/catkin_ws
catkin_make


### Instructions for running the code

-> Download zip folder proj3_33_gazebo_python.zip
-> Extract the zip folder
-> Goto "Phase4" folder
-> Goto "ros_ws" folder
-> copy and paste the folder "astar" at ~/catkin_ws/src

For running the code please follow instructions given below.
->Open Terminal
source /opt/ros/melodic/setup.bash
cd ~/catkin_ws
catkin_make
cd ~/catkin_ws/src/astar/scripts
chmod +x astar.py
cd ~/catkin_ws
catkin_make

Once all the above steps have been performed lets source our catkin workspace and then run the program
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash
export TURTLEBOT3_MODEL= waffle
""NOTE : In the below mentioned command the x and y coordinate should be in m i.e range[-5.1,5.1] for both x and y and yaw must be (theta in degree)*3.14/180. The below mentioned x,y,yaw should match with the ones start co-ordinates you will provide further" 
roslaunch astar demo.launch x:=<start point x-coordinate in m> y:=<start point y-coordinate in m> yaw:=<start angle of robot>


Once you run the environment a second terminal will pop up in which you need to enter the following information:

->Enter the Clearance of the robot in m
->Enter the RPM of the Robot (RPM1,RPM2) -> RPM1 RPM2
"NOTE: The start co-ordinates must be same as mentioned in the command before"
->Enter the co-ordinates of starting point separated by space in m (x,y,theta_s (in radians)) --> x y theta_s
->Enter the co-ordinates of goal point separated by space in m  (x,y) --> x y 
Hit Enter

#Submission Video Parameters:
Video-1
-> Clearance -> 50
-> RPM -> 50 100
-> Start -> -4600 -4600 0
-> Goal -> 4600 4600

Video-2
-> Clearance -> 50
-> RPM -> 50 100
-> Start -> -4600 -4600 0
-> Goal -> 4600 4600

### Results
The following is an example of A-star algorithm applied on a rigid robot (Start Node(in m)- (4, 3, 0), Goal Node(in m)- (-4, -3), Wheel RPM- (100, 50), Clearance(in m)- 0.2):
![Screenshot](output.png)
