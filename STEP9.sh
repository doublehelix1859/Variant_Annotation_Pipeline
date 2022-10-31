#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP9_out


ml python/3.8.2

python STEP9.py $DIR/STEP4_1_out/vep_${NAME}_4_1.csv /sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/STEP_BM_out/mart_out.csv $DIR/STEP9_out/vep_${NAME}_9.csv
