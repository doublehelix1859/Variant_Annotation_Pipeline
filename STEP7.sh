#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP7_out


ml python/3.8.2

python ./STEP7.py $DIR/STEP4_1_out/vep_${NAME}_4_1.csv $DIR/STEP7_out/ $DIR/STEP7_out/vep_${NAME}_7.out
