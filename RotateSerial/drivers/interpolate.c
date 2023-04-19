#include "interpolate.h"
#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  float max_x = 30;
  float n_values_out = 1000;
  float *x = malloc(sizeof(float) * max_x);
  float *y = malloc(sizeof(float) * max_x);

  for (int i = 0; i < max_x; i++) {
    x[i] = i;
    y[i] = sin(x[i]);
  }

  float *x_interp_samples = malloc(sizeof(float) * n_values_out);
  float *y_interp_samples = malloc(sizeof(float) * n_values_out);

  for (int i = 0; i < n_values_out; i++) {
    x_interp_samples[i] = i * (max_x / n_values_out);
  }

  interpolate_1D_linear(x, y, x_interp_samples, y_interp_samples, max_x,
                        n_values_out, 0);

  FILE *f_x = fopen("interpolated_points_x.raw", "wb");
  size_t r_x =
      fwrite(x_interp_samples, sizeof(x_interp_samples[0]), n_values_out, f_x);
  printf("wrote %zu elements out of %d requested\n", r_x, (int)n_values_out);

  FILE *f_y = fopen("interpolated_points_y.raw", "wb");
  size_t r_y =
      fwrite(y_interp_samples, sizeof(y_interp_samples[0]), n_values_out, f_y);
  printf("wrote %zu elements out of %d requested\n", r_y, (int)n_values_out);

  for (int i = 0; i < n_values_out; i++) {
    printf("%f\n", x_interp_samples[i]);
  }

  free(x);
  free(y);
  free(x_interp_samples);
  free(y_interp_samples);
}