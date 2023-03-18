#!/bin/bash

ROS-DISTRO=humble

RUN tmux new-session -d -s $session
RUN tmux rename-window -t 0 'aby'

#Launch foxglove-bridge
tmux send-keys -t 'aby' 'source /opt/ros/$ROS-DISTRO/setup.bash' Enter
tmux send-keys =t 'aby' 'ros2 launch foxglove_bridge foxglove_bridge_launch.xml port:=8765' Enter

#Launch demo script
tmux splitw -h -p 50
tmux send-keys -t . python /app/demo/demo.py Enter



