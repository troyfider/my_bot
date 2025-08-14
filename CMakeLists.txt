cmake_minimum_required(VERSION 3.0.2)
project(my_bot)

## Compile as C++14
add_compile_options(-std=c++14 -Wall -Wextra -Wpedantic)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  # Add any other dependencies here
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  # INCLUDE_DIRS include
  # LIBRARIES my_bot
  CATKIN_DEPENDS roscpp std_msgs
  # DEPENDS system_lib
)

###########
## Build ##
###########
# Example: If you have source files to compile
# include_directories(
#   include
#   ${catkin_INCLUDE_DIRS}
# )
# add_executable(${PROJECT_NAME}_node src/my_source.cpp)
# target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES})

#############
## Install ##
#############
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