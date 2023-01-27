#include "../core/basic_rotate.h"
#include "../core/read-png.h"
#include <assert.h>
#include <math.h>
#include <png.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
  // const char *pathname = "../../images/Roberts-Claude-Shannon-1.png";
  const char *pathname = "../../images/rectangle.png";
  unsigned char *out;

  int width = 300;
  int height = 200;

  // Read image and store in 2D array.
  png_infop info_ptr = rpng(pathname, &width, &height, &out);

  int A[width * height];
  int result[width * height];

  // Store 1D char array in 1D int array.
  // for (int i = 0; i < height; i++) {
  //   for (int j = 0; j < width; j++) {
  //     // int value = (int)out[i * width + j];
  //     // A[width * i + j] = value;
  //   }
  // }

  // Rotate values of 1D array.
  // rotateScatter(A, result, M_PI / 4.0, width, height);

  free(info_ptr);

  FILE *fp = fopen("test_image", "wb");
  if (fp) {
    // for (int i = 0; i < width * height; i++) {
    //   fprintf(fp, "%d\n", A[i]);
    // }
    size_t r = fwrite(out, sizeof(out[0]), width * height, fp);
    printf("wrote %zu elements out of %d requested\n", r, width * height);
  }

  fclose(fp);

  return 0;
}