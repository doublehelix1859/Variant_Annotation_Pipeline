import os
import sys
import pandas as pd
import subprocess
from tqdm import tqdm 

info_file = sys.argv[1] 
fasta_dir=sys.argv[2] #directory with protein fasta seq files
out_dir=sys.argv[3] #directory to save iupred output

available_proteins=os.listdir(fasta_dir)
prot_names=[s[:-6] for s in available_proteins] #except last 6 char: ".fasta"

prot_info=pd.read_csv(info_file)
##running netsurfp for all proteins in the goflof dataset (later run for all?)
for myid in tqdm(prot_info.ENSP_v.unique()):
    myid=str(myid)
    #check if the file exists
    if not os.path.exists(out_dir+myid+".out"):
        if myid in prot_names:     
            ##run netsurfp using the fasta file
            proc=subprocess.Popen("python /sc/arion/projects/Itan_lab/iupred2a/iupred2a.py -a %s/%s.fasta long"%(fasta_dir,myid), shell=True, stdout=subprocess.PIPE).stdout
            out=proc.readlines()
            ###save output into file
            out_file=open("%s/%s.out"%(out_dir,myid),"w")
            for row in out:
                line=row.decode().strip()
                out_file.write("%s\n"%line)
            out_file.close()  
        
