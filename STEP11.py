import pandas as pd
import sys
import os
from functools import reduce

dir = os.environ["DIR"]
name = os.environ["NAME"]

#Step4_2 output
f1 = pd.read_csv(dir + '/STEP4_2_out/vep_' + name + '_4_2.csv')
f1 = f1.drop_duplicates(subset='ID')
#step4_3 output
f2 = pd.read_csv(dir + '/STEP4_3_out/vep_' + name + '_4_3.csv')
f2 = f2.drop_duplicates(subset='ID')
#step4_4 output
f3 = pd.read_csv(dir + '/STEP4_4_out/vep_' + name + '_4_4.csv')
f3 = f3.drop_duplicates(subset='ID')
#step8 output
f4 = pd.read_csv(dir + '/STEP8_out/vep_' + name + '_8.csv')
f4 = f4.drop_duplicates(subset='ID')
#step9 output
f5 = pd.read_csv(dir + '/STEP9_out/vep_' + name + '_9.csv')
f5 = f5.drop_duplicates(subset='ID')
#step10 output
f6 = pd.read_csv(dir + '/STEP10_out/vep_' + name + '_10.csv')
f6 = f6.drop_duplicates(subset='ID')

#Merging
out = f1.merge(f2, on='ID', how='left')
out = out.merge(f3, on='ID', how='left')
out = out.merge(f4, on='ID', how='left')
out = out.merge(f5, on='ID', how='left')
out = out.merge(f6, on='ID', how='left')

out.to_csv(dir + '/STEP11_out/11_' + name + '.csv')

#dropping '_y' and removing '_x'
f12 = pd.read_csv(dir + '/STEP11_out/11_' + name + '.csv')
out = f12.loc[:,~f12.columns.str.endswith('_y')]
out.columns = [col.replace('_x', '') for col in out.columns]
#write a csv file
out.to_csv(dir + '/STEP11_out/11_' + name + '_fix.csv')
