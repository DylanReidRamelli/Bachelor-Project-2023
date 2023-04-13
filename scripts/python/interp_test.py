import matplotlib.pyplot as plt
import numpy as np


def f(x):
    g = np.zeros_like(x)
    for i in range(0, len(x)):
        if x[i] >= 2 and x[i] <= 4:
            g[i] = 1
        else:
            g[i] = 0

    return g


def interp_shift(f, delta):

    r = np.zeros_like(f)
    for x in range(0, len(r)):
        for k in range(0, len(r)):
            if x != k and abs(x - k) <= 1:
                print("x", x)
                slope = (f[k] - f[x]) / (k - x)
                y = f[x] + (delta) * slope
                r[x] = y

    return r


n_original_sample = 11

x = np.linspace(0, 10, num=n_original_sample)
g = f(x)

plt.plot(x, g, '-', label="Original function", marker='o')

# shift
delta = 4
n_samples_mult = 1

result = interp_shift(g, delta)

plt.plot(x, result, label="Interpolated function.")

plt.annotate("Delta: " + str(delta), xy=(9, 0.5))
plt.annotate("N_Samples_Interpolation: " + str(len(x)), xy=(9, 0.4))
plt.annotate("N_Samples_Original: " +
             str(n_original_sample), xy=(9, 0.3))
plt.legend()
plt.show()
