import os
import pandas as pd
import numpy as np

dir = os.environ["DIR"]
name = os.environ["NAME"]
a = pd.read_csv(dir + '/STEP14_out/vep_' + name + '_14.csv')
#Dropping the columns of uninterested
#a = a.drop('column_name_1','column_name_2', axix=1)

#Relocating the column of interest
################################
#####By their names############
###############################
#df = pd.read_csv(dir + '/STEP14_out/vep_gnomAD_14.csv')
#df_reorder = df[['A', 'B', 'C', 'D', 'E']] # rearrange column here

#you may need to use zip(*[['A', 'B', 'C', 'D', 'E']])
#df_reorder.to_csv('/path/to/sample_reorder.csv', index=False)


#dropping '.1' or any other prefix of affix
out = a.loc[:,~a.columns.str.endswith('.1')]
#write a csv file
out.to_csv(dir + '/STEP15_out/vep_' + name + '_15.csv')
