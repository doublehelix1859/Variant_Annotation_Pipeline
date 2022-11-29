#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP3_out

ml python/3.8.2

python STEP3.py $DIR/STEP2_out/vep_${NAME}_2.tsv $DIR/STEP2_out/vep_${NAME}_2_header.txt $DIR/STEP3_out/vep_${NAME}_3
