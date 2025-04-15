# CMake generated Testfile for 
# Source directory: /home/swaminathan/catkin_ws/src/mvsim/tests
# Build directory: /home/swaminathan/catkin_ws/src/mvsim/build/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Still2DLidarRanges "/home/swaminathan/.local/bin/cmake" "-E" "env" "PYTHONPATH=/home/swaminathan/catkin_ws/src/mvsim/build:/opt/ros/noetic/lib/python3/dist-packages" "LD_LIBRARY_PATH=/home/swaminathan/catkin_ws/src/mvsim/build/modules/comms/lib:/home/swaminathan/catkin_ws/src/mvsim/build/modules/msgs/lib:/home/swaminathan/catkin_ws/src/mvsim/build/modules/simulator/lib:/opt/ros/noetic/lib:/opt/ros/noetic/lib/x86_64-linux-gnu:/home/swaminathan/gurobi1100/linux64/lib:/home/swaminathan/.mujoco/mujoco210/bin:/home/swaminathan/.mujoco/mujoco200/bin:/usr/lib/nvidia" "TESTS_DIR=/home/swaminathan/catkin_ws/src/mvsim/tests" "MVSIM_CLI_EXE_PATH=/home/swaminathan/catkin_ws/src/mvsim/build/bin/mvsim" "/usr/bin/python3" "/home/swaminathan/catkin_ws/src/mvsim/tests/test-still-lidar2d.py")
set_tests_properties(Still2DLidarRanges PROPERTIES  _BACKTRACE_TRIPLES "/home/swaminathan/catkin_ws/src/mvsim/tests/CMakeLists.txt;14;add_test;/home/swaminathan/catkin_ws/src/mvsim/tests/CMakeLists.txt;0;")
add_test(test_shape2p5_build "/home/swaminathan/.local/bin/cmake" "--build" "/home/swaminathan/catkin_ws/src/mvsim/build/tests" "--target" "test_shape2p5")
set_tests_properties(test_shape2p5_build PROPERTIES  _BACKTRACE_TRIPLES "/home/swaminathan/catkin_ws/src/mvsim/cmake/mvsim_cmake_functions.cmake;75;add_test;/home/swaminathan/catkin_ws/src/mvsim/tests/CMakeLists.txt;31;mvsim_add_test;/home/swaminathan/catkin_ws/src/mvsim/tests/CMakeLists.txt;0;")
add_test(run_test_shape2p5 "/home/swaminathan/catkin_ws/src/mvsim/build/bin/test_shape2p5")
set_tests_properties(run_test_shape2p5 PROPERTIES  DEPENDS "test_shape2p5_build" _BACKTRACE_TRIPLES "/home/swaminathan/catkin_ws/src/mvsim/cmake/mvsim_cmake_functions.cmake;76;add_test;/home/swaminathan/catkin_ws/src/mvsim/tests/CMakeLists.txt;31;mvsim_add_test;/home/swaminathan/catkin_ws/src/mvsim/tests/CMakeLists.txt;0;")
