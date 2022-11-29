#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP4_4_out


module load python/3.8.2

python $DIR/STEP4_4.py $DIR/STEP3_out/vep_${NAME}_3.tsv /sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/ARCHS4_Tissues-2.txt $DIR/STEP4_4_out/vep_${NAME}_4_4.csv
