#include <assert.h>
#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "convolution.h"
#include "fourier_filter.h"

int main(int argc, char *argv[]) {
  if (2 != argc) {
    fprintf(stderr, "usage: %s <shift-value>\n", argv[0]);

    return EXIT_FAILURE;
  }

  enum { FILTER_SUPPORT = _N_ };

  const float SHIFT = atof(argv[1]);
  const int INT_SHIFT = (int)SHIFT;

  // TODO define a way to choose which M based on the amount of fractional
  // shift.

  float M = 2;
  int n = 100;
  int n_extended = n + FILTER_SUPPORT;

  // Create simple signal, half 1's, half 0's.
  float *x = calloc(n, sizeof(float));
  for (int i = 0; i < floor(n / 2); i++) {
    x[i] = 1;
  }

  // Create filter
  float complex *H = calloc(FILTER_SUPPORT, sizeof(float complex));
  create_filter(H, FILTER_SUPPORT, M);

  float complex *L = calloc(FILTER_SUPPORT, sizeof(float complex));
  create_phase_shift(L, FILTER_SUPPORT, SHIFT - INT_SHIFT);

  float complex *z = calloc(FILTER_SUPPORT, sizeof(float complex));
  shift_filter(H, L, z, FILTER_SUPPORT, M);

  float output[n];
  float *output_int_shift = calloc(n, sizeof(float));

  if (SHIFT - INT_SHIFT != 0) {
    dconv(x, n, z, output);
  } else {
    if (INT_SHIFT > 0) {
      memcpy(output_int_shift + INT_SHIFT, x, sizeof(float) * (n - INT_SHIFT));
    } else {
      memcpy(output_int_shift, x + abs(INT_SHIFT),
             sizeof(float) * (n - abs(INT_SHIFT)));
    }
  }

  // Shift by the integral part
  FILE *fp = fopen("original_signal.raw", "wb");
  if (fp) {
    size_t r = fwrite(x, sizeof(x[0]), n, fp);
    printf("wrote %zu elements out of %d requested\n", r, n);
  }

  FILE *fp1 = fopen("shifted_signal.raw", "wb");
  if (fp1) {
    size_t r = fwrite(output_int_shift, sizeof(output_int_shift[0]), n, fp1);
    printf("wrote %zu elements out of %d requested\n", r, n);
  }

  FILE *fp2 = fopen("filter.raw", "wb");
  if (fp2) {
    size_t r = fwrite(z, sizeof(z[0]), FILTER_SUPPORT, fp2);
    printf("wrote %zu elements out of %d requested\n", r, FILTER_SUPPORT);
  }

  free(x);
  free(H);
  free(L);
  free(z);
}
