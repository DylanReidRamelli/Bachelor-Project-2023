#include <math.h>
#include <stdio.h>

void rotateScatter(const float A[], float dst_array[], const float angle,
                   const int width, const int height) {

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  int size = width * height;

  // Iterate over size of dst_array.
  for (int i = 0; i < size; i++) {
    float x = floor(i / height);
    float y = floor(i % height);

    x = x - c_x;
    y = y - c_y;

    float dst_x = cos(angle) * x - sin(angle) * y;
    float dst_y = sin(angle) * x + cos(angle) * y;

    dst_x = floor(dst_x + c_x);
    dst_y = floor(dst_y + c_y);

    if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
      int idx = dst_x * height + dst_y;
      dst_array[idx] = A[i];
    }
  }
}