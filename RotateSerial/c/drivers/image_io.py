#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def write_data():
    image_path_png = "../../../Images/rectangle.png"
    original_png_data = Image.open(image_path_png).convert('L')
    numpy_data = np.asarray(original_png_data)
    numpy_data = numpy_data.astype(np.float32)
    numpy_data = np.reshape(numpy_data, (60000,))
    print(numpy_data)
    numpy_data.tofile("../../../Images/data_rectangle.raw")


def read_data(image_path):
    nx = 1303
    ny = 2000

    # Load the data from the file
    data = np.fromfile(image_path, dtype=np.float32)
    n = nx * ny
    data = np.reshape(data, (ny, nx))

    print(data)


    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    # Visualize the data as an image
    plt.imshow(data, cmap='gray')
    plt.show()



def read_data_no_loss(image_path, image_info):
    f = open(image_info)
    line = f.readlines()
    line = line[0].split(',')
    nx = int(line[0])
    ny = int(line[1])
    n = nx * ny

    # Load the data from the file
    data = np.fromfile(image_path, dtype=np.float32)
    data = np.reshape(data, (ny, nx))

    print(data)


    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    # Visualize the data as an image
    plt.imshow(data, cmap='gray')
    plt.show()


if __name__ == "__main__":
    # write_data()
    # main()
    if len(sys.argv) == 3:
        read_data_no_loss(sys.argv[1], sys.argv[2])
    else:
        read_data(sys.argv[1])
