#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP14_out
cd $DIR/STEP13_out
cut -d, -f1 --complement vep_${NAME}_13.csv > $DIR/STEP14_out/vep_${NAME}_14.csv
