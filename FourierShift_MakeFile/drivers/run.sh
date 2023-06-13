#!/bin/sh

make clean; make test;

./test $1

python3 ../python/signal_io.py $1