 #include<complex.h> 
#include <stddef.h>
 #define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) < (Y)) ? (Y) : (X))
static void kconv(const float * in0,
const int n,
const float complex *w,float * out) {for(int i = 0; i < n ; ++i)
	    {out[i] = 
w[0]* in0[i + 0] +
w[1]* in0[i + 1] +
w[2]* in0[i + 2] +
w[3]* in0[i + 3] +
w[4]* in0[i + 4] +
w[5]* in0[i + 5] +
w[6]* in0[i + 6] +
w[7]* in0[i + 7] +
w[8]* in0[i + 8] +
w[9] * in0[i + 9] ;
	    	}
	}
void dconv(const float *in, const int n, const float complex *w, float *out){
	 kconv(in, n, w,out);
}
