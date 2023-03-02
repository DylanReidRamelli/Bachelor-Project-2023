#include "basic_rotate.h"
#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  const char *pathname = "../Images/data_roberts.raw";
  // const char *pathname = "../../../Images/data_rectangle.raw";
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
  float *A = malloc(sizeof(float) * n);
  float *result = malloc(sizeof(float) * n);

  // // Populate result array with 0's.
  memset(result, 0, n * sizeof(float));

  // Open input image and populate input array A.
  FILE *raw_p = fopen(pathname, "rb");
  if (raw_p) {
    fread(A, sizeof(float), n, raw_p);
  } else {
    printf("Not able to open image.\n");
  }

  // Modify input array A by normalizing values from 0->1.
  for (int i = 0; i < n; ++i) {
    A[i] = A[i] / 255.0;
  }

  // Rotate values of 1D input array and store in result.
  // rotateScatter(A, result, M_PI / 4, width, height);
  rotateGather(A, result, M_PI / 4, width, height);

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