cmake_minimum_required(VERSION 3.5...3.19)
cmake_policy(SET CMP0048 NEW)
project(
  Rotate
  VERSION 0.0.1
  LANGUAGES "CXX" "C"
  DESCRIPTION "C++ and C read and rotate images.")

find_package(Boost)
find_package(PNG)

add_library(Rotate INTERFACE)
target_include_directories(Rotate INTERFACE core/)

if(Boost_FOUND)
  include_directories(${Boost_INCLUDE_DIRS})
  target_link_libraries(Rotate ${Boost_LIBRARIES})
endif()

if(PNG_FOUND)
  include_directories(${PNG_INCLUDE_DIRS})
  target_link_libraries(Rotate INTERFACE ${PNG_LIBRARIES})
endif()

add_executable(main drivers/main.cpp)
target_link_libraries(main Rotate)

target_compile_features(main PRIVATE cxx_std_17)

add_executable(mainC drivers/main.c)
target_link_libraries(mainC Rotate)

target_compile_features(mainC PRIVATE cxx_std_17)
