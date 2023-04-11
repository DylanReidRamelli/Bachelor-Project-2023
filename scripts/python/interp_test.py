# # # import numpy as np
# # # import matplotlib.pyplot as plt


# # # def cubic_spline_model(x):
# # #     if np.abs(x) < 1 and np.abs(x) >= 0:
# # #         return 2/3 - np.abs(x) ^ 2 + (np.abs(x) ^ 3)/2
# # #     elif np.abs(x) < 2 and np.abs(x) >= 1:
# # #         return (2 - np.abs(x) ^ 3)/6
# # #     else:
# # #         return 0


# # # def f(x):
# # #     if x <= 4 and x >= 3:
# # #         return 1
# # #     else:
# # #         return 0


# # # def run_example():
# # #     max = 6
# # #     o_immagine = np.linspace(0, max, 1000)

# # #     for i in range(0, len(o_immagine)):
# # #         o_immagine[i] = f(o_immagine[i])

# # #     print(o_immagine)

# # #     plt.plot(np.linspace(0, 6, 1000), o_immagine)

# # #     interp_domain = np.linspace(0, 6, 1000)
# # #     y = piecewise_linear_model(interp_domain)

# # #     plt.plot(interp_domain, y, label='Interpolation points')
# # #     plt.show()


# # # def main():
# # #     run_example()


# # # if __name__ == '__main__':
# # #     main()
# # import numpy as np
# # import matplotlib.pyplot as plt


# # def linear_bspline(x):
# #     if np.abs(x) < 1.0:
# #         return 1.0 - np.abs(x)
# #     else:
# #         return 0.0


# # def linear_spline_model(x):
# #     if np.abs(x) < 2.0:
# #         return linear_bspline(x + 1.0)
# #     else:
# #         return 0.0


# # def f(x):
# #     if x <= 4 and x >= 3:
# #         return 1
# #     else:
# #         return 0


# # def run_example():
# #     max = 6
# #     o_immagine = np.linspace(0, max, 1000)

# #     for i in range(0, len(o_immagine)):
# #         o_immagine[i] = f(o_immagine[i])

# #     plt.plot(np.linspace(0, 6, 1000), o_immagine, label='Original Function')

# #     interp_domain = np.linspace(0, 6, 1000)
# #     y = np.zeros_like(interp_domain)
# #     for i in range(len(interp_domain)):
# #         y[i] = f(interp_domain[i])

# #     print(y)
# #     for i in range(len(interp_domain)):
# #         y[i] = linear_spline_model(i)

# #     print(y)

# #     plt.plot(interp_domain, y, label='Linear Spline')
# #     plt.legend()
# #     plt.show()


# # def main():
# #     run_example()


# # if __name__ == '__main__':
# #     main()
# import numpy as np
# import matplotlib.pyplot as plt


# def linear_spline_model(x):
#     if x < 1:
#         return 1 - x
#     elif x < 2:
#         return x - 1
#     else:
#         return 0


# def f(x):
#     return np.logical_and(x >= 3, x <= 4).astype(int)


# def run_example():
#     max = 6
#     o_immagine = np.linspace(0, max, 1000)

#     for i in range(0, len(o_immagine)):
#         o_immagine[i] = f(o_immagine[i])

#     # plt.plot(np.linspace(0, 6, 1000), o_immagine)

#     interp_domain = np.linspace(0, 6, 1000)
#     y = f(interp_domain)
#     print(y)
#     for i in range(len(y)):
#         y[i] = linear_spline_model(y[i])

#     plt.plot(interp_domain, y, label='Linear Spline')
#     plt.legend()
#     plt.show()


# def main():
#     run_example()


# if __name__ == '__main__':
#     main()
import numpy as np
import matplotlib.pyplot as plt


def b(x):
    if abs(x) < 1:
        return 1 - abs(x)
    else:
        return 0


def f(x):
    return np.sin(x)
    # if x >= 3 and x <= 4:
    #     return 1
    # else:
    #     return 0


# Define b(x) and f(x) as before
# Create a list of x values with 1000 samples between 0 and 6
x_values = np.linspace(0, 6, 1000)

y_values = []
for x in x_values:
    # if x >= 3 and x <= 4:
    #     y_values.append(1)
    # else:
    y = 0
    for i in range(-1, 2):
        y += f(x + i) * b(i - x)
    y_values.append(y)


plt.plot(x_values, y_values, label='Interpolated function')
plt.plot(x_values, [f(x) for x in x_values], label='Original function')
plt.legend()
plt.show()
