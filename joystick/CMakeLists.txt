cmake_minimum_required(VERSION 2.8.3)
project(joystick)

find_package(catkin REQUIRED COMPONENTS
	roscpp
	std_msgs
	geometry_msgs
	sensor_msgs
)

catkin_package(
CATKIN_DEPENDS
	std_msgs
	geometry_msgs
	sensor_msgs
	roscpp
)

