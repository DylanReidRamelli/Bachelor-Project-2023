#!/usr/bin/env python3
import sys

size = int(sys.argv[1])

weights_param = ''
in_param = 'const float * in0,\n'

for i in range(size):
	weights_param += 'const float w'+ str(i)+',\n'

n_param = 'const int n,\n'
out_param = 'float * out)'

head = ' #include <stddef.h>\n static void kconv('+ in_param + n_param + weights_param + out_param 

top_body = r'''{ for(int i = 0; i < ''' + str(size) + '''; ++i)
    {\n'''

body_params = ''
for i in range(size - 1):
	body_params += 'w'+ str(i) +'* in0[i + '+ str(i) +'] +\n'
body = '{out[i] = \n'
end = r'''w'''+ str(size-1) + ''' * in0[i + ''' +str(size-1)+'''] ;
    	}
	}
}'''

code = head + top_body+ body + body_params + end
header = "../RotateSerial/core/convolution.h"
f = open(header, 'w')
f.write(code)
f.close()