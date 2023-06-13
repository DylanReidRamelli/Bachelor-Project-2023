import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def read_data(image_path_original, image_path_modified, filter_path, shift):
    # nx = 256
    # ny = 256

    # Load the data from the file
    data = np.fromfile(image_path_original, dtype=np.single)
    data_modified = np.fromfile(image_path_modified, dtype=np.single)
    filter_data = np.fromfile(filter_path, dtype=np.csingle)
    # original_filter_data = np.fromfile(original_filter_path, dtype=np.csingle)
    n = 100
    # data = np.reshape(data, (ny, nx))

    # print(data)


    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    # Visualize the data as an image
    # plt.imshow(data, cmap='gray')
    plt.plot(np.arange(n + 10), data, color='red')
    plt.plot([(n/4)+ float(shift), (n/4) + float(shift)], [0, 1], color='green', linewidth=4)
    plt.plot([(n/2)+ float(shift), (n/2) + float(shift)], [0, 1], color='green', linewidth=4)
    plt.stem(np.arange(n), data_modified)
    # print(filter_data)
    # plt.stem(np.arange(30), filter_data.real)
    # plt.stem(np.arange(20), phase_data)
    # plt.stem(np.arange(20), original_filter_data)

    plt.show()
    # plt.savefig("gather_loss.png")


if __name__ == "__main__":
    shift = sys.argv[1]
    read_data("../core/original_signal.raw", "../core/shifted_signal.raw", "../core/filter.raw", shift)