// #include "../core/basic_rotate.h"
#include "../core/read-png.h"
#include <assert.h>
#include <math.h>
#include <png.h>
#include <stdio.h>
#include <stdlib.h>

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

    dst_x = (int)dst_x + c_x;
    dst_y = (int)dst_y + c_y;

    if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
      int idx = dst_x * height + dst_y;
      dst_array[idx] = A[i];
    }
  }
}

int main(int argc, char *argv[]) {
  // const char *pathname = "../../images/Roberts-Claude-Shannon-1.png";
  const char *pathname = "../../images/data_rectangle.raw";

  int width = 300;
  int height = 200;

  const int n = width * height;
  float A[n];
  float result[n];

  FILE *raw_p = fopen(pathname, "rb");
  if (raw_p) {
    fread(A, sizeof(float), n, raw_p);
  }

  for (int i = 0; i < n; ++i) {
    A[i] = A[i] / 255.0;
  }

  // Rotate values of 1D array.
  rotateScatter(A, result, M_PI / 16.0, height, width);

  FILE *fp = fopen("test_image.raw", "wb");
  if (fp) {
    size_t r = fwrite(result, sizeof(result[0]), n, fp);
    printf("wrote %zu elements out of %d requested\n", r, n);
  }

  fclose(fp);

  return 0;
}