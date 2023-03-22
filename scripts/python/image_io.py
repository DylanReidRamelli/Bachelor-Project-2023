#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def write_data():
    image_path_png = "../../Images/circular_symmetric.png"
    original_png_data = Image.open(image_path_png).convert('L')
    numpy_data = np.asarray(original_png_data)
    numpy_data = numpy_data.astype(np.float32)
    numpy_data = np.reshape(numpy_data, (numpy_data.shape[0] * numpy_data.shape[1],))
    print(numpy_data.shape)
    print(numpy_data)
    numpy_data.tofile("../../Images/circular_symmetric.raw")


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

    print(nx,ny)

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



def read_data_no_loss(image_path, image_info, image_n):

    padding = 50

    original_image_info = image_info.replace(image_n, '0')
    original_image_f = open(original_image_info)
    original_line = original_image_f.readlines()
    original_line = original_line[0].split(',')
    original_nx = int(original_line[0])
    original_ny = int(original_line[1])


    max_x = original_nx + padding
    max_y = original_ny + padding


    f = open(image_info)
    line = f.readlines()
    line = line[0].split(',')
    nx = int(line[0])
    ny = int(line[1])

    inst_padding_x = max_x - nx
    inst_padding_y = max_y - ny

    n = nx * ny

    # print(max_x,max_y)
    # print(inst_padding_x,inst_padding_y)
    # print(nx,ny)

    # Load the data from the file
    data = np.fromfile(image_path, dtype=np.float32)
    data = np.reshape(data, (ny, nx))

    data = np.pad(data,pad_width=padding, mode='constant')

    # print(data)
    # print(data.shape)

    plt.title("Rotation")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")
    print("Image: "+ image_n)

    # Visualize the data as an image
    plt.imshow(data, cmap='gray')
    # plt.show()
    plt.savefig("output_images/image_" + image_n)



if __name__ == "__main__":
    # write_data()
    # # # main()



    if len(sys.argv) == 3:
        read_data_no_loss(sys.argv[1], sys.argv[2])

    elif len(sys.argv) == 4:
        read_data_no_loss(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        read_data(sys.argv[1])
