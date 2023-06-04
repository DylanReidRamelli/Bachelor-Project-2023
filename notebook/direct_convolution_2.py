import sys
import numpy as np
from matplotlib import pyplot as plt
from numpy import fft
from matplotlib.animation import FuncAnimation


# fig, ax = plt.subplots(2, 3)
fig, ax = plt.subplots()
def wavenum(i, N): return (i + N // 2) % N - N // 2


# def shift(angle, path):

# print(angle, path)

# angle = float(angle)
# path = str(path)
angle = 30.5

n = 100
filter_size = 90
x_n = np.arange(n)
x0 = n * 0.5
x = x_n < x0
x = np.array(x)
# ax[0, 0].plot(x_n, x)

integer_part = int(angle)
fractional_part = np.abs(np.mod(angle, 1))
DELTA = integer_part + fractional_part
########################
# Create filter kernel.
M = 3/2
H = np.zeros(filter_size, dtype=complex)
for i in range(filter_size):
    k = wavenum(i, filter_size)
    a = 2 * np.pi / filter_size * k * M
    H[i] = (np.sin(3*a/2))/a - (3 * np.pi *
                                np.cos(3 * a/2))/(9 * a**2 - np.pi**2)

H[0] = 3/2 + 3/np.pi
# H /= 3/2

# H = fft.fftshift(H)
# ax.stem(np.arange(filter_size), np.fft.fftshift(np.fft.ifft(H)), basefmt="gray")
ax.plot(np.arange(filter_size), H)
# ax[0, 0].plot(np.arange(filter_size), H)
# ax[0, 1].plot(np.arange(filter_size), np.fft.ifft(H))

########################

# G = np.zeros(filter_size)
# M = 0
# # we pick the support of the smoothing window depending on the fractional shift
# mydistance = np.abs(np.mod(DELTA, 1) - 0.5)
# if mydistance < 0.5 - 0.03125:
#     M = 1
# if mydistance < 0.5 - 0.0125:
#     M = 2
# if mydistance < 0.5 - 0.25:
#     M = 3
# print("M is ", M)
# if M:
#     for i in range(filter_size):
#         k = wavenum(i, filter_size)
#         a = 2 * np.pi / filter_size * k * M
#         # weighted average of (1/2 + 1/2 cos(pi / M * x))
#         if True:
#             if 4 * k == -filter_size or 4 * k == filter_size:
#                 G[i] += 1
#             else:
#                 G[i] += 2 * a * np.sin(a) / (np.pi**2 - a**2)
#         if True:
#             if i:
#                 G[i] += 2 * np.sin(a) / (a)
#             else:
#                 G[i] += 2
#         G[i] *= 0.5
#         if k == -filter_size//2:
#             print("fs: ", G[i], np.sin(-a) / -a)
# else:
#     G = np.ones(filter_size)
# ax[0, 1].plot(np.arange(filter_size), G)

# ########################
# # Create phase shift
L = np.zeros(filter_size, dtype=complex)
for i in range(filter_size):
    L[i] = np.exp(-2j * np.pi * fractional_part *
                    wavenum(i, filter_size)/filter_size)

# L = fft.fftshift(L)
# ax[0, 2].plot(np.arange(filter_size), L)
# #######################

# ########################
# # Multiply filter kernel by phase shift and do inverse transform.
h = np.fft.ifft(H * L)
# h = np.fft.fftshift(h)
# ax.plot(np.arange(filter_size), h)
# ########################

# ########################
# # Apply filter to signal in time domain to shift by the fractional amount.
z = np.zeros(n)
z = np.convolve(x, h, 'same')

# ax[1, 1].plot(np.arange(n), x)
# ax.plot(np.arange(n),x)
# ax.plot(np.arange(n), z)

########################
# Shift by the integer amount
z_final = np.zeros(n)
for i in range(n):
    z_final[i] = z[i-integer_part]

ax.plot(np.arange(n), z)
ax.plot(np.arange(n), x)
# plt.savefig(path)
plt.show()


# if __name__ == '__main__':
#     shift(sys.argv[1], sys.argv[2])
