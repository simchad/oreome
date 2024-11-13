"""
diann-mapping.py
~~~~~~~~~~~~~~~~
"""

# Load packages.
import pandas as pd
from api_request import requests_uniprot


DPATH = "C:/Users/simhc/OneDrive/Documents/_ProteomicsLAB/UnderGrads/IntroOmics2024/PG_Team4.tsv"
OPATH = "C:/Users/simhc/OneDrive/Documents/_ProteomicsLAB/UnderGrads/IntroOmics2024/"

# import dataset
df = pd.read_csv(filepath_or_buffer=DPATH, sep="\\t", encoding="utf-8")
print(f"Data was imported")

# UP_ID to list object
ids = df['Uniprot Accession ID'].tolist()
print(f"Data contains {len(ids)} entries.")

mapped, link = requests_uniprot.mapping_to_xtract(data=ids)
print(f"Completely mappped and parsed")

mapped.to_csv(path_or_buf=OPATH+"mapped4.csv", encoding="utf-8", index=None)
print(f"mapped.csv have been saved.")