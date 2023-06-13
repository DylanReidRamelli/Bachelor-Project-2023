support?= 10

CFLAGS += -Wpedantic
CFLAGS += -D_N_=$(support)
CFLAGS += -fsanitize=address -fno-omit-frame-pointer -fno-optimize-sibling-calls -O0 -g

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
	rm -f test *.o convolution.c convolution.h filter.raw original_signal.raw shifted_signal.raw

.PHONY : clean