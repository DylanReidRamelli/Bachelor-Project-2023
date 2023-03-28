import numpy as np
import matplotlib.pyplot as plt

# Sample input array
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
plt.plot(x)
plt.show()

# Perform FFT
X = np.fft.fft(x)


plt.plot(X)
plt.show()
print(X)





# # Display original and shifted signals
# print('Original signal:')
# print(x)
# print('Shifted signal:')
# print(x_shifted.real)
