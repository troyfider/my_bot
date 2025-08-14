cmake_minimum_required(VERSION 3.0.2)
project(my_bot)

## Compile as C++14 and enable warnings
add_compile_options(-std=c++14 -Wall -Wextra -Wpedantic)

## Find catkin macros and libraries, plus any dependencies
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  gazebo_ros
  robot_state_publisher
  joint_state_publisher
  xacro
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  # INCLUDE_DIRS include
  # LIBRARIES my_bot
  CATKIN_DEPENDS roscpp rospy std_msgs gazebo_ros robot_state_publisher joint_state_publisher xacro
  # DEPENDS system_lib
)

###########
## Build ##
###########
# If you have C++ source files, uncomment and edit below:
# include_directories(
#   include
#   ${catkin_INCLUDE_DIRS}
# )
# add_executable(${PROJECT_NAME}_node src/my_source.cpp)
# target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES})

#############
## Install ##
#############
# Install resource directories (URDF, launch, config, worlds)
install(
  DIRECTORY config description launch worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############
if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  # Add your tests here
endif()