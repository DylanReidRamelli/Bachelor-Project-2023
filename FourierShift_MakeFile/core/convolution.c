#include <complex.h>
#include <stddef.h>
static void kconv(
    const float *in0, const int n, const float complex w0,
    const float complex w1, const float complex w2, const float complex w3,
    const float complex w4, const float complex w5, const float complex w6,
    const float complex w7, const float complex w8, const float complex w9,
    const float complex w10, const float complex w11, const float complex w12,
    const float complex w13, const float complex w14, const float complex w15,
    const float complex w16, const float complex w17, const float complex w18,
    const float complex w19, const float complex w20, const float complex w21,
    const float complex w22, const float complex w23, const float complex w24,
    const float complex w25, const float complex w26, const float complex w27,
    const float complex w28, const float complex w29, const float complex w30,
    const float complex w31, const float complex w32, const float complex w33,
    const float complex w34, const float complex w35, const float complex w36,
    const float complex w37, const float complex w38, const float complex w39,
    const float complex w40, float *out) {
  for (int i = 0; i < n; ++i) {
    {
      out[i] = w0 * in0[i + 0] + w1 * in0[i + 1] + w2 * in0[i + 2] +
               w3 * in0[i + 3] + w4 * in0[i + 4] + w5 * in0[i + 5] +
               w6 * in0[i + 6] + w7 * in0[i + 7] + w8 * in0[i + 8] +
               w9 * in0[i + 9] + w10 * in0[i + 10] + w11 * in0[i + 11] +
               w12 * in0[i + 12] + w13 * in0[i + 13] + w14 * in0[i + 14] +
               w15 * in0[i + 15] + w16 * in0[i + 16] + w17 * in0[i + 17] +
               w18 * in0[i + 18] + w19 * in0[i + 19] + w20 * in0[i + 20] +
               w21 * in0[i + 21] + w22 * in0[i + 22] + w23 * in0[i + 23] +
               w24 * in0[i + 24] + w25 * in0[i + 25] + w26 * in0[i + 26] +
               w27 * in0[i + 27] + w28 * in0[i + 28] + w29 * in0[i + 29] +
               w30 * in0[i + 30] + w31 * in0[i + 31] + w32 * in0[i + 32] +
               w33 * in0[i + 33] + w34 * in0[i + 34] + w35 * in0[i + 35] +
               w36 * in0[i + 36] + w37 * in0[i + 37] + w38 * in0[i + 38] +
               w39 * in0[i + 39] + w40 * in0[i + 40];
    }
  }
}
void dconv(const float *in, const int n, const float complex *w, float *out) {
  kconv(in, n, w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7], w[8], w[9],
        w[10], w[11], w[12], w[13], w[14], w[15], w[16], w[17], w[18], w[19],
        w[20], w[21], w[22], w[23], w[24], w[25], w[26], w[27], w[28], w[29],
        w[30], w[31], w[32], w[33], w[34], w[35], w[36], w[37], w[38], w[39],
        w[40], out);
}
