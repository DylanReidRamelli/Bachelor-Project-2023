#include "convolution.h"
#include "fourier_filter.h"
#include <assert.h>
#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

  if (2 != argc) {
  }

  const double SHIFT = 10.5;

  int n = 100;
  double *x = calloc(n, sizeof(double));
  for (int i = 0; i < floor(n / 2); i++) {
    x[i] = 1;
  }

  // Create filter
  double complex *H = calloc(FILTER_SIZE, sizeof(double complex));
  create_filter(H, FILTER_SIZE, M);

  double complex *L = calloc(FILTER_SIZE, sizeof(double complex));
  create_phase_shift(L, FILTER_SIZE, SHIFT);

  double complex *z = calloc(FILTER_SIZE, sizeof(double complex));
  shift_filter(H, L, z, FILTER_SIZE, M);

  FILE *fp = fopen("original_signal.raw", "wb");
  if (fp) {
    size_t r = fwrite(x, sizeof(x[0]), n, fp);
    printf("wrote %zu elements out of %d requested\n", r, n);
  }

  FILE *fp2 = fopen("filter.raw", "wb");
  if (fp2) {
    size_t r = fwrite(z, sizeof(z[0]), FILTER_SIZE, fp2);
    printf("wrote %zu elements out of %d requested\n", r, FILTER_SIZE);
  }
}