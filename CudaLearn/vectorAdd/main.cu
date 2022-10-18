#include <iostream>
#include <cuda.h>

__global__ void RotateArray(int*originalA, int*newA, int degrees){
    int x = threadIdx.x + blockDim.x * blockIdx.x;
    int y = threadIdx.y + blockDim.y * threadIdx.y;

    
}

__global__ void AddIntsCUDA(int *a, int *b){
    a[0] += b[0];
}


int main(int argc, char const *argv[])
{

    int a = 5,b = 9;
    int *d_a,*d_b;

    cudaMalloc(&d_a, sizeof(int));
    cudaMalloc(&d_b, sizeof(int));

    cudaMemcpy(d_a, &a, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, sizeof(int), cudaMemcpyHostToDevice);


    AddIntsCUDA<<<1,1>>>(d_a,d_b);


    cudaMemcpy(&a, d_a,sizeof(int), cudaMemcpyDeviceToHost);



    std::cout << "The answer is:" << a <<std::endl;

    cudaFree(d_a);
    cudaFree(d_b);

    
    return 0;
}
