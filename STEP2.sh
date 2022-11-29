#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP2_out

ml bcftools/1.10.2

infile=$DIR/STEP1_out/vep_${NAME}_1.vcf
outfile=$DIR/STEP2_out/vep_${NAME}_2.tsv
outheader=$DIR/STEP2_out/vep_${NAME}_2_header.txt

sed -i "/^#/s/[()]//g" $infile
sed -i "/^#/s/-/_/g" $infile
sed -i "/^#/s/++/plus_plus/g" $infile

bgzip -@ 8 -c $infile > ${infile}.gz
tabix -p vcf ${infile}.gz

bcftools +split-vep ${infile}.gz -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%CSQ\n' -d -A tab -o $outfile
bcftools +split-vep ${infile}.gz -l > $outheader
