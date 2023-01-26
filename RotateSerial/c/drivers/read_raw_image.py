#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
import math as m
from array import array

# with open(image_info_path,"r") as f:
# 	lines = f.readlines()
#     nx = lines[0]
#     ny = lines[1]


def main(image_path):
    nx = 200
    ny = 200

    # f = open(image_path, "r")
    # data = f.read()
    # data = data.split("\n")
    # for i in range(0,len(data)):
    #     if data[i] == '':
    #         data.pop(i)
    #     else:
    #         data[i] = int(data[i])
    # f.close()

    # data = np.array(data)
    dtype = np.dtype("B")
    with open(image_path, "rb") as f:
        numpy_data = np.fromfile(f, dtype)
        numpy_data = np.array(numpy_data, dtype=dtype) 
        numpy_data = np.reshape(numpy_data, (nx,ny))
        figure, axis = plt.subplots()
        image = axis.imshow(numpy_data)
        plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
