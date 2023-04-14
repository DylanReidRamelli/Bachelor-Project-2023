import numpy as np
import matplotlib as plt


# All test are hardcoded.

# Takes an array of x_values and return an array of y_values that 
# are the x_values evaluated with a function f.
# @param A
def f(A):
    Y = np.zeros_like(A)
    for i in range(0,len(Y)):
        if i >= 3 and i <= 4:
            Y[i] = 1
        else:
            Y[i] = 0
    return Y



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

def cubic_spline_model(x,k, delta):
    if abs(x) >= 0 and abs(x) <1:
        return 2 / 3 - abs(x - k - delta)^2 + (abs(x - k - delta)^3)/2
    elif abs(x) >= 1 and abs(x) <2:
        return (2 - abs(x - k - delta)^3)/6
    else:
        return 0
# Main method for running tests and or other things.
def main():
    test_f()
    test_linear_interpolation()


if __name__ == '__main__':
    main()
