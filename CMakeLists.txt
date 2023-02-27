cmake_minimum_required(VERSION 3.5...3.19)
cmake_policy(SET CMP0048 NEW)
project(
  Bachelor
  VERSION 0.0.1
  LANGUAGES "CXX" "C"
  DESCRIPTION "C++ and C read and rotate images.")

include(cmake/BachelorOptions.cmake)
include(cmake/BachelorFunctions.cmake)


if(BACHELOR_ENABLE_CUDA)
  enable_language(CUDA)
  find_package(CUDAToolkit)
  # if(CUDA_FOUND)
    add_executable(rotate_loss_CUDA RotateCuda/rotateKernel.cu)
    target_link_libraries(rotate_loss_CUDA Bachelor)
  #   else()
  #   message(STATUS "NO CUDA COMPILER FOUND!")
  # endif()
endif()

# Add CUDA option.

set(BACHELOR_MODULES RotateSerial/c/core)

foreach(MODULE ${BACHELOR_MODULES})
  add_subdirectory("${MODULE}")
endforeach(MODULE)

add_library(Bachelor ${BACHELOR_SOURCES} ${BACHELOR_HEADERS})

# foreach(include ${BACHELOR_BUILD_INCLUDES})
#   target_include_directories(Bachelor BEFORE PUBLIC $<BUILD_INTERFACE:${include}>)
# endforeach()

# target_include_directories(
#   Bachelor BEFORE
#   PUBLIC $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}>
#          $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
#          $<INSTALL_INTERFACE:include>)

# target_include_directories(Bachelor PUBLIC ${BACHELOR_DEP_INCLUDES})
# target_link_libraries(Bachelor PUBLIC ${BACHELOR_DEP_LIBRARIES})

# add_executable(main RotateSerial/c/drivers/main.cpp)
# target_link_libraries(main Bachelor)

# target_compile_features( PRIVATE cxx_std_17)

# add_executable(rotate_loss RotateSerial/c/drivers/rotate_loss.c)
# target_link_libraries(rotate_loss Bachelor)

# add_executable(rotate_noloss RotateSerial/c/drivers/rotate_noloss.c)
# target_link_libraries(rotate_noloss Bachelor)

