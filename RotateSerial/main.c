#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

// Given an n x n matrix representing an image, 
// rotate it by some angle theta. Then with the new values
// rotate it by -theta and compare the initial results with the ones obtained.
// Theta should not be equal to 0,90,180,270,360. Otherwise there is no loss.



int main(int argc, char const *argv[]){
    int n = 4;
    int image[n*n] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    int newImage[n*n];

    for (int i = 0; i < 3;i++)
        for(int j = 0; j < 3;j++){
            int n_x = trunc(cos(45)*j-sin(45)*i);
            int n_y = trunc(sin(45)*j-cos(45)*i);
            printf("%d,",n_x);
            int oldIndex = j* 3 + i *3;
            int index = n_x * 3 + n_y * 3;
            newImage[index] = image[oldIndex];
        }

    for (int i = 0; i < 15;i++){
        printf("%d\n",newImage[i]);
    }
    return 0;
}   