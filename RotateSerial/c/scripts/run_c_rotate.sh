#!/usr/bin/env bash
make ../build/mainC
../build/mainC 
../drivers/read_raw_image.py ../build/test_image.raw