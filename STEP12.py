import pandas as pd
import numpy as np
import os

dir = os.environ["DIR"]
name = os.environ["NAME"]

a = pd.read_csv(dir + '/STEP11_out/vep_' + name + '_11.csv',low_memory=False)
b = pd.read_csv('/sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/blacklist_hg38.txt', low_memory=False, sep='\t')
bl = pd.DataFrame(b)
df = pd.DataFrame(a)


df['Blacklist'] = (df['CHROM'].astype(str).isin(bl['Chr'].astype(str)))&(df['POS'].astype(str).isin(bl['Pos'].astype(str))) & (df['ALT'].astype(str).isin(bl['Alt'].astype(str)))
df.to_csv(dir + '/STEP12_out/12_' + name + '.csv')

