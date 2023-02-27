cmake_minimum_required(VERSION 3.5...3.19)
cmake_policy(SET CMP0048 NEW)
project(
  Bachelor
  VERSION 0.0.1
  LANGUAGES "CXX" "C"
  DESCRIPTION "C++ and C read and rotate images.")

include(cmake/BachelorOptions.cmake)

find_package(Boost)
find_package(PNG)

add_library(Bachelor INTERFACE)
target_include_directories(Bachelor INTERFACE core/)

if(Boost_FOUND)
  include_directories(${Boost_INCLUDE_DIRS})
  target_link_libraries(Bachelor ${Boost_LIBRARIES})
endif()

if(PNG_FOUND)
  include_directories(${PNG_INCLUDE_DIRS})
  target_link_libraries(Bachelor INTERFACE ${PNG_LIBRARIES})
endif()

add_executable(main RotateSerial/c/drivers/main.cpp)
target_link_libraries(main Bachelor)

target_compile_features(main PRIVATE cxx_std_17)

add_executable(rotate_loss RotateSerial/c/drivers/rotate_loss.c)
target_link_libraries(rotate_loss Bachelor)

add_executable(rotate_noloss RotateSerial/c/drivers/rotate_noloss.c)
target_link_libraries(rotate_noloss Bachelor)

if(BACHELOR_ENABLE_CUDA)
  if(CUDA_FOUND)
    add_executable(rotate_loss_CUDA RotateCuda/rotateKernel.cu)
    target_link_libraries(rotate_loss_CUDA Bachelor)
    else()
    message(STATUS "NO CUDA COMPILER FOUND!")
  endif()
endif()

# Add CUDA option.
