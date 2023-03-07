#include "basic_rotate.h"
#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  const char *pathname = "../Images/data_roberts.raw";
  // const char *pathname = "../../Images/data_rectangle.raw";
  int width = 1303;
  int height = 2000;

  if (argc == 3) {
    width = atoi(argv[1]);
    height = atoi(argv[2]);
  }

  if (argc == 4) {
    width = atoi(argv[1]);
    height = atoi(argv[2]);
    pathname = argv[3];
  }

  // Declare initial variables.
  const int n = width * height;

  const float ANGLE = M_PI / 3;

  float *A = malloc(sizeof(float) * n);
  // float result[n];

  // Open input image and populate input array A.
  FILE *raw_p = fopen(pathname, "rb");
  if (raw_p) {
    fread(A, sizeof(float), n, raw_p);
  } else {
    printf("Image not found.\n");
  }

  // Modify input array A by normalizing values from 0->1.
  for (int i = 0; i < n; ++i) {
    A[i] = A[i] / 255.0;
    // printf("%f\n", A[i]);
  }

  int newSize[2] = {0, 0};

  // Rotate corners and get new dimentions of image.
  rotateCorners(newSize, width, height, ANGLE);

  float *result = malloc(newSize[0] * newSize[1] * sizeof(float));
  if (result) {

    memset(result, 0, newSize[0] * newSize[1] * sizeof(float));
    // Rotate values of 1D input array and store in result.
    rotateGatherNoLoss(A, result, ANGLE, width, height, newSize);

    // for (int i = 0; i < newSize[0] * newSize[1]; i++) {
    //   printf("Value: %f", result[i]);
    // }

    FILE *fpdata = fopen("image_info.raw", "w");
    if (fpdata) {
      fprintf(fpdata, "%i,%i", newSize[0], newSize[1]);
    }

    // Open output file and write result array.
    FILE *fp = fopen("test_image_noloss.raw", "wb");
    if (fp) {
      size_t r = fwrite(result, sizeof(result[0]), newSize[0] * newSize[1], fp);
      printf("wrote %zu elements out of %d requested\n", r,
             newSize[0] * newSize[1]);
    }

    fclose(fp);
    fclose(fpdata);
    fclose(raw_p);
  }
  free(result);
  free(A);
  return 0;
}

// Check if output of array respects min anx max values and None value.
// Create checks to make sure that the output