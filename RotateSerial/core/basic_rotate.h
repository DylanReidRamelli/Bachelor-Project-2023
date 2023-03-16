#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Find max value in array of float.
float max(const float input[], int size) {
  float max_value = input[0];
  for (int i = 0; i < size; i++) {
    if (input[i] > max_value)
      max_value = input[i];
  }
  return max_value;
}

// Find min value in array of float.
float min(const float input[], int size) {
  float min_value = input[0];
  for (int i = 0; i < size; i++) {
    if (input[i] < min_value)
      min_value = input[i];
  }
  return min_value;
}

// 2D rotation.
void rotation(float coordinate[2], int idx, float angle) {
  float tmp_x = coordinate[idx];
  float tmp_y = coordinate[idx + 1];
  coordinate[idx] = cos(angle) * tmp_x - sin(angle) * tmp_y;
  coordinate[idx + 1] = sin(angle) * tmp_x + cos(angle) * tmp_y;
}

// 2D corner rotation.
void rotateCorners(int output[2], int width, int height, float angle) {

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  float corners[8] = {
      0, 0, 0, (float)height, (float)width, 0, (float)width, (float)height};

  for (int j = 0; j < 8; j++) {
    if (j % 2 == 0) {
      corners[j] = corners[j] - c_x;
    } else {
      corners[j] = corners[j] - c_y;
    }
  }

  for (int i = 0; i < 8; i = i + 2) {
    // printf("nx:%f, ny:%f\n", corners[i], corners[i + 1]);
    rotation(corners, i, angle);
    // printf("nx:%f, ny:%f\n", corners[i], corners[i + 1]);
  }

  for (int j = 0; j < 8; j++) {
    if (j % 2 == 0) {
      corners[j] = corners[j] + c_x;
    } else {
      corners[j] = corners[j] + c_y;
    }
  }

  for (int j = 0; j < 8; j = j + 2) {
    // printf("nx:%f, ny:%f\n", corners[j], corners[j + 1]);
  }

  float x_values[] = {corners[0], corners[2], corners[4], corners[6]};
  float y_values[] = {corners[1], corners[3], corners[5], corners[7]};

  // for (int j = 0; j < 4; j++) {
  //   // printf("nx:%f\n", x_values[j]);
  // }

  int sizeX = ceil(max(x_values, 4) - min(x_values, 4));
  int sizeY = ceil(max(y_values, 4) - min(y_values, 4));

  // printf("sizex:%i, sizey:%i\n", sizeX, sizeY);

  output[0] = sizeX;
  output[1] = sizeY;
}

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

  // Iterating horizontally through the image.
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {

      // Subtract center coordinates, so that we rotate with respect to the
      // center of the image.
      float x = j - c_x;
      float y = i - c_y;

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

/**
 * Rotate an image by iterating over the output array.
 * @param A, input array of type float.
 * @param dst_array, output array of type float.
 * @param angle, angle we want to rotate by.
 * @param width, width of the image.
 * @param height, height of the image.
 * @return void
 **/
void rotateGather(const float A[], float dst_array[], const float angle,
                  const int width, const int height) {
  float c_x = width / 2.0;
  float c_y = height / 2.0;

  // Iterating horizontally through the image.
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {

      // Subtract center coordinates, so that we rotate with respect to the
      // center of the image.
      float x = j - c_x;
      float y = i - c_y;

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
        dst_array[i * width + j] = A[idx];
      }
    }
  }
}

void three_pass_rotation(float *A, float *dst_array, const float angle,
                         int width, int height, int newSize[2]) {
  rotateCorners(newSize, width, height, angle);

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  float c_x_out = newSize[0] / 2.0;
  float c_y_out = newSize[1] / 2.0;

  // Iterating horizontally through the image.
  for (int i = 0; i < newSize[1]; i++) {
    for (int j = 0; j < newSize[0]; j++) {

      // Subtract center coordinates, so that we rotate with respect to the
      // center of the image.
      float x = j - c_x_out;
      float y = i - c_y_out;

      // Rotation operations divided in three matrices.
      float dst_x = x - y * tan(angle / 2);
      float dst_y = y;

      dst_x = dst_x;
      dst_y = dst_x * sin(angle) + dst_y;

      dst_x = dst_x - tan(angle / 2) * dst_y;
      dst_y = dst_y;

      // Add back the center "vector"
      dst_x = (int)(dst_x + c_x);
      dst_y = (int)(dst_y + c_y);

      if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
        // If so then assign value from original array to dst_array at idx
        // location.
        int idx = dst_y * width + dst_x;
        dst_array[i * newSize[0] + j] = A[idx];
      }
    }
  }
}

void rotateGatherNoLoss(float *A, float *dst_array, const float angle,
                        int width, int height, int newSize[2]) {

  // Rotate corners and get new dimentions of image.
  rotateCorners(newSize, width, height, angle);

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  float c_x_out = newSize[0] / 2.0;
  float c_y_out = newSize[1] / 2.0;

  // Iterating horizontally through the image.
  for (int i = 0; i < newSize[1]; i++) {
    for (int j = 0; j < newSize[0]; j++) {

      // Subtract center coordinates, so that we rotate with respect to the
      // center of the image.
      float x = j - c_x_out;
      float y = i - c_y_out;

      // Rotation operation
      float dst_x = cos(angle) * x - sin(angle) * y;
      float dst_y = sin(angle) * x + cos(angle) * y;

      // Add back the center "vector"
      dst_x = (int)(dst_x + c_x);
      dst_y = (int)(dst_y + c_y);

      // Check if the resulting point is inside the boundary of the
      // image,i.e 0->max_x, 0->max_y.
      // if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
      //   // If so then assign value from original array to dst_array at
      //   idx
      //   // location.
      //   int idx = dst_y * width + dst_x;
      //   dst_array[i * newSize[0] + j] = A[idx];
      // }

      if (i < c_y_out + 200 && i > c_y_out) {
        int idx = dst_y * width + dst_x;
        dst_array[i * newSize[0] + j] = A[idx];
      } else {
        dst_array[i * newSize[0] + j] = 0;
      }
    }
  }
}
