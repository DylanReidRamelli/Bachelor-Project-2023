import numpy as np
import matplotlib.pyplot as plt


# All test are hardcoded.

# Takes an array of x_values and return an array of y_values that 
# are the x_values evaluated with a function f.
# @param A
def f(A):
    Y = np.zeros_like(A)
    Y = np.cos(A)
    # for i in range(0,len(Y)):
    #     if i >= 3 and i <= 4:
    #         Y[i] = 1
    #     else:
    #         Y[i] = 0
    return Y


# Same thing as above but for just one value x.
def f_s(x):
    # if x >= 3 and x <= 4:
    #     return 1
    # else:
    #     return 0

    return np.cos(x)



def test_f():
    domain_size = 10

    # Variable for controlling how manu subsamples we want to create
    refined = 2

    # Basiccally length of the domain array.
    sample_size = (domain_size + 1) * refined
    x = np.linspace(0,domain_size, sample_size)

    # Apply function f to x
    y = f(x)

    print("X_values: " ,x)
    print("Y_values: " ,y)

    # TODO: Create test to see if function, works correctly.
    # Since it is a simple function for now I will assume it is correct.


def keys_cubic_kernel(x,a):
    if abs(x) >= 0 and abs(x) <1:
        return (a+2)*(abs(s)**3)-(a+3)*(abs(s)**2)+1
    elif abs(x) >= 1 and abs(x) <2:
        return a*(abs(s)**3)-5*(abs(s)**2)+8*abs(s)-4
    else:
        return 0



# Kernel of the cubic spline interpolation 
def cubic_spline_kernel(x):
    if abs(x) >= 0 and abs(x) <1:
        return 2 / 3 - abs(x)^2 + (abs(x)^3)/2
    elif abs(x) >= 1 and abs(x) <2:
        return (2 - abs(x)^3)/6
    else:
        return 0



# Returns y value given an x value and two points
# Interpolate the two points with linear intepolation then find the 
# y value with line equation: m*x + a
# m = slope
# x = input x 
# a = position
def linear_interpolation(x_1, x_2, y_1, y_2, x):
    if abs(x_2) != abs(x_1):
        slope = (y_2 - y_1) / (x_2 - x_1)
        r = slope * (x - x_1) + y_1
        return r

    else:
        print("x_1 and x_2 cannot be the same.")
        return None

# Testing the linear inteprolation with two points.
def test_linear_interpolation():
    x = np.array([3,2])
    y = np.array([5,6])

    point = 4

    r = linear_interpolation(x[0], x[1], y[0], y[1], point)

    print("Given points: x: " + str(x) + " and y: " + str(y) + " the points we want is: " + str(point) + " and the result is: "+ str(r))

# Definition of linear piecewise model, modified for the shift.
def linear_piecewise_model(x,k,delta):
    if abs(x) < 1:
        return 1 - abs(x - k - delta)
    else:
        return 0


def test_shift_function():
    domain_size = 10

    # Variable for controlling how manu subsamples we want to create
    refined = 2

    # Basiccally length of the domain array.
    sample_size = (domain_size + 1) * refined

    # o stands for original function.
    o_x = np.linspace(0,domain_size, sample_size)
    o_y = np.sin(o_x)


    plt.plot(o_x,o_y, marker= 'o', label= "Original function: sin(x)")

    # #############################################################
    delta = 2 * np.pi


    # Works for int samples
    # Variable for controlling how manu subsamples we want to create
    refined = 2
    # Basiccally length of the domain array.
    sample_size = (domain_size + 1) * refined

    # s stands for shifted 
    s_x = np.linspace(-delta,domain_size - delta, sample_size)
    # We need now to evaluate the function for samples that were not use before
    # such as f(x) = f(x - delta).
    s_y = np.zeros_like(s_x)


    for i in range(0,len(s_x)):
        x_1 = s_x[i]


    # Not correct. TODO: FIX THIS!
    # for x in range(0,len(s_x)):
    #     # x_1 = np.floor(s_x[x])
    #     # x_2 = np.ceil(s_x[x])
    #     x_1 = s_x[x]
    #     if x+1 >= len(s_x):
    #         x_2 = x_1
    #     else:  
    #         x_2 = s_x[x+1]

    #     print("Shifted x: " + str(s_x[x]))
    #     print("Floor x: " + str(x_1))
    #     print("Ceil x: " + str(x_2))

    #     if x_1 != x_2:
    #         y_1 = f_s(x_1)
    #         y_2 = f_s(x_2)
    #         y = linear_interpolation(x_1, x_2, y_1, y_2, s_x[x])
    #         print("F(x): " + str(y))
    #         s_y[x] = y
    #     else:
    #         print("SUP")
    #         s_y[x] = f_s(x_1)


    plt.plot(o_x, s_y, linestyle='--', marker= 'o', label="Shifted function: cos(x + 2 * pi)")
    plt.text(9, 0.5, "N_samples: " + str(sample_size))
    plt.legend()
    plt.show()


# Now it is interpolating between integer points so all 
# the values in between will be linear, that is why at the peaks 
# we a straight lines instead of a curve.
# Solutions could be to change the two interpolating points to not be 
# int values but something else.



# Main method for running tests and or other things.
def main():
    # test_f()
    # test_linear_interpolation()
    test_shift_function()


if __name__ == '__main__':
    main()