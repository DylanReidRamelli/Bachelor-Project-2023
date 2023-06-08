support ?= 21

CFLAGS += -Wpedantic
CFLAGS += -D_N_=$(support)

test : main.o dconv.o filter.o 
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o : %.c
	$(CC) $(CFLAGS) -c $<

dconv.c : dconv.py
	./$< > $@

clean : 
	rm -f test *.o dconv.c

.PHONY : clean