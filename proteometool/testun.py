# Load packages.
from os import getcwd
import pandas as pd
import re
from time import localtime, strftime
from proteometool.api_request import requests_uniprot
from proteometool.api_request import _api_uniprot


ids = ['P09429', 'P00338', 'P10275', 'P60709']

#link = requests_uniprot._execute_id_mapping(id_series=ids)

data_json = _api_uniprot.get_id_mapping_results_stream("https://rest.uniprot.org/idmapping/uniprotkb/results/ad13fd7c2f54490e2bbd36006fd61cf56ba9db31")


print(link)
