#!/bin/bash

#set -x
set -e

cd /home/swaminathan/catkin_ws/src/mvsim/build

/usr/bin/python3.8 -m venv venv
source venv/bin/activate

pip install -r /home/swaminathan/catkin_ws/src/mvsim/requirements.txt
