import math as m
import matplotlib.pyplot as plt
import numpy as np

def rotateScatter(A, angle, width, height, invalid_value):
	# Find (x,y) coordinate.
	dst_array = [invalid_value] * len(A)
	for i in range(0,len(A)):
		x = m.floor(i / height)
		y = m.floor(i % height)

		# Translate point to have relative coordinates to the center of the image.
		c_x = width / 2.0
		c_y = height / 2.0

		x = x - c_x
		y = y - c_y

		# Rotate in respect to new origin.
		dst_x = m.cos(angle)*x - m.sin(angle)*y
		dst_y = m.sin(angle)*x + m.cos(angle)*y

		# Make (0,0) the origin again

		dst_x = int(dst_x + c_x)
		dst_y = int(dst_y + c_y)

		if dst_x >= 0 and dst_x < width and dst_y >= 0 and dst_y < height:
			# Find index
			idx = dst_x * height + dst_y
			dst_array[idx] = A[i]

	return dst_array

def rotateGather(A, angle, width, height, invalid_value):
	# Find (x,y) coordinate.
	dst_array = [invalid_value] * len(A)
	for i in range(0,len(dst_array)):
		x = m.floor(i / height)
		y = m.floor(i % height)
		# Translate point to have relative coordinates to the center of the image.
		c_x = width / 2.0
		c_y = height / 2.0
		x = x - c_x
		y = y - c_y

		# Inverse rotate in respect to new origin.
		dst_x = m.cos(angle)*x - m.sin(angle)*y
		dst_y = m.sin(angle)*x + m.cos(angle)*y 

		# Make (0,0) the origin again

		dst_x = int(dst_x + c_x)
		dst_y = int(dst_y + c_y)

		if dst_x >= 0 and dst_x < width and dst_y >= 0 and dst_y < height:
			# Find index
			idx = dst_x * height + dst_y
			dst_array[i] = A[idx]

	return dst_array

def roationMatrix(angle,position):
	dst_x = m.cos(angle)*position[0] - m.sin(angle)*position[1]
	dst_y = m.sin(angle)*position[0] + m.cos(angle)*position[1] 
	return np.array([dst_x,dst_y])


def rotateGatherNoLoss(A, angle, width, height, invalid_value):
	c_x = height/ 2.0
	c_y = width / 2.0

	minmin = np.array([0,0])
	maxmin = np.array([width,0])
	minmax = np.array([0,height])
	maxmax = np.array([width,height])

	minmin[0] = minmin[0] - c_x
	minmin[1] = minmin[1] - c_y
	maxmin[0] = maxmin[0] - c_x
	maxmin[1] = maxmin[1] - c_y
	minmax[0] = minmax[0] - c_x
	minmax[1] = minmax[1] - c_y
	maxmax[0] = maxmax[0] - c_x
	maxmax[1] = maxmax[1] - c_y


	# print(minmin,"\n")
	# print(maxmin,"\n")
	# print(minmax,"\n")
	# print(maxmax,"\n")

	minmin = roationMatrix(angle,minmin)
	maxmin = roationMatrix(angle,maxmin)
	minmax = roationMatrix(angle,minmax)
	maxmax = roationMatrix(angle,maxmax)

	minmin[0] = minmin[0] + c_x
	minmin[1] = minmin[1] + c_y
	maxmin[0] = maxmin[0] + c_x
	maxmin[1] = maxmin[1] + c_y
	minmax[0] = minmax[0] + c_x
	minmax[1] = minmax[1] + c_y
	maxmax[0] = maxmax[0] + c_x
	maxmax[1] = maxmax[1] + c_y


	# print(minmin,"\n")
	# print(maxmin,"\n")
	# print(minmax,"\n")
	# print(maxmax,"\n")

	sizeX = m.ceil(max(minmin[0],maxmin[0],minmax[0],maxmax[0]) - min(minmin[0],maxmin[0],minmax[0],maxmax[0]))
	sizeY = m.ceil(max(minmin[1],maxmin[1],minmax[1],maxmax[1]) - min(minmin[1],maxmin[1],minmax[1],maxmax[1]))

	dst_array = [invalid_value] * sizeX * sizeY

	c_x_in = width / 2.0
	c_y_in = height / 2.0
	c_x_out = sizeX / 2.0
	c_y_out = sizeY / 2.0

	for i in range(0,len(dst_array)):
		x = m.floor(i / sizeY)
		y = m.floor(i % sizeY)
		# Translate point to have relative coordinates to the center of the image.

		x = x - c_x_out
		y = y - c_y_out

		# Inverse rotate in respect to new origin.
		dst_x = m.cos(angle)*x - m.sin(angle)*y
		dst_y = m.sin(angle)*x + m.cos(angle)*y 

		# Make (0,0) the origin again

		dst_x = int(dst_x + c_x_in)
		dst_y = int(dst_y + c_y_in)

		if dst_x >= 0 and dst_x < width and dst_y >= 0 and dst_y < height:
			# Find index
			idx = dst_x * height + dst_y
			dst_array[i] = A[idx]

	return dst_array, sizeX, sizeY