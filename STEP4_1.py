## Cigdem Sevim Bayrak, 2020
## add protein-level annotations 
## run as python 5.aa_properties.py <goflof_VEP> (goflof_DM_VEP.csv file, output of 4.add_VEP_output)
## splits and determines the position and aa features: rel_cDNA_pos, rel_CDS_pos, rel_prot_pos, AA_pos, Ref_aa, Alt_aa
## calculates the stable Ensembl protein ID (with version) from HGVSp. It will be used in BioMart to extract protein domain info.
## these info saved into another file prot_info.csv to use as an input for IUPRED and NetSurfP

## After running:
## use the BioMart hg37!! https://grch37.ensembl.org/biomart/martview/
## select Ensembl genes -> Human -> filters -> GENE -> input external references-> "Protein stable IDs with version" from the drop down and copy biomart_input.csv
## Attributes -> GENE : Gene stable ID, Gene stable ID version, Transcript stable ID, Transcript stable ID version, Protein stable ID, Protein stable ID version, 
## Protein Domain and families: Pfam domain ID, Pfam domain start, Pfam domain end
## InterPro: InterPro ID, short description, InterPro start, InterPro end

## After running: STEP_BM(Old Step_5_2)
## Minju Kim, 2022 (updated approach)
## use the BioMart hg38!! https://www.ensembl.org/biomart/martview
## select Ensembl Genes 106 -> human genes -> click "Attributes" -> click "GENE" -> select "Gene stable ID", "Gene stable ID version", "Protein stable ID", "Protein stable ID version" -> click "Protein domains and families" -> slect "Pfam ID", "Pfam start", "Pfam end", "Interpro ID", "Interpro Short Description", "Interpro start", "Interpro end" -> click "Resultes" at the top left -> from the "Export all results to", select "File" and "CSV" and hit the GO 
## Attributes --> ensembl_gene_id;ensembl_peptide_id;ensembl_peptide_id_version;interpro;interpro_short_description;interpro_start;interpro_end;pfam;pfam_start;pfam_end

##STEP4_1_alt.py: alternative version of STEP4_1
##If STEP4_1.py doesn't work, please try STEP4_1_alt.py


import pandas as pd
import sys
from tqdm import tqdm

tqdm.pandas()

data_file = sys.argv[1]
biomart_out = sys.argv[2]
outfile = sys.argv[3]

data=pd.read_csv(data_file, sep='\t')

##take the ones with protein info
mydata=data[(data.BIOTYPE=="protein_coding") & (data.Protein_position.notnull()) & (data.Protein_position!=".")]

##take the ENSP id with version
mydata["ENSP_v"]=mydata["HGVSp"].str.split(":", n=1, expand=True)[0]

##Relative position: pos/len*10 (gives number btw 0-10)
def calc_pos(x):
    if x=="-":
        return "NULL"
    else:
        
        splitted=x.split("/")
        pos_info=splitted[0]
        prot_len=splitted[1]
        positions=pos_info.split("-")
        if len(positions)==1: #single position, not a range
            if int(pos_info) > int(prot_len): ## if stop-gain: 503/502
                return 1

            else:
                return int(float(pos_info)/float(prot_len))

        elif len(positions)==2: ## if position is a range
            start_pos=positions[0]
            end_pos=positions[1]
            if start_pos=="?" or start_pos=="":
                if end_pos!='':
                    return int(float(end_pos)/float(prot_len))
            elif int(start_pos) > int(prot_len):
                return 1
            else:
                return int(float(start_pos)/float(prot_len))

### Calculate relative positions (0-10): pos/len*10
mydata["rel_cDNA_pos"]=mydata["cDNA_position"].progress_apply(calc_pos)
mydata["rel_CDS_pos"]=mydata["CDS_position"].progress_apply(calc_pos)
mydata["rel_prot_pos"]=mydata["Protein_position"].progress_apply(calc_pos)

##Relative position: pos/len*10 (gives number btw 0-10)
def aa_pos(x):
    if x=="-":
        return "NULL"
    else:
        splitted=x.split("/")
        pos_info=splitted[0]
        prot_len=splitted[1]
        positions=pos_info.split("-")
        if len(positions)==1: #single position, not a range
            if int(pos_info) > int(prot_len): ## if stop-gain: 503/502
                return int(prot_len)
            else:
                return int(pos_info)

        elif len(positions)==2: ## if position is a range
            start_pos=positions[0]
            end_pos=positions[1]
            if start_pos=="?" or start_pos=="":
                if end_pos!='':
                    return int(end_pos)
            elif int(start_pos) > int(prot_len):
                return int(prot_len)
            else:
                return int(start_pos)

mydata["AA_pos"]=mydata["Protein_position"].progress_apply(aa_pos)


# ### Ref and Alt aa types
def ref_aa(x):
    if x=="-":
        return "NULL"
    else:
        #original version#
#       splitted=x.split("/")
        #new version#
        splitted=str(x).split()
        if len(splitted)==1: #synonymous
            return str(splitted[0])
        elif len(splitted)==2:
            return str(splitted[0])[0]
mydata["Ref_aa"]=mydata["Amino_acids"].progress_apply(ref_aa)

def alt_aa(x):
    if x=="-":
        return "NULL"
    else:
        #original version#
#       splitted=x.split("/")
        #new version#
        splitted=str(x).split()
        if len(splitted)==1: #synonymous
            return str(splitted[0])
        elif len(splitted)==2:
            if "*" in splitted[1]:
                return "*"
            elif "X" in splitted[1]:
                return "X"
            else:
                return str(splitted[1])[0]
mydata["Alt_aa"]=mydata["Amino_acids"].progress_apply(alt_aa)

mydata = mydata[["ID","ENSP_v","rel_cDNA_pos","rel_CDS_pos","rel_prot_pos","AA_pos","Ref_aa","Alt_aa"]]
out = data.merge(mydata, on='ID', how='left')
out.to_csv(outfile, index=False)

## biomart input file
myids=pd.unique(mydata[mydata["ENSP_v"]!="."].ENSP_v)
out=open(biomart_out, "w")
for id in myids:
    out.write("%s\n"%id)
out.close()
