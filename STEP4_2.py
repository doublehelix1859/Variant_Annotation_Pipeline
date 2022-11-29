## Cigdem Sevim Bayrak, 2020
## run as 8.gene_features <goflof_file> <path_for_inputfiles>
## maps the gene level features based on gene name

import pandas as pd
from tqdm import tqdm
import sys

data_file = sys.argv[1]
path= sys.argv[2] #path to annotation files
outfile = sys.argv[3]

data=pd.read_csv(data_file, sep='\t')

gdi=pd.read_csv(path+"/Gene-level.csv", index_col='Gene')
denovo=pd.read_csv(path+"/denovo.txt", sep="\t", header=None, names=["Gene","denovo"], index_col='Gene')
rvis_data=pd.read_csv(path+"/RVIS_v3_12Mar16.txt", sep="\t", index_col='GENE')
gerstein=pd.read_csv(path+"/Gerstein.TXT", sep="\t", usecols=["GENE_NAME", "PREDICTED_INDISPENSABILITY_SCORE"], index_col='GENE_NAME')


gdi_phred = []
selective_pressure = []
clarks_distance = []
cds_len = []
number_of_paralogs = []
denovo_zscore = []
rvis = []
indisp = []
for i in tqdm(data.index):
    mygene=data.at[i,'SYMBOL'] #from VEP
    if pd.notnull(mygene):

        if mygene in gdi.index:
            gdi_phred.append(gdi.at[mygene,'GDI_Phred'])
            selective_pressure.append(gdi.at[mygene,'Selective_pressure'])
            clarks_distance.append(gdi.at[mygene,'Clarks_distance'])
            cds_len.append(gdi.at[mygene,'CDS_len'])
            number_of_paralogs.append(gdi.at[mygene,'Number_of_paralogs'])
        else:
            gdi_phred.append(None)
            selective_pressure.append(None)
            clarks_distance.append(None)
            cds_len.append(None)
            number_of_paralogs.append(None)        

        if mygene in denovo.index:
            denovo_zscore.append(denovo.at[mygene, 'denovo'])
        else:    
            denovo_zscore.append(None)

        if mygene in rvis_data.index:
            rvis.append(rvis_data.at[mygene, 'ALL_0.1%'])
        else:
            rvis.append(None)

        if mygene in gerstein.index:
            indisp.append(gerstein.at[mygene, 'PREDICTED_INDISPENSABILITY_SCORE'])
        else:
            indisp.append(None)
    else:
        gdi_phred.append(None)
        selective_pressure.append(None)
        clarks_distance.append(None)
        cds_len.append(None)
        number_of_paralogs.append(None)
        denovo_zscore.append(None)
        rvis.append(None)
        indisp.append(None)

        
for l in [gdi_phred, selective_pressure, clarks_distance, cds_len, number_of_paralogs, denovo_zscore, rvis, indisp]:
    if len(l) != data.shape[0]:
        raise ValueError()

data['GDI_Phred'] = gdi_phred
data['Selective_pressure'] = selective_pressure
data['Clarks_distance'] = clarks_distance
data['CDS_len'] = cds_len
data['Number_of_paralogs'] = number_of_paralogs
data['denovo_Zscore'] = denovo_zscore
data['RVIS'] = rvis
data['Indispensability_score'] = indisp
        
data.to_csv(outfile, index=False)


