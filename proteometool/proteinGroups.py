"""
proteinGroups.py
~~~~~~~~~~~~~~~~

This module pre-process proteinGroups.txt

Example file (quan=TMT)
 `example\maxquant_opendata\\dataset_TMT\proteinGroups.txt`
"""
import pandas as pd
from proteometool.lib import preprocessing

DPATH = 'C:\\Users\\simhc\\Desktop\\skku-hjh-s6k1\\g6.txt'
DPATH_2 = 'C:\\Users\\simhc\\OneDrive\\Documents\\_ProteomicsLAB\\_proj\\undergrads\\TimeDep\\proteinGroups.txt'

data = pd.read_csv(filepath_or_buffer=DPATH_2, sep='\\t', encoding='utf-8')
df_base = preprocessing.base_proteingroups(df=data, quan="tmt")
print(df_base.head)

if __name__ == "__main__":
    print(__doc__)