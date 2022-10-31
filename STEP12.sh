#!/bin/bash

source ./STEP0.sh
cd $DIR/STEP11_out

cut -d, -f1 --complement 11_${NAME}_fix.csv > 11_${NAME}_mod.csv
cut -d, -f1 --complement 11_${NAME}_mod.csv > vep_${NAME}_11.csv

cd $DIR
mkdir STEP12_out

ml python/3.8.2
# automatically export variables
set -a
. ./STEP0.sh
exec python ./STEP12.py
