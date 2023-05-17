import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, datasets

# Constants
N = 100
DELTA = 0.9
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

	x = np.linspace(0, 2, N)
	f_x = y_l(x)

	# Plot original function
	ax.plot(x,f_x)


	# Calculate Fourier transform of the Geometric progression function: y(k) = 2^-k
	G = np.zeros(N, dtype=complex)
	for i in range(0,N):
	    G[i] = (1 - fourier_geometric_progression(i)**N) / (1 - fourier_geometric_progression(i))


	N_prime = N if N % 2 == 0 else N+1

	# for i in range(0,)

	for k in range(0,int(N_prime/2)):
		G[k] = np.exp(-2j * np.pi * DELTA * k / N) * G[k]
	for k in range(int(N_prime/2), N):
		G[k] = np.exp(-2j * np.pi * DELTA * (k - N) / N) * G[k]


	for k in range(0,N):
		if N % 2 == 0 and k == N/2:
			G[k] = np.exp(1j*np.pi * (DELTA % 1)) * G[k]
		else:
			G[k] = G[k] 


	out_inverse = np.zeros(N, dtype=complex)
	out_inverse = np.fft.ifft(G)
	ax.plot(x, out_inverse.real)

	plt.show()


def fourier_image_shift():
	data = np.fromfile("../../Images/data_rectangle.raw", dtype=np.float32)
	delta = 30

	a = np.tan(delta/2)
	b = -np.sin(delta)

	nx = 300
	ny = 200


	N = len(data)
	F = np.zeros(N, dtype=complex)
	F = np.fft.fft(data)


	# Shear x axis
	N_prime = N if N % 2 == 0 else N+1

	for k in range(0,int(N_prime/2)):
		F[k] = np.exp(-2j * np.pi * a * k / N) * F[k]
	for k in range(int(N_prime/2), N):
		F[k] = np.exp(-2j * np.pi * a * (k - N) / N) * F[k]


	for k in range(0,N):
		if N % 2 == 0 and k == N/2:
			F[k] = np.exp(1j*np.pi * (a % 1)) * F[k]
		else:
			F[k] = F[k] 


	final_output = np.zeros(N, dtype=complex)
	final_output = np.fft.ifft(F)

	# final_output = np.reshape(final_output.real,(200,300))

	plt.title("Original Image")
	plt.xlabel("X pixel scaling.")
	plt.ylabel("Y pixel scaling.")

	final_output = np.reshape(final_output, (200,300))

	# Visualize the data as an image
	plt.imshow(final_output.real, cmap='gray')
	# plt.imshow(np.reshape(data, (200,300)), cmap='gray')
	plt.show()


def image_test():
	im = np.fromfile("../../Images/data_rectangle.raw", dtype=np.float32)
	im = np.reshape(im, (200,300))

	# Pad array such that image is twice the original size
	# to avoid Fourier wraparound artefact
	impad = np.pad(im,(200,300))

	# Apply fftshift in real space before fft2 (!)
	fft = np.fft.fftshift(impad)

	# Do the regular fft --> fftshift --> rotate --> ifftshift --> ifft2
	fft = np.fft.fft2(fft)
	fft = np.fft.fftshift(fft)
	fft = ndimage.rotate(fft,30.7,reshape=False)
	fft = np.fft.ifftshift(fft)
	out = np.fft.ifft2(fft)

	# Apply ifftshift in real space after ifft2 (!)
	out = np.fft.ifftshift(out)

	# Crop back to original size
	out=out[200:-200,300:-300]

	# Take absolute value
	im_rotated = abs(out)

	plt.imshow(im_rotated.real, cmap='gray')
	# plt.imshow(np.reshape(data, (200,300)), cmap='gray')
	plt.show()


def main():
	# fourier_transform_with_shift()
	image_test()
	# fourier_image_shift()
if __name__ == '__main__':
	main()