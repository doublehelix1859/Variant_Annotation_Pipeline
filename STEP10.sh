#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP10_out

ml python/3.8.2

python $DIR/STEP10.py $DIR/STEP4_1_out/vep_${NAME}_4_1.csv /sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/step9_input $DIR/STEP10_out/vep_${NAME}_10.csv
