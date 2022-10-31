ml bcftools/1.10.2

for file in *.vcf*; do
  for sample in `bcftools view -h $file | grep "^#CHROM" | cut -f10-`; do
    bcftools view -c1 -Oz -s $sample -o ${file/.vcf*/.$sample.vcf.gz} $file
  done
done
