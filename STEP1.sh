#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir std
mkdir STEP1_out


source activate phen
ml bcftools
module load vep/100

WRKDIR=$DIR/STEP1_out
cachedir=/hpc/packages/minerva-centos7/vep/100/cache/
cadddir=/sc/arion/projects/Itan_lab/vep_data/CADD/GRCh38
ref_fasta=/sc/arion/projects/Itan_lab/vep_data/fasta_ref/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
plugdir=/sc/arion/projects/Itan_lab/vep_data

myinput=$DIR/$IN
myoutput=vep_${NAME}_1.vcf

#HG38

/hpc/packages/minerva-centos7/vep/100/src/ensembl-vep/vep -i $myinput -o $WRKDIR/$myoutput --verbose --vcf --dir_cache $cachedir --assembly GRCh38 --cache --sift b --polyphen b --ccds --no_stats --hgvs --symbol --numbers --domains --regulatory --canonical --protein --biotype --uniprot --tsl --appris --gene_phenotype --pubmed --variant_class --mane --total_length --pick_allele --offline --fasta $ref_fasta --dir_plugins $pathToPlugins --plugin CADD,$cadddir/whole_genome_SNVs.tsv.gz,$cadddir/gnomad.genomes.r3.0.indel.tsv.gz --force_overwrite --fork 40 --buffer_size 1000 --minimal --allele_number --plugin Blosum62 --plugin Condel,$plugdir/Condel/config,b --plugin Conservation,$plugdir/Conservation/gerp_conservation_scores.homo_sapiens.GRCh38.bw --plugin ExACpLI,$plugdir/ExACpLI/ExACpLI_values.txt --plugin LoFtool,$plugdir/LoFtool/LoFtool_scores.txt --plugin REVEL,$plugdir/REVEL/new_tabbed_revel_grch38.tsv.gz --plugin StructuralVariantOverlap,file=$plugdir/StructuralVariantOverlap/gnomad_v2.1_sv.sites.vcf.gz --plugin NearestExonJB --plugin Carol --plugin Downstream --plugin GeneSplicer,$plugdir/GS/GeneSplicer/bin/linux/genesplicer,$plugdir/GS/GeneSplicer/human,context=200,tmpdir=/tmp --plugin MaxEntScan,$plugdir/maxentscan/ --plugin Mastermind,$plugdir/mastermind/mastermind_cited_variants_reference-2021.04.02-grch38.vcf.gz --plugin PON_P2,$plugdir/ponp2/ponp2.py --plugin ReferenceQuality,$plugdir/refquality/sorted_GRCh38_quality_mergedfile.gff3.gz --plugin satMutMPRA,file=$plugdir/satmutmpra/satMutMPRA_GRCh38_ALL.gz --plugin TSSDistance --plugin DisGeNET,file=$plugdir/disgenet/all_variant_disease_pmid_associations_final.tsv.gz --plugin dbscSNV,$plugdir/dbscsnv/dbscSNV1.1_GRCh38.txt.gz --plugin dbNSFP,$plugdir/dbNSFP/dbNSFP4.1a_grch38.gz,ALL
