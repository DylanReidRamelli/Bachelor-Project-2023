import basic_rotate as b
import numpy as np
import math as m
import matplotlib.pyplot as plt


def main():
	n_x = 20
	n_y = 20
	n = n_x * n_y
	init_array = np.linspace(0,n,num=n)
	# init_array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
	dst_array_scatter = b.rotateScatter(init_array,m.pi/4,n_x,n_y, 0)
	dst_array_gather = b.rotateGather(init_array,m.pi/4,n_x,n_y, 0)

	figure, axis = plt.subplots(2, 2)

	#original image
	axis[0, 0].imshow(np.reshape(np.array(init_array, dtype=np.float32), (n_x,n_y)))
	axis[0, 0].set_title("Original_image")

	# Final image
	axis[0, 1].imshow(np.reshape(np.array(dst_array_gather, dtype=np.float32), (n_x,n_y)))
	axis[0, 1].set_title("Resulting image (gather rotate)")

	axis[1, 1].plot(init_array, dst_array_scatter)
	axis[1, 1].set_title("Scatter rotate (unrolled signal)")
	# axis[0,0].xlabel("index") 
	# axis[0,0].ylabel("value") 
	# plt.ylabel("value") 
	  
	axis[1, 0].plot(init_array, dst_array_gather)
	axis[1, 0].set_title("Gather rotate (unrolled signal)")
	# axis[0,1].xlabel("index") 
	# axis[0,1].ylabel("value")


	# Display

	plt.show()	

if __name__ == '__main__':
	main()