#ifndef BASIC_ROTATE_HPP
#define BASIC_ROTATE_HPP
#include <cmath>
#include <iostream>
#include <string.h>
#include <vector>

std::vector<float> rotateScatter(const std::vector<float> A, const float angle,
                                 const int width, const int heigth) {
  std::vector<float> dst_array = [0] * A.length();
  float c_x = width / 2.0;
  float c_y = width / 2.0;

  for (int i = 0; i < A.length(); i++) {
    float x = std::floor(i / heigth);
    float y = std::floor(i % heigth);
  }

  return dst_array;
}

#endif