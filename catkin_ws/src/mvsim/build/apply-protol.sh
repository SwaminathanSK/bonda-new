#!/bin/bash

#set -x
set -e

cd /home/swaminathan/catkin_ws/src/mvsim/build
source /home/swaminathan/catkin_ws/src/mvsim/build/venv/bin/activate

protol --create-package \
    --in-place \
    --python-out /home/swaminathan/catkin_ws/src/mvsim/build/mvsim_msgs/ \
    protoc --proto-path=/home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto \
    /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/AdvertiseServiceRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/AdvertiseTopicRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/CallService.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/GenericAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/GenericObservation.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/GetServiceInfoAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/GetServiceInfoRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/ListNodesAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/ListNodesRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/ListTopicsAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/ListTopicsRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/ObservationLidar2D.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/Pose.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/RegisterNodeAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/RegisterNodeRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvGetPose.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvGetPoseAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvSetControllerTwist.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvSetControllerTwistAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvSetPose.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvSetPoseAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvSetPoseTwist.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvShutdown.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SrvShutdownAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SubscribeAnswer.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/SubscribeRequest.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/TimeStampedPose.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/TopicInfo.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/Twist.proto /home/swaminathan/catkin_ws/src/mvsim/modules/msgs/proto/UnregisterNodeRequest.proto

