#include "convolution.h"
#include "fourier_filter.h"
#include <assert.h>
#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

  const double SHIFT = 10.5;

  int n = 100;
  double *x = calloc(n, sizeof(double));
  for (int i = 0; i < floor(n / 2); i++) {
    x[i] = 1;
  }

  // Create filter
  int filterSize = 41;
  int M = 3;
  double complex *H = calloc(filterSize, sizeof(double complex));
  create_filter(H, filterSize, M);

  double complex *L = calloc(filterSize, sizeof(double complex));
  create_phase_shift(L, filterSize, SHIFT);

  double complex *z = calloc(filterSize, sizeof(double complex));
  shift_filter(H, L, z, filterSize, M);

  FILE *fp = fopen("original_signal.raw", "wb");
  if (fp) {
    size_t r = fwrite(x, sizeof(x[0]), n, fp);
    printf("wrote %zu elements out of %d requested\n", r, n);
  }

  FILE *fp1 = fopen("shifted_signal.raw", "wb");
  if (fp1) {
    size_t r = fwrite(x_shifted, sizeof(x_shifted[0]), n + filterSize - 1, fp1);
    printf("wrote %zu elements out of %d requested\n", r, n + filterSize - 1);
  }

  FILE *fp2 = fopen("filter.raw", "wb");
  if (fp2) {
    size_t r = fwrite(z, sizeof(z[0]), filterSize, fp2);
    printf("wrote %zu elements out of %d requested\n", r, filterSize);
  }
}