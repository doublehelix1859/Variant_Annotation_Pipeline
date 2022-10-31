import os
import pandas as pd
import numpy as np

dir = os.environ["DIR"]
a = pd.read_csv(dir + '/STEP14_out/vep_gnomAD_14.csv',low_memory=False)
#Dropping the columns of uninterested
#a = a.drop('column_name_1','column_name_2', axix=1)

#Relocating the column of interested
################################
#####By their names############
###############################
#df = pd.read_csv(dir + '/STEP14_out/vep_gnomAD_14.csv')
#df_reorder = df[['A', 'B', 'C', 'D', 'E']] # rearrange column here

#you may need to use zip(*[['A', 'B', 'C', 'D', 'E']])
#df_reorder.to_csv('/path/to/sample_reorder.csv', index=False)
