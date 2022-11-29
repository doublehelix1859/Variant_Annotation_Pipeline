import os
import sys
from tqdm import tqdm
import pandas as pd

info_file = sys.argv[1] 
out_dir=sys.argv[2] #directory with netsurfp outputs
outfile=sys.argv[3]

prot_info=pd.read_csv(info_file)
output_files=os.listdir(out_dir)
file_names=[s[:-4] for s in output_files] #except last 4 char: ".out"

rsa_class = []
rsa = []
asa = []
rsa_zfit = []
helix_prob = []
beta_prob = []
coil_prob = []
lists = [rsa_class, rsa, asa, rsa_zfit, helix_prob, beta_prob, coil_prob]

def append_none():
    for l in lists:
        l.append(None)

for i in tqdm(prot_info.index):
    myid=prot_info.loc[i,"ENSP_v"]
    if myid!="-":
        try:
            mypos=int(prot_info.loc[i,"AA_pos"])
        except:
            append_none()
            print(i, 'Could not get AA_pos')
            continue
        if myid in file_names:
            myfile=open("%s/%s.out"%(out_dir,myid),"r")
            mylines= myfile.readlines()
            header=0
            for line in mylines:
                if line.startswith("#"):
                    header+=1
                else:
                    break
            try:
                columns=mylines[header+mypos-1].rstrip().split() ##skip the header and read the columns
            except:
                append_none()
                print('Failed to read line')
                continue
            try:
                rsa_class.append(columns[0])
            except:
                rsa_class.append(None)
            try:
                rsa.append(columns[4])
            except:
                rsa.append(None)
            try:
                asa.append(columns[5])
            except:
                asa.append(None)
            try:
                rsa_zfit.append(columns[6])
            except:
                rsa_zfit.append(None)
            try:
                helix_prob.append(columns[7])
            except:
                helix_prob.append(None)
            try:
                beta_prob.append(columns[8])
            except:
                beta_prob.append(None)
            try:
                coil_prob.append(columns[9])
            except:
                coil_prob.append(None)
        else:
            print('ID not in file names')
            append_none()
    else:
        print('ID did not equal -')
        append_none()

for l in lists:
    if len(l) != prot_info.shape[0]:
        raise ValueError()
            
prot_info['RSA_class'] = rsa_class
prot_info['RSA'] = rsa
prot_info['ASA'] = asa
prot_info['RSA_Zfit'] = rsa_zfit
prot_info['Helix_prob'] = helix_prob
prot_info['Beta_prob'] = beta_prob
prot_info['Coil_prob'] = coil_prob

prot_info.to_csv(outfile,index=False)
