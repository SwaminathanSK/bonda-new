
# Honor the DESTDIR env variable:
if (DEFINED ENV{DESTDIR})
    message(STATUS "DESTDIR: $ENV{DESTDIR}")
    set(INSTALL_ROOT_DIR $ENV{DESTDIR}//usr/local)
else()
    set(INSTALL_ROOT_DIR /usr/local)
endif()

set(cmd_
    /usr/bin/python3.8 -m pip install .
        --target=${INSTALL_ROOT_DIR}/lib/python3/dist-packages
        --ignore-installed
        --upgrade
)

string(REPLACE ";" " " _cmd_print "${cmd_}")
message(STATUS "Running: ${_cmd_print}")

execute_process(COMMAND ${cmd_}
    RESULT_VARIABLE result
    WORKING_DIRECTORY /home/swaminathan/catkin_ws/src/mvsim/build
)

if(result)
    message(FATAL_ERROR "CMake step for installing python modules failed: ${result}")
endif()
