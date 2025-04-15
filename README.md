# For the simulation framework, install mvsim_ros_noetic

The following steps assume that you have ros-noetic installed and set-up.

**To setup, do the following:**
```bash
sudo apt remove ros-noetic-mvsim # removes the current mvsim package
source /opt/ros/noetic/setup.bash
git clone https://github.com/YoWassup69/mvsim_ros_noetic.git
cd bonda/catkin_ws
sudo add-apt-repository ppa:joseluisblancoc/mrpt-stable # master (stable releases) branch
sudo apt install libmrpt-dev mrpt-apps # C++ libs + apps
sudo apt install python3-pymrpt # for the Python package
sudo apt install \
  build-essential cmake g++ \
  libbox2d-dev \
  libmrpt-opengl-dev libmrpt-obs-dev libmrpt-maps-dev libmrpt-tclap-dev \
  libmrpt-gui-dev libmrpt-tfest-dev libmrpt-topography-dev \
  protobuf-compiler \
  libzmq3-dev \
  pybind11-dev \
  libprotobuf-dev \
  libpython3-dev
catkin config -DProtobuf_PROTOC_EXECUTABLE=/usr/bin/protoc -DPYTHON_EXECUTABLE=/usr/bin/python3
catkin build -j4
source devel/setup.bash
roslaunch mvsim demo_warehouse.launch
```
