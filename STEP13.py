#importing some libraries
import pandas as pd
import numpy as np
import csv
import os

dir = os.environ["DIR"]
name = os.environ["NAME"]

#importing two files(1.VEP output including the blacklist; 2.GOF/LOF/Neutral reference file)
a = pd.read_csv(dir + '/STEP12_out/vep_' + name + '_12.csv')
b = pd.read_csv('/sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/LoGoFuncVotingEnsemble_preds_final.csv',sep='\t')

#VEP output
df1 = pd.DataFrame(a)
#GOF/LOF/Neutral reference
df2 = pd.DataFrame(b)

################################################################################################################
#STEP13. Adding a column of the prediction percentages of GOF/LOF/Neutral to GOF/LOF/Neutral reference file###
################################################################################################################

#(Format  GOF;LOF;Neutral)

##Dataframe to a list
ls=df2.values.tolist()

##Creating a list containing the prediction information (GOF;LOF;Neutral / Unknown (if all of the prediction values are less than 0.5))
V=[]
for i in range(len(ls)):
    if ((ls[i][1]>0.5) | (ls[i][2]>0.5) | (ls[i][3]>0.5)):
        V.append(str(ls[i][2])+';'+str(ls[i][3])+';'+str(ls[i][1]))
    else:
        V.append('Unknown')

##Adding the prediction list as a column of df2
df2['GOF/LOF/NEU']=V


##Merging the two dataframes
df3=df1.merge(df2,how='left',on=['CHROM','POS','REF','ALT'])
df3.to_csv(dir + '/STEP13_out/vep_' + name + '_13.csv')

