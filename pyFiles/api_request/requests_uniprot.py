"""
api_request.requests_uniprot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains function that mainly using with api_uniprot.py
"""

# import packages
import csv
import pandas as pd
from . import api_uniprot


# UDF
def _execute_id_mapping(id_series, db_from="UniProtKB_AC-ID", db_to="UniProtKB"):
    """
    execute(id_series, db_from, db_to) -> (link) str

    Parameters
    ----------
    - id_series (pandas.Series like)
    - db_from : default "UniProtKB_AC-ID"
    - db_to : default "UniProtKB"

    Notes
    -----
    link contains .json formatted context.
    """
    job_id = api_uniprot.submit_id_mapping(
        from_db=db_from, to_db=db_to, ids=id_series
    )
    if api_uniprot.check_id_mapping_results_ready(job_id):
        link = api_uniprot.get_id_mapping_results_link(job_id)
    return link


def parser_id_mapping(data):
    """
    parser_id_mapping(data) -> (df_respond) pandas.DataFrame

    Notes
    -----
    Parse rule : %2Cprotein_name, %2Cgene_names, %2Csequence.
    """
    # Set parse rule
    parse = "?compressed=true&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Clength%2Csequence&format=tsv"
    
    # Data type
    if (isinstance(data, list) or isinstance(data, pd.Series)):
        link = _execute_id_mapping(id_series=data)
    elif isinstance(data, pd.DataFrame):
        prot_ids = pd.Series(data['Protein IDs'])
        link = _execute_id_mapping(id_series=prot_ids)
    else:
        raise TypeError
    
    # Parsing
    tsv_rst = api_uniprot.get_id_mapping_results_stream(str(link)+parse)
    reader = csv.DictReader(tsv_rst, delimiter="\t", quotechar='"')
    df_respond = pd.DataFrame(list(reader))
    
    return df_respond


if __name__ == "__main__":
    pass