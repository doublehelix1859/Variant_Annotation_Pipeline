#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP16_out


cd $DIR/STEP15_out

cut -d, -f1 --complement vep_${NAME}_15.csv > $DIR/STEP16_out/vep_${NAME}_16.csv
