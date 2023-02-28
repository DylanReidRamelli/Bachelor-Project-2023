#ifndef BASIC_ROTATE_HPP
#define BASIC_ROTATE_HPP
#include <cmath>
#include <iostream>
#include <string.h>
#include <vector>

/**
 * Rotation matrix
 * @param angle
 * @param, position vector
 **/
std::vector<float> rotationMatrix(float angle, std::vector<int> &position) {
  float dst_x = cos(angle) * position[0] - sin(angle) * position[1];
  float dst_y = sin(angle) * position[0] + cos(angle) * position[1];
}

/**
 * Rotate each value of the input vector according to an angle.
 * @param A, original 1-D vector of the image.
 * @param angle, angle to rotate.
 * @param width
 * @param height
 * @return vector, resulting rotated vector.
 **/
std::vector<int> rotateScatter(const std::vector<float> &A, const float angle,
                               const int width, const int height) {
  std::vector<int> dst_array(A.size());
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
      // auto it = dst_array.begin() + idx;
      dst_array[idx] = A[i];
    }
  }

  return dst_array;
}

/**
 * Rotate each value of the input vector according to an angle.
 * @param A, original 1-D vector of the image.
 * @param angle, angle to rotate.
 * @param width
 * @param height
 * @return vector, resulting rotated vector.
 **/
std::vector<int> rotateGather(const std::vector<int> &A, const float angle,
                              const int width, const int height) {
  std::vector<int> dst_array(A.size());
  float c_x = width / 2.0;
  float c_y = height / 2.0;

  for (int i = 0; i < dst_array.size(); i++) {
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
      // auto it = dst_array.begin() + idx;
      dst_array[i] = A[idx];
    }
  }

  return dst_array;
}

/**
 * First rotate the four corners of the image, then specify the size of the
 * resulting vector. Then rotate all other points accordin to new nector size.
 * @param A, original 1-D vector of the image.
 * @param angle, angle to rotate.
 * @param width
 * @param height
 * @return vector, resulting rotated vector.
 **/
std::vector<int> rotateGatherNoLoss(const std::vector<int> &A,
                                    const float angle, const int width,
                                    const int height) {
  int c_x = height / 2.0;
  int c_y = width / 2.0;

  // std::vector<int> ld{0, 0};
  // std::vector<int> lu{0, height};
  // std::vector<int> rd = {width, 0};
  // std::vector<int> ru = {width, height};
  // int i = 0;

  // while (i < 2) {
  //   if (i == 0) {
  //     ld[i] = ld[i] - c_x;
  //     lu[i] = lu[i] - c_x;
  //     rd[i] = rd[i] - c_x;
  //     ru[i] = ru[i] - c_x;
  //   } else {
  //     ld[i] = ld[i] - c_y;
  //     lu[i] = lu[i] - c_y;
  //     rd[i] = rd[i] - c_y;
  //     ru[i] = ru[i] - c_y;
  //   }
  //   i++;
  // }
}

#endif