import numpy as np
import matplotlib.pyplot as plt
import sys

np.set_printoptions(threshold=sys.maxsize)



def _my_shear(A,c,):

    G = np.fft.fft(A)
    print(G)


    # N_prime = N if N % 2 == 0 else N+1

    # for k in range(0, int(N_prime/2)):
    #     G[k] = np.exp(-2j * np.pi * DELTA * k / N) * G[k]
    # for k in range(int(N_prime/2), N):
    #     G[k] = np.exp(-2j * np.pi * DELTA * (k - N) / N) * G[k]

    # for k in range(0, N):
    #     if N % 2 == 0 and k == N/2:
    #         G[k] = np.exp(1j*np.pi * (DELTA % 1)) * G[k]
    #     else:
    #         G[k] = G[k]




def _fft_shear(arr, arr_ori, c, ax, pad=0, shift_ini=True):
    ax2 = 1-ax % 2
    
    # print("ax2: ", ax2)
    # print(arr_ori.shape[ax2])
    freqs = np.fft.fftfreq(arr_ori.shape[ax2])
    # print("freqs: ", freqs)
    sh_freqs = np.fft.fftshift(freqs)
    # print("sh_freqs: ", sh_freqs)
    arr_u = np.tile(sh_freqs, (arr_ori.shape[ax], 1))
    
    # print("arr_u: ", arr_u)
    # print(arr_u.shape)
    if ax == 1:
        arr_u = arr_u.T

    # print("arr_u: ", arr_u)
    # print(arr_u.shape)

    # print("sx: ", arr)
    s_x = np.fft.fftshift(arr)
    # print("s_x after spatial domain shift: ", s_x)
    s_x = np.fft.fft(s_x)
    # print("s_x after fft: ", s_x)
    s_x = np.fft.fftshift(s_x)
    # print("s_x after shift freq domain: ", s_x)




    s_x = np.exp(-2j*np.pi*c*arr_u*arr_ori)*s_x
    s_x = np.fft.fftshift(s_x)
    s_x = np.fft.ifft(s_x, axis=ax)
    s_x = np.fft.fftshift(s_x)

    return s_x

im = np.fromfile("../../Images/data_rectangle.raw", dtype=np.float32)

N = len(im)
ANGLE = 30
NX = 200
NY = 300
a = np.tan(np.deg2rad(ANGLE)/2)
b = - np.sin(np.deg2rad(ANGLE))


# Transform back to 2D array
im = np.reshape(im, (NX, NY))


ori_y, ori_x = im.shape
arr_xy = np.mgrid[0:ori_y, 0:ori_x]
arr_y = arr_xy[0]-100
arr_x = arr_xy[1] - 150
# print(arr_xy)
# print(arr_xy.shape)

# print(np.fft.fftfreq(4))


print(arr_x)
print(arr_x.shape)



s_x = _fft_shear(im, arr_x, a, ax=1, pad=0)
# s_x = _fft_shear(s_x, arr_y, b, ax=0, pad=0)
# s_x = _fft_shear(s_x, arr_x, a, ax=1, pad=0)

# print(s_x.shape)


fix, ax = plt.subplots()

ax.imshow(s_x.real)

plt.show()

