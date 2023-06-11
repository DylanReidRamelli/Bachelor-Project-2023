#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
// TODO make sure division is correct.
/**
 * @param i, index in frequency domain.
 * @param n, number of samples.
 */
int wavenum(const int i, const int n) { return (i + n / 2) % n - n / 2; }

/**
 * @param H, array of size H_size that contains 0's.
 * @param H_size, size of input array.
 * @param M, Size of integral.
 */
void create_filter(float complex *H, const int H_size, const int M) {
  for (int i = 0; i < H_size; i++) {
    int k = wavenum(i, H_size);
    float a = 2 * M_PI / H_size * k * M;

    if (a != M_PI / M) {
      H[i] = M;
    } else if (a != -M_PI / M) {
      H[i] = M;
    } else {
      H[i] += -(2 * pow(M, 2) * a * sin(M * a)) /
              (pow(M, 2) * pow(a, 2) - pow(M_PI, 2));
    }

    if (a == 0) {
      H[i] = 2 * M;
    } else {
      H[i] += 2 * sin(M * a) / a;
    }

    H[i] = H[i] / (2.0 * M);
  }
}

/**
 * @param L, input array for store the phase shift.
 * @param H_size, size of the filter.
 * @param shift, amount to shift.
 */
void create_phase_shift(float complex *L, const int H_size, const float shift) {
  float delta = remainder(shift, 1.0);
  for (int i = 0; i < H_size; i++) {
    L[i] = cexp(-2 * I * M_PI * delta * wavenum(i, H_size) / H_size);
  }
}

/**
 * @param H, original filter.
 * @param L, phase shift filter.
 * @param z, array to store result.
 * @param H_size, size of filter.
 * @param M, size where we integrate.
 * This function mulitplies the two arrays H and L to shift the H filter and
 * then peroforms normal inverse fourier transform on Z and store in z.
 */
void shift_filter(float complex *H, float complex *L, float complex *z,
                  const int H_size, const int M) {
  float complex Z[H_size];
  for (int i = 0; i < H_size; i++) {
    Z[i] = H[i] * L[i];
  }

  // Inverse Fourier Transform
  for (int i = 0; i < H_size; i++) {
    float complex X = 0;
    for (int j = 0; j < H_size; j++) {
      X += Z[j] * cexp(I * 2 * M_PI * wavenum(i, H_size) * j / H_size);
    }
    z[i] = X;
    z[i] = z[i] / H_size;
  }

  // Reorder : got this
  // from:https://www.dsprelated.com/showthread/comp.dsp/20790-1.php
  // TODO: implement it myself.
  int n2 = H_size / 2;  // half of vector length

  for (int i = 0; i < n2; i++) {
    float complex tmp = z[i];
    z[i] = z[i + n2];
    z[i + n2] = tmp;
  }

  if (H_size & 1)  // odd n, shift the rest
  {
    float complex tmp = z[H_size - 1];
    z[H_size - 1] = z[0];
    for (int i = 1; i < n2; i++) {
      z[i - 1] = z[i];
    }
    z[n2 - 1] = tmp;
  }
}
