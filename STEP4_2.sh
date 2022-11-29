#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP4_2_out

ml python/3.8.2

python $DIR/STEP4_2.py $DIR/STEP3_out/vep_${NAME}_3.csv /sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input $DIR/STEP4_2_out/vep_${NAME}_4_2.csv

