#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mvsim::mvsim-msgs" for configuration "Release"
set_property(TARGET mvsim::mvsim-msgs APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mvsim::mvsim-msgs PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libmvsim-msgs.so.0.11.2"
  IMPORTED_SONAME_RELEASE "libmvsim-msgs.so.0.11.2"
  )

list(APPEND _IMPORT_CHECK_TARGETS mvsim::mvsim-msgs )
list(APPEND _IMPORT_CHECK_FILES_FOR_mvsim::mvsim-msgs "${_IMPORT_PREFIX}/lib/libmvsim-msgs.so.0.11.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
