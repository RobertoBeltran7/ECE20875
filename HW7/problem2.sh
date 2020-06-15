#!/usr/bin/env bash

OUT=${OUTFILE}.out
echo $OUT

ERR=${OUTFILE}.err
echo $ERR

./cmd1 < $INFILE | ./cmd3 > $OUT 2> $ERR
