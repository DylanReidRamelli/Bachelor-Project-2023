import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

# Constants
N = 100
DELTA = 12.5
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

    x = np.linspace(0, 6 * np.pi, N)
    f_x = np.cos(x)

    # Plot original function
    ax.plot(x, f_x)

    # F = np.fft.fftshift(f_x)
    G = np.fft.fft(f_x)
    # G = np.fft.fftshift(G)

    N_prime = N if N % 2 == 0 else N+1

    for k in range(0, int(N_prime/2)):
        G[k] = np.exp(-2j * np.pi * DELTA * k / N) * G[k]
    for k in range(int(N_prime/2), N):
        G[k] = np.exp(-2j * np.pi * DELTA * (k - N) / N) * G[k]

    for k in range(0, N):
        if N % 2 == 0 and k == N/2:
            G[k] = np.exp(1j*np.pi * (DELTA % 1)) * G[k]
        else:
            G[k] = G[k]

    out_inverse = np.zeros(N, dtype=complex)
    # out_inverse = np.fft.ifftshift(G)
    out_inverse = np.fft.ifft(G)
    # out_inverse = np.fft.ifftshift(out_inverse)
    ax.plot(x, out_inverse.real, marker='o')

    plt.show()


def _fft_shear(arr, arr_ori, c, ax, pad=0, shift_ini=True):
    ax2 = 1-ax % 2
    freqs = np.fft.fftfreq(arr_ori.shape[ax2])
    sh_freqs = np.fft.fftshift(freqs)
    arr_u = np.tile(sh_freqs, (arr_ori.shape[ax], 1))
    if ax == 1:
        arr_u = arr_u.T
    s_x = np.fft.fftshift(arr)
    s_x = np.fft.fft(s_x, axis=ax)
    s_x = np.fft.fftshift(s_x)
    s_x = np.exp(-2j*np.pi*c*arr_u*arr_ori)*s_x
    s_x = np.fft.fftshift(s_x)
    s_x = np.fft.ifft(s_x, axis=ax)
    s_x = np.fft.fftshift(s_x)

    return s_x


def fourier_image_shift():
    data = np.fromfile("../../Images/data_rectangle.raw", dtype=np.float32)
    angle = 31
    a = np.tan(np.deg2rad(angle)/2)
    b = -np.sin(np.deg2rad(angle))

    nx = 300
    ny = 200

    # data = np.reshape(data, (200, 300))
    # data = np.pad(data, (200, 300))

    # data = np.reshape(data, (560000,))

    N = len(data)

    F = np.zeros(N, dtype=complex)

    data = np.reshape(data, (200, 300))
    ori_y, ori_x = data.shape
    arr_xy = np.mgrid[0:ori_y, 0:ori_x]
    arr_y = arr_xy[0]-150
    arr_x = arr_xy[1]-100

    F = _fft_shear(data, arr_x, a, ax=1, pad=0)
    F = _fft_shear(F, arr_y, b, ax=0, pad=0)
    F = _fft_shear(F, arr_x, a, ax=1, pad=0)

    # F = np.fft.fft(data)
    # for i in range(0, N):
    #     print(F[i])

    # plt.plot(np.linspace(0, N), F.real)

    # F = ndimage.rotate(F, 30, reshape=False)

    # Shear x axis
    # N_prime = N if N % 2 == 0 else N+1

    # for k in range(0, int(N_prime/2)):
    #     F[k] = np.exp(-2j * np.pi * delta * k / N) * F[k]
    # for k in range(int(N_prime/2), N):
    #     F[k] = np.exp(-2j * np.pi * delta * (k - N) / N) * F[k]

    # for k in range(0, N):
    #     if N % 2 == 0 and k == N/2:
    #         F[k] = np.exp(1j*np.pi * (delta % 1)) * F[k]
    #     else:
    #         F[k] = F[k]

    # final_output = np.zeros(N, dtype=complex)
    # final_output = np.fft.ifft(F)

    # final_output = final_output[300:-300]

    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    # final_output = np.reshape(final_output, (700, 800))
    # final_output = final_output[200:-300, 200:-300]
    # print(final_output.shape)
    # Visualize the data as an image
    # final_output = np.reshape(final_output, (200, 300))
    plt.imshow(F.real)
    # plt.imshow(np.reshape(data, (200,300)), cmap='gray')
    plt.show()


# def image_test():

#     N = 7
#     x = np.linspace(0, 3 * np.pi, N)
#     # x = np.random.rand(N,1)
#     y = np.sin(x)

