#include <iostream>
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__global__ void rotateScatter(float *A, float *dst_array, const float angle,
							  const int width, const int height)
{
	float c_x = width / 2.0;
	float c_y = height / 2.0;


	// Check if thread is in the range of the points. With width and height.
	int tid = (blockIdx.x * blockDim.x) + threadIdx.x;

	// Loop that check if each thread 

	float x = int(tid % width);
	float y = int(tid / height);

	// Subtract center coordinates, so that we rotate with respect to the
	// center of the image.
	x = x - c_x;
	y = y - c_y;

	// Rotation operation
	float dst_x = cos(angle) * x - sin(angle) * y;
	float dst_y = sin(angle) * x + cos(angle) * y;

	// Add back the center "vector"
	dst_x = (int)(dst_x + c_x);
	dst_y = (int)(dst_y + c_y);

	// Check if the resulting point is inside the boundary of the image, i.e
	// 0->max_x, 0->max_y.
	if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height)
	{
		// If so then assign value from original array to dst_array at idx
		// location.
		int idx = dst_y * width + dst_x;
		dst_array[idx] = A[tid];
	}
}

__global__ void rotateGather(float *A, float *dst_array, const float angle,
							 const int width, const int height)
{
	float c_x = width / 2.0;
	float c_y = height / 2.0;

	int tid = (blockIdx.x * blockDim.x) + threadIdx.x;

	float x = int(tid % width);
	float y = int(tid / height);

	// Subtract center coordinates, so that we rotate with respect to the
	// center of the image.
	x = x - c_x;
	y = y - c_y;

	// Rotation operation
	float dst_x = cos(angle) * x - sin(angle) * y;
	float dst_y = sin(angle) * x + cos(angle) * y;

	// Add back the center "vector"
	dst_x = (int)(dst_x + c_x);
	dst_y = (int)(dst_y + c_y);

	// Check if the resulting point is inside the boundary of the image, i.e
	// 0->max_x, 0->max_y.
	if (dst_x >= 0 && dst_x < width && dst_y >= 0 && dst_y < height)
	{
		// If so then assign value from original array to dst_array at idx
		// location.
		int idx = dst_y * width + dst_x;
		dst_array[tid] = A[idx];
	}
}

int main(int argc, char *argv[])
{

	const char *pathname = "../Images/data_roberts.raw";
	int width = 300;
	int height = 200;

	if (argc == 3)
	{
		width = atoi(argv[1]);
		height = atoi(argv[2]);
	}

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

	int NUM_THREADS = 1024;
	int NUM_BLOCKS = (int)ceil(n / NUM_THREADS);

	// // Call Kernel rotateScatter
	rotateScatter<<<NUM_BLOCKS, NUM_THREADS>>>(d_a, d_out, M_PI / 4, width, height);
	// rotateGather<<<NUM_BLOCKS, NUM_THREADS>>>(d_a, d_out, M_PI / 4, width, height);

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