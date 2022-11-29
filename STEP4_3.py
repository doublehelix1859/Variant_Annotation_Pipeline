import pandas as pd
import sys

data_file = sys.argv[1]
outfile = sys.argv[2]

data=pd.read_csv(data_file, sep='\t')

data.rename(columns={"GDI-Phred": "GDI_Phred"}, inplace=True) #get rid off dash (raises error)

### VEP consequence: simplify by taking the first one
data["Consequence_first"]=data["Consequence"].str.split(",", n=1, expand=True)[0]

data["SIFT_pred"]=data["SIFT"].apply(lambda x: "NULL" if x=="." else x.split("(")[0])
data["SIFT_score"]=data["SIFT"].apply(lambda x: "NULL" if x=="." else float(x.split("(")[1].split(")")[0]))

data["PolyPhen_pred"]=data["PolyPhen"].apply(lambda x: "NULL" if x=="." else x.split("(")[0])
data["PolyPhen_score"]=data["PolyPhen"].apply(lambda x: "NULL" if x=="." else float(x.split("(")[1].split(")")[0]))

data["Condel_pred"]=data["Condel"].apply(lambda x: "NULL" if x=="." else x.split("(")[0])
data["Condel_score"]=data["Condel"].apply(lambda x: "NULL" if x=="." else float(x.split("(")[1].split(")")[0]))

### Extract transmembrane helix region info from domains
data["TMhelix"]=data["DOMAINS"].apply(lambda x: 1 if "TMhelix" in x else 0)
### Extract low complexity region info from domains
data["SEG"]=data["DOMAINS"].apply(lambda x: 1 if "Low_complexity" in x else 0)

##Extract NearestExonJB the distance and the length (given as: Ensembl identifier of the exon + the distance to the exon boundary + the boundary type (start or end of exon) + the total length in nucleotides of the exon)
data["NearestExonJB_distance"]=data["NearestExonJB"].apply(lambda x: "NULL" if x=="." else x.split("+")[1])
data["NearestExonJB_len"]=data["NearestExonJB"].apply(lambda x: "NULL" if x=="." else x.split("+")[3])

data.to_csv(outfile, index=False)

