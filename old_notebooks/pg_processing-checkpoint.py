import os
import pandas as pd
from time import localtime, strftime

def op_address(vers):
    wd = os.getcwd()
    tm = localtime()
    ntm = strftime('%Y%m%d_%H%M%S', tm)
    address = '/outputs/proteinGroups_v'+str(vers)+'-'+ntm+'.txt'
    return address

df = pd.read_table('./RawData/TextFiles/proteinGroups.txt')


df.drop(df[df['Potential contaminant'] == '+'].index, inplace = True)
df.drop(df[df['Reverse'] == '+'].index, inplace = True)
df.drop(df[df['Only identified by site'] == '+'].index, inplace = True)
df.drop(columns=['Only identified by site', 'Reverse', 'Potential contaminant'], inplace=True)


delContam = df.copy()
delContam.to_csv(path_or_buf='.'+op_address('0'), sep='\t', index=False, encoding='utf-8')


column_names = list(df)
rest = {'Protein IDs', 'Peptide counts (razor+unique)', 'Protein names', 'Gene names', 'Number of proteins',
        'Razor + unique peptides', 'Unique sequence coverage [%]', 'Sequence lengths' ,'Score', 'Intensity',
        'MS/MS count', 'id', 'Best MS/MS'}
filt = [ele for ele in column_names if ele not in rest]
df.drop(columns=filt, inplace=True)

prot = pd.Series(df["Protein IDs"])
for ele in prot:
    tmp = ele.split(';')[0]
    prot.replace(ele, tmp, inplace=True)
    
bmsms = pd.Series(df["Best MS/MS"])
for ele in bmsms:
    tmp = ele.split(';')[0]
    bmsms.replace(ele, tmp, inplace=True)

df.to_csv(path_or_buf='.'+op_address('1.1'), sep='\t', index=False, encoding='utf-8')