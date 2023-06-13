#include <complex.h>
// TODO make sure division is correct.
/**
 * @param i, index in frequency domain.
 * @param n, number of samples.
 */
int wavenum(const int i, const int n);

/**
 * @param H, array of size H_size that contains 0's.
 * @param H_size, size of input array.
 * @param M, Size of integral.
 */
void create_filter(float complex *H, const int H_size, const float M);

/**
 * @param L, input array for store the phase shift.
 * @param H_size, size of the filter.
 * @param shift, amount to shift.
 */
void create_phase_shift(float complex *L, const int H_size, const float shift);

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
                  const int H_size, const int M);
