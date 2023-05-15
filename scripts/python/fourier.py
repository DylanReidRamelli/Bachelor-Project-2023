import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 100
DELTA = 1.55
R = 2

# Geometric progression function: y_l(x) = R^{-x}
def y_l(A):
    out = np.zeros(len(A))
    for i in range(0, len(A)):
        out[i] = R**-A[i]
    return out


def fourier_geometric_progression(k):
	return np.exp(-2j * np.pi * k / N) * R**-1


def fourier_transform_with_shift():

	fig, ax = plt.subplots()

	x = np.linspace(0, 10, N)
	f_x = y_l(x)

	# Plot original function
	ax.plot(x,f_x)


	# Calculate Fourier transform of the Geometric progression function: y(k) = 2^-k
	G = np.zeros(N, dtype=complex)
	for i in range(0,N):
	    G[i] = (1 - fourier_geometric_progression(i)**N) / (1 - fourier_geometric_progression(i))


	for k in range(0,N):
		e = np.exp(-2j * np.pi * k * DELTA/N)
		if k < N - k:
			e = np.exp(-2j * np.pi * DELTA  * k / N)
		elif k > N - k:
			e = np.exp(-2j * np.pi * DELTA  * (k-N) / N)
		elif k == N - k and k == N/2:
			e = np.cos(2 * np.pi * DELTA/2)
		G[k] = G[k] * e


	out_inverse = np.zeros(N, dtype=complex)
	out_inverse = np.fft.ifft(G)
	ax.plot(x, out_inverse.real)

	plt.show()

def main():
	fourier_transform_with_shift()
if __name__ == '__main__':
	main()