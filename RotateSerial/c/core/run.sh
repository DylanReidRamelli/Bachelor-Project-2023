#!/usr/bin/env bash

set -e

img=$1
rawfile="in.raw"
out="out.raw"

./readpng $img $rawfile
./rotate $rawfile $out

