#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mvsim::mvsim-simulator" for configuration "Release"
set_property(TARGET mvsim::mvsim-simulator APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mvsim::mvsim-simulator PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "mvsim::mvsim-msgs"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libmvsim-simulator.so.0.11.2"
  IMPORTED_SONAME_RELEASE "libmvsim-simulator.so.0.11.2"
  )

list(APPEND _IMPORT_CHECK_TARGETS mvsim::mvsim-simulator )
list(APPEND _IMPORT_CHECK_FILES_FOR_mvsim::mvsim-simulator "${_IMPORT_PREFIX}/lib/libmvsim-simulator.so.0.11.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
