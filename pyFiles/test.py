import pandas as pd
from my_lib import preprocessing

df = pd.read_csv(filepath_or_buffer="example\maxquant_opendata\dataset_TMT\proteinGroups.txt", sep='\t', encoding='utf-8')

reporter = preprocessing.column_tmt_reporter(df, type=None)
print(reporter)