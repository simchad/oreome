import pandas as pd
from api_request import requests_uniprot

ids=["P05067", "P12345"]
df_respond = requests_uniprot.parser_id_mapping(data=ids)
print(df_respond)