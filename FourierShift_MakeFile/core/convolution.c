 #include <stddef.h>
 static void kconv(const float * in0,
const float w0,
const float w1,
const float w2,
const float w3,
const float w4,
const float w5,
const float w6,
const float w7,
const float w8,
const float w9,
const float w10,
const float w11,
const float w12,
const float w13,
const float w14,
const float w15,
const float w16,
const float w17,
const float w18,
const float w19,
const float w20,
float * out){ for(int i = 0; i < 21; ++i)
	    {
{out[i] = 
w0* in0[i + 0] +
w1* in0[i + 1] +
w2* in0[i + 2] +
w3* in0[i + 3] +
w4* in0[i + 4] +
w5* in0[i + 5] +
w6* in0[i + 6] +
w7* in0[i + 7] +
w8* in0[i + 8] +
w9* in0[i + 9] +
w10* in0[i + 10] +
w11* in0[i + 11] +
w12* in0[i + 12] +
w13* in0[i + 13] +
w14* in0[i + 14] +
w15* in0[i + 15] +
w16* in0[i + 16] +
w17* in0[i + 17] +
w18* in0[i + 18] +
w19* in0[i + 19] +
w20 * in0[i + 20] ;
	    	}
		}
	}
void dconv(const float *in, const float *w, float*out){
	 kconv(in,w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10],w[11],w[12],w[13],w[14],w[15],w[16],w[17],w[18],w[19],w[20],out);
}
