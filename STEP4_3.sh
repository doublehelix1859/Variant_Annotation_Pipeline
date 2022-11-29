#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP4_3_out

ml python/3.8.2

python $DIR/STEP4_3.py $DIR/STEP3_out/vep_${NAME}_3.csv $DIR/STEP4_3_out/vep_${NAME}_4_3.csv