#     print("Original:", y)
#     print(np.fft.fftshift(y))

#     im = np.fromfile("../../Images/wrapped_sinusoid.raw", dtype=np.float32)
#     im = np.reshape(im, (256, 256))

#     # Pad array such that image is twice the original size
#     # to avoid Fourier wraparound artefact
#     impad = np.pad(im, (256, 256))

#     # Apply fftshift in real space before fft2 (!)
#     fft = np.fft.fftshift(impad)
#     # Do the regular fft --> fftshift --> rotate --> ifftshift --> ifft2
#     fft = np.fft.fft2(fft)

#     fft = np.fft.fftshift(fft)
#     fft = ndimage.rotate(fft, 30, reshape=False)
#     # fft = np.fft.ifftshift(fft)

#     out = np.fft.ifft2(fft)

#     # # Apply ifftshift in real space after ifft2 (!)
#     out = np.fft.ifftshift(out)

#     # # Crop back to original size
#     out = out[256:-256, 256:-256]

#     # # Take absolute value
#     im_rotated = abs(out)

#     plt.imshow(im_rotated, cmap='gray')
#     # plt.imshow(np.reshape(data, (200,300)), cmap='gray')
#     plt.show()


def testing_solution():
    # Declare original function
    N = 20
    nx = 3 * np.pi
    x = np.linspace(0, nx, N)
    y = np.sin(x)

    # FORWARD FOURIER TRANSFORM

    # Plot original function.
    fig, ax = plt.subplots(3, 3)
    ax[0, 0].plot(x, y, marker='o')
    ax[0, 0].title.set_text(
        "Original cos function with N: " + str(N) + " from 0 to: " + str(nx))

    o_fft_shift = np.fft.fftshift(y)
    ax[0, 1].plot(x, o_fft_shift, marker='o')
    ax[0, 1].title.set_text("Original Function with fftshift applied.")

    # Pad array such that image is twice the original size
    # to avoid Fourier wraparound artefact
    # impad = np.pad(im,(300,300))

    # Normal fourier transform of the original fucntion.
    o_fft = np.fft.fft(y)
    ax[0, 2].plot(x, o_fft, marker='o')
    ax[0, 2].title.set_text("Magnitude of Fourier transform without fft shift")

    # Do the regular fft --> fftshift --> rotate --> ifftshift --> ifft2
    s_fft = np.fft.fft(o_fft_shift)

    ax[1, 0].plot(x, s_fft.real, marker='o')
    ax[1, 0].title.set_text(
        "Magnitude of Fourier transform with fftshift applied before")

    # Shift the already shifted fft
    s2_fft = np.fft.fftshift(s_fft)
    ax[1, 1].plot(x, s2_fft.real, marker='o')
    ax[1, 1].title.set_text(
        "Magnitude of Fourier transform with fftshift applied before and after the transform")

    DELTA = 0.5

    s2_fft_rotated = np.zeros_like(s2_fft)
    for i in range(0, N):
        s2_fft_rotated[i] = np.exp(-2j * np.pi * i * DELTA / N) * s2_fft[i]

    ax[1, 2].plot(x, s2_fft_rotated.real, marker='o')
    ax[1, 2].title.set_text(
        "Magnitude of Fourier transform with fftshift applied before and after the transform and shifted by a phase of delta: " + str(DELTA))

    i_s2_fft_rotated_ishift = np.fft.ifftshift(s2_fft_rotated)
    ax[2, 0].plot(x, i_s2_fft_rotated_ishift.real, marker='o')
    ax[2, 0].title.set_text(
        "Magnitude of the Fourier Transform after rotation and 1 ifftshift")

    # Apply ifft without ifftshift at first.

    i_s2_fft_rotated = np.fft.ifft(i_s2_fft_rotated_ishift)
    ax[2, 1].plot(x, i_s2_fft_rotated.real, marker='o')
    ax[2, 1].title.set_text("Magnitude of Inverse Fourier transform ")

    # ifftshift in the spatial domain
    i_s2_fft_rotated_shift = np.fft.ifftshift(i_s2_fft_rotated)
    ax[2, 2].plot(x, i_s2_fft_rotated_shift.real, marker='o')
    ax[2, 2].title.set_text(
        "Magnitude of Inverse Fourier transform with ifft shift applied after inverse")

    plt.show()
    plt.legend()


def main():
    # fourier_transform_with_shift()
    # image_test()
    fourier_image_shift()
    # testing_solution()


if __name__ == '__main__':
    main()
