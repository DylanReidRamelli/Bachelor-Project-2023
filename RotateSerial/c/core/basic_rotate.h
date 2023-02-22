#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Find max value in array of float.
float max(float input[], int size) {
  float max_value = 0;
  for (int i = 0; i < size; i++) {
    if (input[i] > max_value)
      max_value = input[i];
  }
  return max_value;
}

// Find min value in array of float.
float min(float input[], int size) {
  float min_value = 0;
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
void rotateCorners(float output[2], int width, int height, float angle) {

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  float corners[8] = {0, 0, 0, height, width, 0, width, height};

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
    printf("nx:%f, ny:%f\n", corners[j], corners[j + 1]);
  }

  float x_values[] = {corners[0], corners[2], corners[4], corners[6]};
  float y_values[] = {corners[1], corners[3], corners[5], corners[7]};
  int sizeX = ceil(max(x_values, 4) - min(x_values, 4));
  int sizeY = ceil(max(y_values, 4) - min(y_values, 4));

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
        dst_array[i * width + j] = A[idx];
      }
    }
  }
}

void rotateGatherNoLoss(const float A[], float *dst_array, const float angle,
                        int width, int height, int mSize[2]) {

  float newSize[2] = {0.0, 0.0};
  rotateCorners(newSize, width, height, angle);

  float c_x = width / 2.0;
  float c_y = height / 2.0;
  float c_x_out = newSize[0] / 2.0;
  float c_y_out = newSize[1] / 2.0;

  float *new_dst_array =
      realloc(dst_array, newSize[0] * newSize[1] * sizeof(float));

  if (new_dst_array) {

    memset(new_dst_array, 0, newSize[0] * newSize[1] * sizeof(float));

    // Iterating horizontally through the image.
    for (int i = 0; i < newSize[1]; i++) {
      for (int j = 0; j < newSize[0]; j++) {

        // Subtract center coordinates, so that we rotate with respect to the
        // center of the image.
        float x = i - c_x_out;
        float y = j - c_y_out;

        // Rotation operation
        float dst_x = cos(angle) * x - sin(angle) * y;
        float dst_y = sin(angle) * x + cos(angle) * y;

        // Add back the center "vector"
        dst_x = (int)(dst_x + c_x);
        dst_y = (int)(dst_y + c_y);

        // Check if the resulting point is inside the boundary of the image,i.e
        // 0->max_x, 0->max_y.
        if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height) {
          // If so then assign value from original array to dst_array at idx
          // location.
          int idx = dst_y * width + dst_x;
          new_dst_array[i * width + j] = A[idx];
        }
      }
    }

    // For python.
    mSize[0] = (int)newSize[0];
    mSize[1] = (int)newSize[1];
  }

  free(new_dst_array);
}
