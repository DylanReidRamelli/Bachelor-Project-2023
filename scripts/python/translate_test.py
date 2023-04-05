# import numpy as np
import matplotlib.pyplot as plt


# SHIFT = 30.25555


# #PHASE SHIFTING
# samples = 200

# # t = np.arange(0,np.pi, np.pi/samples)
# t = np.linspace(0,np.pi * 2, samples)

# f = 1

# g = np.sin(2 * np.pi  * f * t)

# g = np.convolve(g, np.array([SHIFT]), 'same')

# fig = plt.figure()
# plt.plot(t,g, label="Original Wave.")
# # plt.show()

# phase = SHIFT * 2* np.pi

# # y = np.sin(2*np.pi*f*t + phase)

# # plt.plot(y, label="Shifted wave.")
# # plt.legend()
# # plt.show()

# fourier_g = np.fft.fft(g)

# fourier_g = np.convolve(fourier_g, np.array([SHIFT,1,SHIFT]), 'same')

# fourier_g = np.fft.ifft(fourier_g)


# fig2 = plt.figure()
# plt.plot(t,fourier_g, label="Fourier of g")
# plt.show()

# # RESAMPLING AND INTERPOLATING


# # FREQUENCY DOMAIN


# # fft = np.fft.fft(np.sin(t + SHIFT))
# # freq = np.fft.fftfreq(t.shape[-1])
# # plt.plot(freq, fft.real, freq, fft.imag)
# # plt.show()
import numpy as np
from scipy import fftpack, ndimage

def rotate_image(image, angle):
    # Convert angle to radians
    angle = np.deg2rad(angle)
    
    # Compute filter kernel
    size = 2 * int(np.ceil(np.abs(angle))) + 1
    kernel = np.zeros((size, size))
    center = (size - 1) / 2
    epsilon = 1e-8
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            if x == 0 and y == 0:
                kernel[i, j] = 1
            else:
                kernel[i, j] = np.sin(np.pi * x * np.sin(angle) + np.pi * y * np.cos(angle)) / (np.pi * x * np.sin(angle) + np.pi * y * np.cos(angle) + epsilon)
                if x == 0:
                    kernel[i, j] *= (np.sin(np.pi * y / size) / (np.pi * y / size))
                elif y == 0:
                    kernel[i, j] *= (np.sin(np.pi * x / size) / (np.pi * x / size))
                else:
                    kernel[i, j] *= (np.sin(np.pi * x / size) / (np.pi * x / size)) * (np.sin(np.pi * y / size) / (np.pi * y / size))

    # Pad image with zeros
    pad_width = int(np.ceil(np.sqrt(2) * max(image.shape)))
    padded = np.pad(image, pad_width, mode='constant')

    # Compute Fourier transforms
    input_fft = fftpack.fft2(padded)
    kernel_fft = fftpack.fft2(kernel, shape=padded.shape)

    # Apply filter
    filtered = fftpack.ifft2(input_fft * kernel_fft)

    # Extract rotated image
    rotated = ndimage.rotate(filtered.real, -np.rad2deg(angle), reshape=False)

    # Crop to original size
    cropped = rotated[pad_width:-pad_width, pad_width:-pad_width]
    return cropped
def main():
	image_path = "../../Images/wrapped_sinusoid.raw"
	nx = 512
	ny = 512
	data = np.fromfile(image_path, dtype=np.float32)
	data = np.reshape(data, (ny, nx))
	print(data)
	result = rotate_image(data, 45)

	print(result)
	plt.imshow(result, cmap='gray')
	plt.show()

if __name__ == '__main__':
	main()

