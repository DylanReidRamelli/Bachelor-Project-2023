import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def read_data(image_path_original, image_path_modified, filter_path):
    # nx = 256
    # ny = 256

    # Load the data from the file
    data = np.fromfile(image_path_original, dtype=np.double)
    data_modified = np.fromfile(image_path_modified, dtype=np.single)
    # filter_data = np.fromfile(filter_path, dtype=float)
    n = 100
    # data = np.reshape(data, (ny, nx))

    # print(data)


    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    # Visualize the data as an image
    # plt.imshow(data, cmap='gray')
    plt.plot(np.arange(n), data)
    plt.plot(np.arange(n), data_modified)
    # print(filter_data)
    # plt.stem(np.arange(41), filter_data.real)
    # plt.stem(np.arange(41), phase_data)
    # plt.stem(np.arange(41), original_filter_data)

    plt.show()
    # plt.savefig("gather_loss.png")


if __name__ == "__main__":
	read_data("../core/original_signal.raw", "../core/shifted_signal.raw", "../core/filter.raw")