import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def read_data(image_path_original, image_path_modified, filter_path, phase_path, original_filter_path):
    # nx = 256
    # ny = 256

    # Load the data from the file
    data = np.fromfile(image_path_original, dtype=np.double)
    data_modified = np.fromfile(image_path_modified, dtype=np.cdouble)
    filter_data = np.fromfile(filter_path, dtype=np.cdouble)
    phase_data = np.fromfile(phase_path, dtype=np.cdouble)
    original_filter_data = np.fromfile(original_filter_path, dtype=np.cdouble)
    n = 100
    # data = np.reshape(data, (ny, nx))

    # print(data)


    plt.title("Original Image")
    plt.xlabel("X pixel scaling.")
    plt.ylabel("Y pixel scaling.")

    # Visualize the data as an image
    # plt.imshow(data, cmap='gray')
    plt.plot(np.arange(n), data)
    plt.plot(np.arange(140), data_modified)
    # print(filter_data)
    # plt.stem(np.arange(41), filter_data.real)
    # plt.stem(np.arange(41), phase_data)
    # plt.stem(np.arange(41), original_filter_data)

    plt.show()
    # plt.savefig("gather_loss.png")


if __name__ == "__main__":
	read_data("../../build/original_signal.raw", "../../build/shifted_signal.raw", "../../build/filter.raw","../../build/phase.raw","../../build/original_filter.raw" )