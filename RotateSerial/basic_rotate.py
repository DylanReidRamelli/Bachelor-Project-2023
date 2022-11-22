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