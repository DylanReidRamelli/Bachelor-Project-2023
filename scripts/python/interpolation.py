import numpy as np
import matplotlib.pyplot as plt


############# INTERPOLATION MODELS

def cubic_interpolation_model(x):
    if abs(x) >= 0 and abs(x) < 1:
        return 2 / 3 - (abs(x))** 2 + (abs(x)**3)/2
    elif abs(x) >= 1 and abs(x) < 2:
        return ((2 - abs(x))**3)/6
    else:
        return 0



def linear_interpolation_model(x):
	if abs(x) < 1:
		return 1 - abs(x)
	else:
		return 0


############# TESTING INTERPOLATION


def test_linear_interpolation():
	x_samples = np.array([0,np.pi , 2 * np.pi , 3 * np.pi, 4 * np.pi])
	y_samples = np.cos(x_samples)
	h = x_samples[1] - x_samples[0]

	x_interp_samples = np.linspace(0, 4 * np.pi, 1000)
	y_interp_samples = np.zeros_like(x_interp_samples)

	for i in range(0, len(x_interp_samples)):
		for k in range(0, len(x_samples)):
			phi = linear_interpolation_model((x_interp_samples[i] - x_samples[k])/ h)
			f_n = y_samples[k] * phi
			y_interp_samples[i] += f_n


	plt.plot(x_samples, y_samples, label='Original Function', marker = 'o')
	plt.plot(x_interp_samples,y_interp_samples, label='Interpolated function', marker = 'o')
	plt.show()



def test_cubic_interpolation():
	x_samples = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	y_samples = np.cos(x_samples)

	x_interp_samples = np.linspace(0, 14, 100)
	y_interp_samples = np.zeros_like(x_interp_samples)

	for i in range(0, len(x_interp_samples)):
		for k in range(0, len(x_samples)):
			phi = cubic_interpolation_model(x_interp_samples[i] - x_samples[k])
			f_n = y_samples[k] * phi
			y_interp_samples[i] += f_n


	plt.plot(x_samples, y_samples, label='Original Function', marker = 'o')
	plt.plot(x_interp_samples,y_interp_samples, label='Interpolated function', marker = 'o')
	plt.show()



def test_cubic_interpolation_shift(delta):
	x_samples = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	y_samples = np.cos(x_samples)

	x_interp_samples = np.linspace(0, 14, 100)
	y_interp_samples = np.zeros_like(x_interp_samples)

	for i in range(0, len(x_interp_samples)):
		for k in range(0, len(x_samples)):
			phi = cubic_interpolation_model(x_interp_samples[i] - delta - x_samples[k])
			f_n = y_samples[k] * phi
			y_interp_samples[i] += f_n


	plt.plot(x_samples, y_samples, label='Original Function', marker = 'o')
	plt.plot(x_interp_samples,y_interp_samples, label='Interpolated function', marker = 'o')
	plt.show()




#############

def io_interpolation_1D(input_array_x,input_array_y,max_x, n_values_result, interpolant = 'linear', shift = 0):
	x_interp_samples = np.linspace(0, max_x, n_values_result)
	y_interp_samples = np.zeros_like(x_interp_samples)

	# For normalizing the range to 0->1
	h = input_array_x[1] - input_array_x[0]

	for i in range(0, len(x_interp_samples)):
		for k in range(0, len(input_array_x)):

			if interpolant == 'linear':
				phi = linear_interpolation_model((x_interp_samples[i] - shift - input_array_x[k])/ h)
			elif interpolant == 'cubic':
				phi = cubic_interpolation_model((x_interp_samples[i] - shift - input_array_x[k])/ h)
			else:
				phi = linear_interpolation_model((x_interp_samples[i] - shift - input_array_x[k])/ h)
			f_n = input_array_y[k] * phi
			y_interp_samples[i] += f_n

	return x_interp_samples, y_interp_samples



def test_io_interpolation():
	max_x = 30
	n_points_multiplier = 3 
	x = np.linspace(0, max_x, (max_x * n_points_multiplier) + 1)
	y = np.sin(x)

	interpolated_x, interpolated_y = io_interpolation_1D(x,y,max_x, 1000, 'cubic', -2.555)
	plt.plot(x,y, marker='o', label='Original function')
	plt.plot(interpolated_x,interpolated_y,label='Interpolated function')
	plt.legend()
	plt.show()





def read_c_implementation():
	data_x = np.fromfile("../../build/interpolated_points_x.raw", dtype=np.float32)
	data_y = np.fromfile("../../build/interpolated_points_y.raw", dtype=np.float32)


	plt.plot(data_x,data_y, label = "Interpolated function in C")
	plt.legend()
	plt.show()



def main():
	# test_linear_interpolation()
	# test_cubic_interpolation()
	# test_cubic_interpolation_shift(2.5)
	# test_io_interpolation()
	read_c_implementation()


if __name__ == '__main__':
	main()