"""
proteinGroups.py
~~~~~~~~~~~~~~~~

This module pre-process proteinGroups.txt

Example file (quan=TMT)
 `example\maxquant_opendata\\dataset_TMT\proteinGroups.txt`
"""
import pandas as pd
from proteometool.lib import preprocessing

data = pd.read_csv(filepath_or_buffer='example\maxquant_opendata\dataset_TMT\proteinGroups.txt', sep='\\t', encoding='utf-8')
df_base = preprocessing.base_proteingroups(df=data, quan="tmt")
print(df_base.head)

if __name__ == "__main__":
    print(__doc__)