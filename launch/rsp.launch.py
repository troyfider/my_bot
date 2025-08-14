<launch>
  <!-- Argument: use_sim_time -->
  <arg name="use_sim_time" default="false" />

  <!-- Load the robot_description parameter from the Xacro file -->
  <param name="robot_description"
         command="$(find xacro)/xacro '$(find my_bot)/description/robot.urdf.xacro'" />

  <!-- Start the robot_state_publisher node -->
  <node pkg="robot_state_publisher"
        type="robot_state_publisher"
        name="robot_state_publisher"
        output="screen">
    <param name="use_sim_time" value="$(arg use_sim_time)" />
  </node>
</launch>