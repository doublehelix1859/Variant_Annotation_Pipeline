#!/bin/bash

source ./pSTEP0.sh
mkdir STEPM_out
cd $DIR
mkdir $DIR/std


for file in ${NAME}_*;do
    cd "${file}"
    bsub < "vep_${file}.lsf"
done


#If you want to execute only a part of vcf file, please use this part after silencing the for loop above#

#for i in {###..###};do
#    cd "gnomAD_${i}";
#    bsub < vep_gnomAD_${i}.lsf
#done
