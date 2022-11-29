import os
import sys
import pandas as pd
import numpy as np
from tqdm import tqdm

info_file = sys.argv[1] 
out_dir=sys.argv[2] #directory with iupred outputs
outfile=sys.argv[3]

prot_info=pd.read_csv(info_file)
output_files=os.listdir(out_dir)
file_names=[s[:-4] for s in output_files] #except last 4 char: ".out"

for i in tqdm(prot_info.index):
    myid=prot_info.loc[i,"ENSP_v"]
    if myid!="-":
        try:
            mypos=int(prot_info.loc[i,"AA_pos"])
        except:
            continue
        if myid in file_names:
            myfile=open("%s/%s.out"%(out_dir,myid),"r")
            header_count=7
            mylines=myfile.readlines()
            if not np.isnan(mypos):
                line_number=header_count+int(mypos)-1
                try:
                    ##read the corresponding line of the output file
                    columns=mylines[line_number].rstrip().split("\t")
                    prot_info.at[i,"IUPRED2"]=columns[2]
                    prot_info.at[i,"ANCHOR2"]=columns[3]
                except:
                    break
                    
prot_info.to_csv(outfile,index=False)
