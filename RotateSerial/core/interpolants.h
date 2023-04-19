// Bicubic convolution algorithm
#include <math.h>

// The generating function for cubic spline intepolants.
float cubic_spline_model(float x) {
  if (fabs(x) >= 0 && fabs(x) < 1) {
    return 2 / 3 - pow(fabs(x), 2) + pow(fabs(x), 3) / 2;
  } else if (fabs(x) < 2 && fabs(x) >= 1) {
    return pow(2 - fabs(x), 3) / 6;
  } else {
    return 0;
  }
}

// a = -1/2 with N = 3.
float keys_cubic_interpolant(float a, float x) {
  if (fabs(x) >= 0 && fabs(x) < 1) {
    return (a + 2) * pow(fabs(x), 3) - (a + 3) * pow(fabs(x), 2) + 1;
  } else if (fabs(x) >= 1 && fabs(x) < 2) {
    return a * (pow(fabs(x), 3) - 5 * pow(fabs(x), 2) + 8 * fabs(x) - 4);
  } else {
    return 0;
  }
}

float linear_interpolation_model(float x) {
  if (fabs(x) < 1) {
    return 1 - fabs(x);
  } else {
    return 0;
  }
}
