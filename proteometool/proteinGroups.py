"""
proteinGroups.py
~~~~~~~~~~~~~~~~

This module pre-process proteinGroups.txt

Example file (quan=TMT)
 `example\\maxquant_opendata\\dataset_TMT\proteinGroups.txt`
"""
# 작동 잘됨. 2024.08.02. 확인
# quan=tmt, silac 옵션 -> column 섞이는 현상.
import os
import pandas as pd
from proteometool.lib import preprocessing


PATH_NOW = os.getlogin()
PATH_EX = "..\\example\\maxquant_opendata\\dataset_TMT\\proteinGroups.txt"

#DPATH = os.path.join(PATH_NOW, PATH_EX)

data = pd.read_csv(filepath_or_buffer=PATH_EX, sep='\\t', encoding='utf-8')
df_base = preprocessing.base_proteingroups(df=data)
print(df_base.head)

# if __name__ == "__main__":
#     print(__doc__)