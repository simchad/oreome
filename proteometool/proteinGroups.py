"""
proteinGroups.py
~~~~~~~~~~~~~~~~

This module pre-process proteinGroups.txt

Example file (quan=TMT)
 `example\maxquant_opendata\\dataset_TMT\proteinGroups.txt`
"""
import os
import pandas as pd
from proteometool.lib import preprocessing

logged = os.getlogin()
DPATH = 'C:\\Users\\'+logged+'\\Desktop\\Documents\\'

data = pd.read_csv(filepath_or_buffer=DPATH, sep='\\t', encoding='utf-8')
df_base = preprocessing.base_proteingroups(df=data, quan="tmt")
print(df_base.head)

if __name__ == "__main__":
    print(__doc__)