// Bicubic convolution algorithm
#include <math.h>

// The generating function for cubic spline intepolants.
float cubic_spline_model(float x) {
  if (abs(x) >= 0 && abs(x) < 1) {
    return 2 / 3 - pow(abs(x), 2) + pow(abs(x), 3) / 2;
  } else if (abs(x) < 2 && abs(x) >= 1) {
    return pow(2 - abs(x), 3) / 6;
  } else {
    return 0;
  }
}

// a = -1/2 with N = 3.
float keys_cubic_interpolant(float a, float x) {
  if (abs(x) >= 0 && abs(x) < 1) {
    return (a + 2) * pow(abs(x), 3) - (a + 3) * pow(abs(x), 2) + 1;
  } else if (abs(x) >= 1 && abs(x) < 2) {
    return a * (pow(abs(x), 3) - 5 * pow(abs(x), 2) + 8 * abs(x) - 4);
  } else {
    return 0;
  }
}