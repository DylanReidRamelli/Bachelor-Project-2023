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


def compute_kernel(angle):
    # Convert angle to radians
    angle = np.deg2rad(angle)

    # Compute filter kernel
    size = 2 * int(np.ceil(np.abs(angle))) + 1
    kernel = np.zeros((size, size))
    print(kernel)
    center = (size - 1) / 2
    epsilon = 1e-8
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            if x == 0 and y == 0:
                kernel[i, j] = 1
            else:

                # Sinc function on angle
                #
                kernel[i, j] = np.sin(np.pi * x * np.sin(angle) + np.pi * y * np.cos(angle)) / (
                    np.pi * x * np.sin(angle) + np.pi * y * np.cos(angle) + epsilon)
                if x == 0:
                    kernel[i, j] *= (np.sin(np.pi * y / size) /
                                     (np.pi * y / size))
                elif y == 0:
                    kernel[i, j] *= (np.sin(np.pi * x / size) /
                                     (np.pi * x / size))
                else:
                    kernel[i, j] *= (np.sin(np.pi * x / size) / (np.pi * x / size)) * \
                        (np.sin(np.pi * y / size) / (np.pi * y / size))
    return kernel


def rotate_image(image, angle):

    kernel = compute_kernel(angle)

    # Pad image with zeros
    pad_width = int(np.ceil(np.sqrt(2) * max(image.shape)))
    padded = np.pad(image, pad_width, mode='constant')

    # Compute 2D-Fourier transforms
    input_fft = fftpack.fft2(padded)
    kernel_fft = fftpack.fft2(kernel, shape=padded.shape)

    # Apply the kernel to the frequency function of the image.
    filtered = input_fft * kernel_fft

    # Go back to the spatial domain.
    filtered = fftpack.ifft2(filtered)

    # Extract rotated image
    # ndimage.rotate: array is rotated and the interpolated the points using spline interpolation.
    rotated = ndimage.rotate(filtered.real, -np.rad2deg(angle), reshape=False)

    # Crop to original size
    cropped = rotated[pad_width:-pad_width, pad_width:-pad_width]
    return cropped


def sinc_kernel(size, k):
    kernel = np.zeros(size)
    return np.sinc(kernel * k)


def translate_1d_signal(angle):
    # compute_kernel(angle)

    domain_size = 10
    domain = np.linspace(0, domain_size, domain_size)
    result = np.sin(domain)

    plt.plot(domain, result)
    plt.show()
    # pad_width = int(np.ceil(np.sqrt(2) * max(domain_size)))
    # padded = np.pad(result, domain_size, mode='constant')
    # print(padded)

    # input_fft = fftpack.fft(padded)
    input_fft = fftpack.fft(result)
    kernel_fft = fftpack.fft(sinc_kernel(domain_size, 2))

    filtered = input_fft * kernel_fft

    filtered = fftpack.ifft(filtered)

    # Extract rotated image
    # ndimage.rotate: array is rotated and the interpolated the points using spline interpolation.
    # rotated = ndimage.rotate(filtered.real, -np.rad2deg(angle), reshape=False)
    plt.plot(domain, filtered)
    plt.show()
    print(filtered)


def main():
    translate_1d_signal(45)
    # image_path = "../../Images/wrapped_sinusoid.raw"
    # nx = 256
    # ny = 256
    # data = np.fromfile(image_path, dtype=np.float32)
    # data = np.reshape(data, (ny, nx))
    # result = rotate_image(data, 90)

    # plt.imshow(result, cmap='gray')
    # plt.show()
    # plt.savefig("fourier_rotate.png")


if __name__ == '__main__':
    main()
