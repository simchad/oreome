"""
api_request.requests_uniprot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains function that mainly using with api_uniprot.py

Contains
--------

::
 _execute_id_mapping            --- Execute id-mapping job
 parser_id_mapping              --- Parsing .json result

See Also
--------

"""

# import packages
import csv
import pandas as pd
from proteometool.api_request import _api_uniprot


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
    job_id = _api_uniprot.submit_id_mapping(
        from_db=db_from, to_db=db_to, ids=id_series
        )
    if _api_uniprot.check_id_mapping_results_ready(job_id):
        link = _api_uniprot.get_id_mapping_results_link(job_id)
    return link


def parser_id_mapping(data):
    """
    parser_id_mapping(data) -> (df_respond) pandas.DataFrame

    Parameters
    ----------
    data : pandas.Series like or pandas.DataFrame type.

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
    tsv_rst = _api_uniprot.get_id_mapping_results_stream(str(link)+parse)
    reader = csv.DictReader(tsv_rst, delimiter="\t", quotechar='"')
    df_respond = pd.DataFrame(list(reader))
    
    return df_respond


def link_to_xtract(data):
    """
    link_to_xtract(data) -> (df_respond) pandas.DataFrame

    Parameters
    ----------

    Notes
    -----
    """
    # link to json stream data
    link = _execute_id_mapping(id_series=data)
    json_data = _api_uniprot.get_id_mapping_results_stream(link)

    # Xtract names from json
    num_sublist = json_data['results'].__len__()

    category_name = []
    pr_names = []
    entry_from = []

    for n_try in range(num_sublist):
        data_dict = json_data["results"][n_try]
        name_dict = data_dict["to"]
        phrase = "Protein Name Joined..."

        print('Processing... %d : %s'%(n_try, data_dict["from"]))

        if name_dict.get("proteinDescription") == None:
            entry_from.append(data_dict["from"])
            category_name.append("Deleted")
            pr_names.append('Deleted')
            print(phrase)

        else:
            try:
                pr_name = name_dict['proteinDescription']['recommendedName']['fullName']['value']
                entry_from.append(data_dict["from"])
                category_name.append('recommendedName')
                pr_names.append(pr_name)
                print(phrase)
            except:
                pr_name =name_dict['proteinDescription']['submissionNames'][0]['fullName']['value']
                entry_from.append(data_dict["from"])
                category_name.append('submissionNames')
                pr_names.append(pr_name)
                print(phrase)

    df_protname = pd.DataFrame({'From': entry_from,
                                'Category': category_name,
                                'Protein Name': pr_names
                                })

    # df_protname.to_csv(path_or_buf='C:/Users/simhc/Downloads/ProteinName_20241014.CSV', index=None, encoding='utf-8')

    return df_protname


if __name__ == "__main__":
    # Mainly test api interaction.
    ids = ['P09429', 'P00338', 'P10275', 'P60709']
    df_respond = parser_id_mapping(ids)
    print(df_respond.head)

    #