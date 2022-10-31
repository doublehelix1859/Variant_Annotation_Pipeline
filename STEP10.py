#Cigdem Sevim Bayrak, 2020
## run as 9.ptm.py <goflof_file> <path_for_inputfiles> (goflof file from 5.aa_properties)
## maps the PTM values based on protein name and position
import pandas as pd
from tqdm import tqdm
import sys
import tabix

goflof_file = sys.argv[1] ##goflof_DM_VEP_aa output of 5.aa_properties
path = sys.argv[2]#path for the resources on synology Itan_Lab/Projects/GOF-LOF/
out_file = sys.argv[3]

data = pd.read_csv(goflof_file)

phospho = tabix.open(path+"/Phosphorylation_sorted.txt.gz")
acet = tabix.open(path+"/Acetylation_sorted.txt.gz")
meth = tabix.open(path+"/Methylation_sorted.txt.gz")
ubiq = tabix.open(path+"/Ubiquitination_sorted.txt.gz")
gly = tabix.open(path+"/N-linkedGlycosylation_sorted.txt.gz")
gly_o = tabix.open(path+"/O-linkedGlycosylation_sorted.txt.gz")

def get_ptm(pos, uni, ptm):
    query = uni + ':' + str(pos) + '-' + str(pos)
    try:
        result = ptm.querys(query)
    except:
        return 0
    if len(list(result)) > 0:
        return 1
    else:
        return 0

out = []
for _, row in tqdm(data.iterrows(), total=len(data)):
    uni_id=str(row["SWISSPROT"]).split('.')[0]
    mypos=None
    try:
        mypos=int(row["AA_pos"])
    except:
        out.append([row['ID'], None, None, None, None, None, None])
        continue
    p = get_ptm(mypos, uni_id, phospho)
    a = get_ptm(mypos, uni_id, acet)
    m = get_ptm(mypos, uni_id, meth)
    u = get_ptm(mypos, uni_id, ubiq)
    g = get_ptm(mypos, uni_id, gly)
    if g == 0:
        g = get_ptm(mypos, uni_id, gly_o)
    ptm = max(p, a, m, u, g)
    out.append([row['ID'], p, a, m, u, g, ptm])


pd.DataFrame(out, columns=["ID", "Phosphorylation", "Acetylation", "Methylation", "Ubiquitination", "Glycosylation", "PTM"]).to_csv(out_file,index=False)
