## Cigdem, 2020
## example: python 11.enrichr_feats.py ./4.add_VEP_output/goflof_DM_VEP.csv /Volumes/Itan_Lab/Projects/GOF-LOF/Enrichr_libraries/ARCHS4_tissues/ARCHS4_Tissues-2.txt goflof_DM_VEP_ARCHS4_tissues.csv
## maps gene-level binary features from Enrichr libraries. Datasets have the same format where the first column is the feature and the others are the genes having that feature.

import pandas as pd
import sys

data_file = sys.argv[1] 
enrichr_file= sys.argv[2] #file downloaded from Enrichr resources
output_filename = sys.argv[3] 

data=pd.read_csv(data_file, usecols=["ID", 'SYMBOL'])

with open(enrichr_file) as file1:
    for line in file1:
        record=line.strip().split("\t")
        data[record[0]]=data["SYMBOL"].apply(lambda x: 1 if x in record[1:] else 0)

data.drop(["SYMBOL"], axis=1, inplace=True)
data.to_csv("%s"%output_filename, index=False)
