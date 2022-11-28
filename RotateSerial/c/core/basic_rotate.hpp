#ifndef BASIC_ROTATE_HPP
#define BASIC_ROTATE_HPP
#include <cmath>
#include <iostream>
#include <string.h>
#include <vector>

std::vector<float> rotateScatter(const std::vector<float> A, const float angle,
                                 const int width, const int height) {
  std::vector<float> dst_array(A.size());
  float c_x = width / 2.0;
  float c_y = height / 2.0;

  for (int i = 0; i < A.size(); i++) {
    float x = std::floor(i / height);
    float y = std::floor(i % height);

    x = x - c_x;
    y = y - c_y;

    float dst_x = cos(angle) * x - sin(angle) * y;
    float dst_y = sin(angle) * x - cos(angle) * y;

    dst_x = std::floor(dst_x + c_x);
    dst_y = std::floor(dst_y + c_y);

    if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
      int idx = dst_x * height + dst_y;
      auto it = dst_array.begin() + idx;
      dst_array.insert(it, A[i]);
    }
  }

  return dst_array;
}

#endif