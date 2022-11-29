#STEP 3_1
import pandas as pd
import sys
import csv
import os

#dir = os.environ["DIR"]
#name = os.enrivon["NAME"]

info_file = sys.argv[1]
out_file = sys.argv[2]

f = pd.read_csv(info_file, sep='\t')
#convert to dataframes
df = pd.DataFrame(f)

#Create a dictionary
# key = old name
# value = new name

dict = {'ID': 'ogn_ID'}

df = df.rename(columns=dict,inplace=True)
df['ID'] = df.apply(lambda r: str(r[0])+'_'+str(r[1])+'_'+r[3]+'_'+r[4],axis=1)
df.to_csv(outfile,index=False)

