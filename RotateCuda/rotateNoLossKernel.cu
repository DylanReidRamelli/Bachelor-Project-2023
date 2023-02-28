#include <iostream>
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__global__ float max(float *input, int size)
{
    int tid = (blockIdx.x * blockDim.x) + threadIdx.x;
}

__global__ void rotateGatherNoLoss(float *A, float *dst_array, const float angle,
                                   int width, int height, int mSize[2])
{

    int newSize[2] = {0, 0};

    // Rotate corners and get new dimentions of image.
    // rotateCorners(newSize, width, height, angle);

    float c_x = width / 2.0;
    float c_y = height / 2.0;
    float c_x_out = newSize[0] / 2.0;
    float c_y_out = newSize[1] / 2.0;

    printf("Size of new image: nx:%i, ny:%i\n", newSize[0], newSize[1]);

    // For python.
    mSize[0] = newSize[0];
    mSize[1] = newSize[1];

    dst_array = (float *)realloc(dst_array, mSize[0] * mSize[1] * sizeof(float));

    if (dst_array)
    {

        memset(dst_array, 0, mSize[0] * mSize[1] * sizeof(float));

        // Iterating horizontally through the image.
        for (int i = 0; i < newSize[1]; i++)
        {
            for (int j = 0; j < newSize[0]; j++)
            {

                // Subtract center coordinates, so that we rotate with respect to the
                // center of the image.
                float x = j - c_x_out;
                float y = i - c_y_out;

                // Rotation operation
                float dst_x = cos(angle) * x + sin(angle) * y;
                float dst_y = -sin(angle) * x + cos(angle) * y;

                // Add back the center "vector"
                dst_x = (int)(dst_x + c_x);
                dst_y = (int)(dst_y + c_y);

                // Check if the resulting point is inside the boundary of the
                // image,i.e 0->max_x, 0->max_y.
                if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height)
                {
                    // If so then assign value from original array to dst_array at idx
                    // location.
                    int idx = dst_y * width + dst_x;
                    dst_array[i * mSize[0] + j] = A[idx];
                }
            }
        }
    }
}

int main()
{

    const char *pathname = "../Images/data_rectangle.raw";
    int width = 300;
    int height = 200;

    const int n = width * height;
    float *A = (float *)malloc(sizeof(float) * n);
    float *R = (float *)malloc(sizeof(float) * n);

    memset(R, 0, n * sizeof(float));

    float *d_a, *d_out;

    // Open input image and populate input array A.
    FILE *raw_p = fopen(pathname, "rb");
    if (raw_p)
    {
        fread(A, sizeof(float), n, raw_p);
    }

    // Can create a kernel for this as well, or just add it in the rotation kernel.
    // Modify input array A by normalizing values from 0->1.
    for (int i = 0; i < n; ++i)
    {
        A[i] = A[i] / 255.0;
    }

    // Allocate memory on device.
    cudaMalloc(&d_a, sizeof(float) * n);
    cudaMalloc(&d_out, sizeof(float) * n);

    // Copy Image array to device.
    cudaMemcpy(d_a, A, sizeof(float) * n, cudaMemcpyHostToDevice);
    cudaMemcpy(d_out, R, sizeof(float) * n, cudaMemcpyHostToDevice);

    int NUM_THREADS = 256;
    int NUM_BLOCKS = (int)ceil(n / NUM_THREADS);

    cudaMemcpy(R, d_out, sizeof(float) * n, cudaMemcpyDeviceToHost);

    // Open output file and write result array.
    FILE *fp = fopen("test_image.raw", "wb");
    if (fp)
    {
        size_t r = fwrite(R, sizeof(R[0]), n, fp);
        printf("wrote %zu elements out of %d requested\n", r, n);
    }

    cudaFree(d_a);
    cudaFree(d_out);
    // fclose(fp);
    // fclose(raw_p);
    free(A);
    free(R);

    return 0;
}