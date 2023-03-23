import numpy as np
import matplotlib.pyplot as plt

# Sample input array
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Perform FFT
X = np.fft.fft(x)


plt.plot(X)
plt.show()
print(X)



# Create phase shift vector
# N = len(x)
# f = np.arange(N) / N
# phase_shift = 2 * np.pi * 13.33333 * f
# exp_phase_shift = np.exp(-1j * phase_shift)

# # Apply phase shift in frequency domain
# X_shifted = X * exp_phase_shift

# # Perform inverse FFT
# x_shifted = np.fft.ifft(X_shifted)

# # Display original and shifted signals
# print('Original signal:')
# print(x)
# print('Shifted signal:')
# print(x_shifted.real)
