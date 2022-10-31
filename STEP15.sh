#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP15_out


ml python/3.8.2
# automatically export variables
set -a
. ./STEP0.sh
exec python ./STEP15.py

cd $DIR/STEP15_out

cut -d, -f1 --complement vep_${NAME}_15.csv > vep_${NAME}_15.csv
