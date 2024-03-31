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

USER = os.getlogin()
DPATH = 'C:\\Users\\'+USER+'\\Desktop\\skku-hjh-s6k1\\g6.txt'
DPATH_2 = 'C:\\Users\\'+USER+'\\OneDrive\\Documents\\_ProteomicsLAB\\_proj\\undergrads\\TimeDep\\proteinGroups.txt'

data = pd.read_csv(filepath_or_buffer=DPATH_2, sep='\\t', encoding='utf-8')
df_base = preprocessing.base_proteingroups(df=data, quan="tmt")
print(df_base.head)

os.get

if __name__ == "__main__":
    print(__doc__)