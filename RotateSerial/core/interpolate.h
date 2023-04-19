#include "interpolants.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void interpolate_1D_linear(float in_x[], float in_y[], float out_x[],
                           float out_y[], int max_out, int n_values_out,
                           float shift) {

  float h = in_x[1] - in_x[0];
  for (int i = 0; i < n_values_out; i++) {
    for (int k = 0; k < max_out; k++) {
      float phi = linear_interpolation_model((out_x[i] - shift - in_x[k]) / h);
      float f_n = in_y[k] * phi;
      out_y[i] += f_n;
    }
  }
}

void interpolate_1D_cubic(float in_x[], float in_y[], float out_x[],
                          float out_y[], int max_out, int n_values_out,
                          float shift) {

  float h = in_x[1] - in_x[0];
  for (int i = 0; i < n_values_out; i++) {
    for (int k = 0; k < max_out; k++) {
      float phi = cubic_spline_model((out_x[i] - shift - in_x[k]) / h);
      float f_n = in_y[k] * phi;
      out_y[i] += f_n;
    }
  }
}

void interpolate_1D_cubic_keys(float in_x[], float in_y[], float out_x[],
                               float out_y[], int max_out, int n_values_out,
                               float shift) {

  float h = in_x[1] - in_x[0];
  for (int i = 0; i < n_values_out; i++) {
    for (int k = 0; k < max_out; k++) {
      float phi =
          keys_cubic_interpolant(-1 / 2, (out_x[i] - shift - in_x[k]) / h);
      float f_n = in_y[k] * phi;
      out_y[i] += f_n;
    }
  }
}