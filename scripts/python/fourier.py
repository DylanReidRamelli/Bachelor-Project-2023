import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, datasets

# Constants
N = 100
DELTA = 1.5
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

	x = np.linspace(0, 20, N)
	f_x = np.cos(x)

	# Plot original function
	ax.plot(x,f_x)


	F = np.fft.fftshift(f_x)
	G = np.fft.fft(F)
	# G = np.fft.fftshift()
	
	
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
	out_inverse = np.fft.ifftshift(out_inverse)
	ax.plot(x, out_inverse.real)

	plt.show()


def fourier_image_shift():
	data = np.fromfile("../../Images/data_rectangle.raw", dtype=np.float32)
	delta = 30.5

	a = np.tan(delta/2)
	b = -np.sin(delta)

	nx = 300
	ny = 200


	N = len(data)
	F = np.zeros(N, dtype=complex)
	F = np.fft.fftshift(data)
	F = np.fft.fft(F)



	# Shear x axis
	N_prime = N if N % 2 == 0 else N+1

	for k in range(0,int(N_prime/2)):
		F[k] = np.exp(-2j * np.pi * delta * k / N) * F[k]
	for k in range(int(N_prime/2), N):
		F[k] = np.exp(-2j * np.pi * delta * (k - N) / N) * F[k]


	for k in range(0,N):
		if N % 2 == 0 and k == N/2:
			F[k] = np.exp(1j*np.pi * (delta % 1)) * F[k]
		else:
			F[k] = F[k] 


	F = np.fft.ifftshift(F)

	final_output = np.zeros(N, dtype=complex)
	final_output = np.fft.ifft(F)

	# final_output = np.fft.ifftshift(final_output)

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


	N = 7
	x = np.linspace(0,3 * np.pi, N)
	# x = np.random.rand(N,1)
	y = np.sin(x)


	print("Original:", y)
	print(np.fft.fftshift(y))

	im = np.fromfile("../../Images/circular_symmetric.raw", dtype=np.float32)
	im = np.reshape(im, (300,300))

	# Pad array such that image is twice the original size
	# to avoid Fourier wraparound artefact
	impad = np.pad(im,(300,300))

	# Apply fftshift in real space before fft2 (!)
	fft = np.fft.fftshift(im)
	# Do the regular fft --> fftshift --> rotate --> ifftshift --> ifft2
	fft = np.fft.fft2(fft)
	
	fft = np.fft.fftshift(fft)
	fft = ndimage.rotate(fft,30,reshape=False)
	# fft = np.fft.ifftshift(fft)

	out = np.fft.ifft2(fft)

	# # Apply ifftshift in real space after ifft2 (!)
	out = np.fft.ifftshift(out)

	# # Crop back to original size
	out = out[300:-300, 300:-300]

	# # Take absolute value
	im_rotated = abs(out)

	plt.imshow(im_rotated, cmap='gray')
	# plt.imshow(np.reshape(data, (200,300)), cmap='gray')
	plt.show()



def testing_solution():
	# Declare original function
	N = 20
	nx = 3 * np.pi
	x = np.linspace(0,nx, N)
	y = np.sin(x)



	# FORWARD FOURIER TRANSFORM

	# Plot original function.
	fig, ax = plt.subplots(3,3)
	ax[0,0].plot(x,y, marker = 'o')
	ax[0,0].title.set_text("Original cos function with N: "+ str(N) + " from 0 to: " + str(nx))



	o_fft_shift = np.fft.fftshift(y)
	ax[0,1].plot(x, o_fft_shift, marker ='o')
	ax[0,1].title.set_text("Original Function with fftshift applied.")

	# Pad array such that image is twice the original size
	# to avoid Fourier wraparound artefact
	# impad = np.pad(im,(300,300))



	# Normal fourier transform of the original fucntion.
	o_fft = np.fft.fft(y)
	ax[0,2].plot(x,o_fft, marker ='o')
	ax[0,2].title.set_text("Magnitude of Fourier transform without fft shift")


	# Do the regular fft --> fftshift --> rotate --> ifftshift --> ifft2
	s_fft = np.fft.fft(o_fft_shift)
	
	ax[1,0].plot(x,s_fft.real, marker='o')
	ax[1,0].title.set_text("Magnitude of Fourier transform with fftshift applied before")


	# Shift the already shifted fft 
	s2_fft = np.fft.fftshift(s_fft)
	ax[1,1].plot(x,s2_fft.real, marker='o')
	ax[1,1].title.set_text("Magnitude of Fourier transform with fftshift applied before and after the transform")


	DELTA = 0.5


	s2_fft_rotated = np.zeros_like(s2_fft)
	for i in range(0, N):
		s2_fft_rotated[i] = np.exp(-2j * np.pi * i * DELTA / N) * s2_fft[i]


	ax[1,2].plot(x,s2_fft_rotated.real, marker='o')
	ax[1,2].title.set_text("Magnitude of Fourier transform with fftshift applied before and after the transform and shifted by a phase of delta: " + str(DELTA))


	i_s2_fft_rotated_ishift = np.fft.ifftshift(s2_fft_rotated)
	ax[2,0].plot(x,i_s2_fft_rotated_ishift.real, marker='o')
	ax[2,0].title.set_text("Magnitude of the Fourier Transform after rotation and 1 ifftshift")

	# Apply ifft without ifftshift at first.

	i_s2_fft_rotated = np.fft.ifft(i_s2_fft_rotated_ishift)
	ax[2,1].plot(x,i_s2_fft_rotated.real, marker='o')
	ax[2,1].title.set_text("Magnitude of Inverse Fourier transform ")

	# ifftshift in the spatial domain
	i_s2_fft_rotated_shift = np.fft.ifftshift(i_s2_fft_rotated)
	ax[2,2].plot(x,i_s2_fft_rotated_shift.real, marker='o')
	ax[2,2].title.set_text("Magnitude of Inverse Fourier transform with ifft shift applied after inverse")

	plt.show()
	plt.legend()


def main():
	# fourier_transform_with_shift()
	# image_test()
	# fourier_image_shift()
	testing_solution()
if __name__ == '__main__':
	main()