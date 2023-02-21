// #include "../core/basic_rotate.h"
#include "../core/read-png.h"
#include <assert.h>
#include <math.h>
#include <png.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * Rotate an image by iterating over the input array.
 * @param A, input array of type float.
 * @param dst_array, output array of type float.
 * @param angle, angle we want to rotate by.
 * @param width, width of the image.
 * @param height, height of the image.
 * @return void
 **/
void rotateScatter(const float A[], float dst_array[], const float angle,
                   const int width, const int height) {

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  int size = width * height;

  // Iterating horizontally through the image.
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {

      // Subtract center coordinates, so that we rotate with respect to the
      // center of the image.
      float x = i - c_x;
      float y = j - c_y;

      // Rotation operation
      float dst_x = cos(angle) * x - sin(angle) * y;
      float dst_y = sin(angle) * x + cos(angle) * y;

      // Add back the center "vector"
      dst_x = (int)(dst_x + c_x);
      dst_y = (int)(dst_y + c_y);

      // Check if the resulting point is inside the boundary of the image, i.e
      // 0->max_x, 0->max_y.
      if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
        // If so then assign value from original array to dst_array at idx
        // location.
        int idx = dst_y * width + dst_x;
        dst_array[idx] = A[i * width + j];
      }
    }
  }
}

int main(int argc, char *argv[]) {
  // const char *pathname = "../../images/Roberts-Claude-Shannon-1.png";
  const char *pathname = "../../images/data_rectangle.raw";
  int width = 300;
  int height = 200;

  if (argv == 3) {
    width = argv[1];
    height = argv[2];
  }

  // Declare initial variables.
  const int n = width * height;
  float A[n];
  float result[n];

  // Populate result array with 0's.
  memset(result, 0, n * sizeof(float));

  // Open input image and populate input array A.
  FILE *raw_p = fopen(pathname, "rb");
  if (raw_p) {
    fread(A, sizeof(float), n, raw_p);
  }

  // Modify input array A by normalizing values from 0->1.
  for (int i = 0; i < n; ++i) {
    A[i] = A[i] / 255.0;
  }

  // Rotate values of 1D input array and store in result.
  rotateScatter(A, result, M_PI / 4, width, height);

  // Open output file and write result array.
  FILE *fp = fopen("test_image.raw", "wb");
  if (fp) {
    size_t r = fwrite(result, sizeof(result[0]), n, fp);
    printf("wrote %zu elements out of %d requested\n", r, n);
  }

  fclose(fp);
  fclose(raw_p);

  return 0;
}

// Check if output of array respects min anx max values and None value.
// Create checks to make sure that the output