import numpy as np

def fourier_transform_N():
	N = 4
	delta = 1.55
	k = np.linspace(0,N-1)
	g_k = k - delta
	h_k = np.zeros_like(g_k)
	m = np.floor(N/2)+1
	m = 1

	for i in range(0,len(g_k)):
		h_k[i] = g_k[i]*np.exp(1)**(-1j*(2*np.pi/N) * k[i] * m)

	print(k)
	print(h_k)
def main():
	fourier_transform_N()
if __name__ == '__main__':
	main()