#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP8_out


ml python/3.8.2

python STEP8.py $DIR/STEP7_out/vep_${NAME}_7.out $DIR/STEP8_out/ $DIR/STEP8_out/vep_${NAME}_8.csv
