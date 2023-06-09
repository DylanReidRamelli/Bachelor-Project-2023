support ?= 41

CFLAGS += -Wpedantic
CFLAGS += -D_N_=$(support)

# -lm to link the math libraries.
LDFLAGS += -lm

test : main.o convolution.o fourier_filter.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o : %.c convolution.h
	$(CC) $(CFLAGS) -c $<

convolution.c : convolution.py
	./$< $(support) > $@

convolution.h : convolution.py
	./$< $(support) header > $@

clean :
	rm -f test *.o convolution.c convolution.h

.PHONY : clean