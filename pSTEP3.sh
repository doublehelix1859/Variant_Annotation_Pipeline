#!/bin/bash

source ./pSTEP0.sh

for file in ${NAME}_*; do
    #copying the stepwise scripts of the pipeline in every single directory where the splitted vcf is located
    #cp STEP* ./${file};
    #copying the material of the igniter script, "vep_all_the_way.lsf" in every single directory where its own igniter script with its own name
    cat vep_all_the_way.lsf > "vep_${file}.lsf"
    #Insert a specific  Job name to every single igniter in every single directory of the splitted vcf
    sed -i '2 i #BSUB -J vep_all_the_way_'${file} "vep_${file}.lsf" 
    #copying the igniter sciprt into every single directory wehre the splitted vcf file and the pipelien stepwise work scripts are located 
    cp "vep_${file}.lsf" ./"$file";
    #Deleting the igniter in the current directory
    rm "vep_${file}.lsf"
done 
