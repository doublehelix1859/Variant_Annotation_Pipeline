#!/bin/bash

source ./STEP0.sh

cd $DIR
mkdir STEP4_1_out


ml python/3.8.2

python STEP4_1.py $DIR/STEP3_out/vep_${NAME}_3.csv /sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/biomart_out.txt $DIR/STEP4_1_out/vep_${NAME}_4_1.csv
