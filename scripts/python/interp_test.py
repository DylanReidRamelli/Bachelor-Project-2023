import numpy as np


def cubic_spline_model(x):
    if np.abs(x) < 1 and np.abs(x) >= 0:
        return 2/3 - np.abs(x) ^ 2 + (np.abs(x) ^ 3)/2
    elif np.abs(x) < 2 and np.abs(x) >= 1:
        return (2 - np.abs(x) ^ 3)/6
    else:
        return 0


def piecewise_linear_model(x):
    if np.abs(x) < 1:
        return 1 - np.abs(x)
    else:
        return 0


def sample_function(x):
    if x <= 4 and x >= 3:
        return 1
    else:
        return 0


def run_example():
    samples = 7
    o_domain = np.linspace(0, samples - 1, samples)
    o_immagine = np.zeros(samples)

    for i in range(0, len(o_domain)):
        o_immagine[i] = sample_function(o_domain[i])

    # Lets shift the function by delta = 1

    for i in range(0, samples):


def main():
    run_example()


if __name__ == '__main__':
    main()
