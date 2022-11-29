#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP6_out


ml python/3.8.2

python STEP6.py $DIR/STEP4_1_out/vep_${NAME}_4_1.csv $DIR/STEP5_out $DIR/STEP6_out
