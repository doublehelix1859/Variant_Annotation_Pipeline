#!/bin/bash

source ./STEP0.sh
cd $DIR/STEP12_out
cut -d, -f1 --complement 12.csv > vep_${NAME}_12.csv

cd $DIR
mkdir STEP13_out


ml python/3.8.2
# automatically export variables
set -a
. ./STEP0.sh
exec python ./STEP13.py
