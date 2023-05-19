import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


g = [0, np.pi / 2, np.pi]
g_x = np.cos(g)

F_g_x = np.fft.fft(g_x)
print("FOurier transform of not shifted frequancies: \n", F_g_x)

fft_shift_g_x = np.fft.fftshift(g_x)

print("Shifted values: \n", fft_shift_g_x)

F_fft_shift_g_x = np.fft.fft(fft_shift_g_x)

print("FOurier transform of not shifted frequancies: \n", F_fft_shift_g_x)
