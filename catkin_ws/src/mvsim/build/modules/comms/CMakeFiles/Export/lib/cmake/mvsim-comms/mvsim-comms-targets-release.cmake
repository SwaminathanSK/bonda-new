#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mvsim::mvsim-comms" for configuration "Release"
set_property(TARGET mvsim::mvsim-comms APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mvsim::mvsim-comms PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libmvsim-comms.so.0.11.2"
  IMPORTED_SONAME_RELEASE "libmvsim-comms.so.0.11.2"
  )

list(APPEND _IMPORT_CHECK_TARGETS mvsim::mvsim-comms )
list(APPEND _IMPORT_CHECK_FILES_FOR_mvsim::mvsim-comms "${_IMPORT_PREFIX}/lib/libmvsim-comms.so.0.11.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
