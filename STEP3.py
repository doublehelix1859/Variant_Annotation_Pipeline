import collections
from pandas import *
import numpy as np
import sys
import os
import pandas as pd

datafile = sys.argv[1]
headerfile = sys.argv[2]
outfile = sys.argv[3]
outfile_final = sys.argv[4]

gdi_df=read_csv("/sc/arion/projects/Itan_lab/vep_data/GDI/GDI.csv")
msc_df=read_csv("/sc/arion/projects/Itan_lab/vep_data/MSC_v1.6/MSC_v1.6_95.txt", usecols=['Gene','MSC'], sep="\t")

##read all column names of the vcf output
csqheader=read_csv(headerfile, header=None, names=["i","name"], sep="\t")["name"].to_list()
csqheaderdedup = []
for i in range(len(csqheader)):
    if csqheader[i] in ['APPRIS', 'TSL']:
        csqheaderdedup.append(csqheader[i]+str(i))
    else:
        csqheaderdedup.append(csqheader[i])       
myheader=["CHROM","POS","ID","REF","ALT"]
myheader+=csqheaderdedup ##add the columns of the input file

##compares CADD scores to MSC thresholds
def compare(x,y):
        if x!="." and not isnull(y):
                if float(x)>float(y):
                        return "High"
                else:
                        return "Low"

chunk=10**5
for chunk in read_csv(datafile, sep="\t", chunksize=chunk, header=None, names=myheader):
	chunk_gdi=merge(chunk, gdi_df, how='left', left_on='SYMBOL', right_on='Gene', suffixes=('','_gdi'))
	chunk_gdi.drop('Gene_gdi', axis=1, inplace=True)

	chunk_gdi_msc=merge(chunk_gdi, msc_df, how='left', left_on='SYMBOL', right_on='Gene', suffixes=('','_msc'))
	chunk_gdi_msc.drop('Gene_msc', axis=1, inplace=True)
	chunk_gdi_msc.rename(columns={'MSC':'MSC_95CI'}, inplace=True)

	chunk_gdi_msc['MSC_CADD_95CI']=chunk_gdi_msc.apply(lambda x: compare(x.CADD_PHRED, x.MSC_95CI), axis=1)

	if not os.path.isfile("%s.tsv"%outfile):
		chunk_gdi_msc.to_csv("%s.tsv"%outfile, sep="\t", index=False)
	else:
		chunk_gdi_msc.to_csv("%s.tsv"%outfile, sep="\t", index=False, mode='a', header=False)


#source
dir = os.environ["DIR"]
name = os.environ["NAME"]


#Renaming 'ID' and creating a new 'ID' column for the downstream work
f = pd.read_csv(dir + '/STEP3_out/vep_pre_' + name + '_3.tsv', sep='\t')
#convert to dataframes
df = pd.DataFrame(f)

#Create a dictionary
# key = old name
# value = new name

#This part should be modified according to the information of the input VCF. Specifically, value should be changed
#Original ID column's header will be changed upon the newly named value
dict = {'ID': 'refSNP_ID'}

df.rename(columns=dict,inplace=True)
#Creating a new 'ID'column using the format of 'chr_pos_ref_alt'
df['ID'] = df.apply(lambda r: str(r[0])+'_'+str(r[1])+'_'+r[3]+'_'+r[4],axis=1)
#Replacing 'chr' prefix
df['ID']=df['ID'].str.replace('chr','')

#Creating csv output
df.to_csv(outfile_final,index=False)
