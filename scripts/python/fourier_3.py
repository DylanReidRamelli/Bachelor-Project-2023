import numpy as np
import matplotlib.pyplot as plt
import sys

np.set_printoptions(threshold=sys.maxsize)



N = 100
ANGLE = 35
ANGLE_git = np.deg2rad(ANGLE)
a = np.tan(np.deg2rad(ANGLE)/2)
b = - np.sin(np.deg2rad(ANGLE))

    


def _my_fft(A, c, NX, NY):
    R = np.array([])
    R = np.fft.fftshift(A)
    R = np.fft.fft(R)
    
    N = NX * NY
    
   
    N_prime = N if N % 2 == 0 else N+1

    for k in range(0, int(N_prime/2)):
        freq = k / N
        R[k] = np.exp(-2j * np.pi *c * freq) * R[k]
    for k in range(int(N_prime/2), N):
        freq = (k-N)/N
        R[k] = np.exp(-2j * np.pi *c * freq) * R[k]

    # for k in range(0, N):
    #     if N % 2 == 0 and k == N/2:
    #         R[k] = np.exp(1j*np.pi *(c % 1)) * R[k]
    #         print(k)
    #     else:
    #         R[k] = R[k]
            
            
    R = np.fft.ifft(R)
    
    R = np.fft.ifftshift(R)

    return R



def _fft_example(A, c, arr_ori, ax=1):
    ax2 = 1-ax % 2
    freqs = np.fft.fftfreq(arr_ori.shape[ax2])

    sh_freqs = np.fft.fftshift(freqs)

    arr_u = np.tile(sh_freqs, (arr_ori.shape[ax], 1))
    

    if ax == 1:
        arr_u = arr_u.T

    s_x = np.fft.fftshift(A)

    s_x = np.fft.fft(s_x)

    s_x = np.fft.fftshift(s_x)

    s_x = np.exp(-2j*np.pi*c*arr_u*arr_ori)*s_x


    s_x = np.fft.fftshift(s_x)
    s_x = np.fft.ifft(s_x)
    s_x = np.fft.fftshift(s_x)

    return s_x

# x = np.linspace(0, 8* np.pi, N)
# y = np.sin(x)
# arr_x = np.linspace(0,N-1,N)
# N_plots = 10

# fig, ax = plt.subplots(2,1)


# ax[0].plot(x, _fft_example(y,a,arr_x).real)
# ax[0].plot(x,_my_fft(y, 0).real)


im = np.fromfile("../../Images/data_rectangle.raw", dtype=np.float32)
NX = 200
NY = 300
result = _my_fft(im, a, NX, NY)
result = np.reshape(result, (NX,NY))



plt.imshow(result.real, cmap='gray')

plt.show()