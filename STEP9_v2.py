import pandas as pd
import sys
from tqdm import tqdm
from multiprocessing import Process, Manager
from more_itertools import sliced

tqdm.pandas()

data_file = sys.argv[1]
biomart_file = sys.argv[2] #BioMart output file generated from get_biomart_data.R
outfile = sys.argv[3]

data=pd.read_csv(data_file, usecols=['ID', 'ENSP_v', 'AA_pos'])
biomart=pd.read_csv(biomart_file)

## return the protein domain info based on the protein id and aa position
def domain(myid, mypos):
    subtable=biomart.loc[biomart["ProteinStableIDversion"]==myid]
    if len(subtable)==0:
       return "Unknown"
    else:
        if pd.notnull(subtable["PfamID"]).any():
            check=0
            for j in subtable.index:
                start=int(subtable.at[j,"PfamStart"])
                end=int(subtable.at[j,"PfamEnd"])
                if mypos>=start and mypos<=end: # if mutation falls into domain region
                    return subtable.at[j,"PfamID"]
                    check=1
            if check==0:
                return "Outside_domain"
#        else: #no pfam info: check interpro
#            if pd.notnull(subtable["Interpro"]).any():
#                check=0
#                for j in subtable.index:
#                    start=int(subtable.at[j,"InterproStart"])
#                    end=int(subtable.at[j,"InterproEnd"])
#                    if mypos>=start and mypos<=end:
#                        return subtable.at[j,"InterproID"]
#                        check=1
#                if check==0:
#                    return "Outside_domain"
           
def get_annotations(df, return_dict, worker_index):
    print('%dth chunk started'%worker_index)
    df['Protein_dom']=df.progress_apply(lambda x: domain(x.ENSP_v,x.AA_pos), axis=1)
    print('Worker %d complete'%worker_index)
    return_dict[worker_index] = df

workers = 20
manager = Manager()
return_dict = manager.dict()
chunk_size = round(data.shape[0] / workers)
print(chunk_size)
jobs = []
i = 0
for chunk in sliced(data, chunk_size):
    p = Process(target=get_annotations, args=(chunk, return_dict, i))
    jobs.append(p)
    p.start()
    print('%dth chunk started'%i)
    i += 1

for proc in jobs:
    proc.join()

out = pd.concat([return_dict[i] for i in range(workers)], ignore_index=True)
out.to_csv(outfile, index=False)
