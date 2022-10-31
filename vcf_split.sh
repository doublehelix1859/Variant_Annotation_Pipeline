#!/bin/bash

source ./STEP0.sh

split -l 146956 --numeric-suffixes clinvar_20220730.vcf ${NAME}_;

for file in ${NAME}_*; do
    mv "$file" "${file}.vcf"
done 
