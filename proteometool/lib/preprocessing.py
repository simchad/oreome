# preprocessing.py
"""
preprocessing
~~~~~~~~~~~~~

This module contains pre-processing functions

Internal
--------
_create_csv(df, target),

Functions
---------
column_filter_dict(df, **kwargs), split_itmes(df, **kwargs),
"""
__author__ = "github.com/simhc0714"

# Load packages.
import os
import pandas as pd
import re
from time import localtime, strftime
from api_request import requests_uniprot


# UDF
def column_filter_dict(df, **kwargs):
    """
    column_filter_dict(df, **kwrags) -> (df) pandas.DataFrame

    Filter and drop the column that have specific value in dict parameter.

    Parameters
    ----------
    - df (pandas.DataFrame) : *.txt format of Maxquant searched files.
    In normal, proteinGroups, peptides, PTM (X)Sites were included here.
    - **kwargs : {key:value} key is all column_name, value is the value in df.

    Notes
    -----
    General key, value for **kwargs are
    - Potential contaminant : +
    - Reverse : +
    - Only identified by site : +
    - Razor + unique peptides : 1
    """
    data = df.copy(deep=True)
    # 인수로 받은 df에서 value 값과 같은 key가 몇 개인지 -> 비율
    for key, value in kwargs.items():
        # drop한 entry 비율 = (value에 해당하는 key entry 수)/(전체 entry 수)
        total = len(data)
        entry = len(data[data[key] == value])
        ratio = 100*(entry/total)

        # key에 해당하는 entry 값이 value 인 entry 를 drop.
        data.drop(data[data[key] == value].index, inplace=True)

        # entry drop 후에 column을 drop 하고
        # message 출력합니다 (str, int) 다르게.
        if isinstance(value, str):
            data.drop(columns=[key], inplace=True)
            print('message! >>> '+str(entry)+' (%.2f%%) entries were dropped, [' %ratio +key+'] column removed.')
        else:
            print('message! >>> '+str(entry)+' (%.2f%%) entries were dropped. ['%ratio +key+' = '+str(value)+']')
    
    # 최종 몇개의 entry가 남았는지 출력 및 리턴
    print('message! >>> '+str(len(data))+' entries left.')
    return data


def split_items(df, **kwargs):
    """
    split_items(df, *kwargs) -> (df) pandas.DataFrame

    split items by delimiter and leave first value of them.

    Parameters
    ----------
    - df (pandas.DataFrame)
    - *kwargs : {column_name:delimiter}

    Notes
    -----
    Some columns in DataFrame have multiple values.
    For example in proteinGroups.txt, Protein IDs, Best MS/MS are separated with semi-colon (;).
    For delimiter separated value, first value is most abundant or major value.
    """
    data = df.copy(deep=True)
    for cname, delimiter in kwargs.items():
        tmp_series = pd.Series(data[cname])
        for elements in tmp_series:
            ele = elements.split(delimiter)[0]
            tmp_series.replace(elements, ele, inplace=True)
        print('message! >>> ['+cname+'] elements were splitted')
    return data


def column_tmt_reporter(df, type=None):
    """
    column_tnt_reporter(df) -> (reporter) list

    Return the column name list that contains related with TMT reporter ion.

    Parameters
    ----------
    df (pandas.DataFrame)
    type : Default is None. Available types are (None, corrected and count).

    Notes
    -----
    The Tandem Mass Tags (TMT) is useful for multiplexed-sample analyze.
    The TMT have bunch of product line-up, e.g., TMT-duplex, TMT6plex, TMT10plex.
    (N)plex TMT contains N different reporter ions.

    In maxquant searched file, there are few types of TMT relating data
    - type=None : Reporter intensity N.
    - type=corrected : Reporter intensity corrected N.
    - type=count : Reporter intensity count N.
    - type=all : All entries.
    """
    # initialize and set patterns.
    reporter = []
    col_name = df.columns.values.tolist()
    r = re.compile("Reporter")
    r_corrected = re.compile("corrected")
    r_count = re.compile("count")
    
    # Pattern match.
    reporters = list(filter(r.match, col_name))
    reporter_corrected = list(filter(r_corrected.search, reporters))
    reporter_count = list(filter(r_count.search, reporters))

    # Return result.
    if type == None:
        reporter = sorted(list((set(reporters)-set(reporter_corrected))-set(reporter_count)))
    elif type == "corrected":
        reporter = reporter_corrected
    elif type == "count":
        reporter = reporter_count
    elif type == "all":
        reporter = reporters
    else:
        raise ValueError
    return reporter


def column_silac(df, type=None):
    return None


def _create_csv(df, target):
    """
    _create_csv(df) -> (saved_path) str

    Create csv file with time point.

    Parameters
    ----------
    - df (pandas.DataFrame)
    - target (str) : (e.g., proteinGroups, peptides) use full name below.

    Notes
    -----
    Available targets
    - proteinGroups
    """
    # internal variables.
    ntm = strftime('%Y%m%d-%H%M%S', localtime())
    cwd = os.getcwd()
    saved_path = '.\output\\'+target+'_base_'+ntm+'.csv'

    df.to_csv(path_or_buf=saved_path, sep=',', index=False, encoding='utf-8')
    msg = 'message! >>> file created... '
    print(msg+saved_path)
    return saved_path


def _create_base_df(df, target, columns, drop=False):
    """
    _create_base_df(df, target, columns) -> (df) pandas.DataFrame

    internal function.

    Parameters
    ----------
    - df (pandas.DataFrame)
    - target (str) : See below notes.
    - columns (list) : 
    - drop (bool) : Default if False. If drop is True, drop the columns in columns.
    Then, create base df with left columns.

    Notes
    -----
    Available targets
    - proteinGroups
    """
    if target == "proteinGroups":
        df_base = df[columns].copy(deep=True)
    else:
        raise ValueError
    return df_base


def _create_base_proteingroups(df, quan=None):
    """
    _create_base_proteingroups(df) -> (df) pandas.DataFrame

    Create and save base file for proteinGroups.txt

    Parameters
    ----------
    - df (pandas.DataFrame)
    - quan (str) : (None, tmt, silac, lfq)

    Notes
    -----
    This file is the BASE file on ToxicoProteomics LAB.
    """
    # initialize.
    rest_cols = []
    rest_tmt = []
    rest_silac = []
    target = "proteinGroups"

    # Set rest_columns.
    base_cols = ['Protein IDs',
                 'Protein names',
                 'Gene names',
                 'Razor + unique peptides',
                 'Sequence coverage [%]',
                 'Mol. weight [kDa]',
                 'Sequence length',
                 'Q-value',
                 'Score',
                 'Intensity',
                 'Peptide IDs',
                 'Evidence IDs',
                 'Best MS/MS']
    if quan == None:
        # In normal
        rest_cols = base_cols
    elif quan == "tmt":
        # Case TMT
        rest_tmt = column_tmt_reporter(df, type=None)
        rest_cols = set(base_cols)+set(rest_tmt)
    elif quan == "silac":
        # Case SILAC
        rest_silac = column_silac(df, type=None)
        rest_cols = set(base_cols)+set(rest_silac)
    else:
        raise ValueError
    
    # Set filter options (base).
    base_filter = {'Potential contaminant':'+',
                   'Reverse':'+',
                   'Only indentified by site':'+',
                   'Razor + unique peptides':1}
    # Set which column split items.
    split_cols = {'Protein IDs':';',
                  'Best MS/MS':';'}
    
    # Process (Non-API).
    df_tmp = column_filter_dict(df, **base_filter)
    df_tmp = split_items(df_tmp, **split_cols)
    df_base = _create_base_df(df_tmp, target="proteinGroups", columns=base_cols)
    df_base.reset_index(drop=True, inplace=True)

    # Process (with API).
    df_respond = requests_uniprot.parser_id_mapping(df_base)
    df_base['Protein names'] = df_respond['Protein name']
    # ---------------------------------------------------------------
    # ---------------------------------------------------------------
    # ---------------------------------------------------------------
    # ---------------------------------------------------------------
    # -------------------------------------------------------23/04/29

    return None


def _create_base_peptides(df, quan):
    """
    _create_base_peptides(df) -> (df) pandas.DataFrame

    Create and save base file for peptides.txt

    Parameters
    ----------
    - df (pandas.DataFrame)
    - quan (str) : (None, tmt, silac, lfq)

    Notes
    -----
    This file is the BASE file on ToxicoProteomics LAB.
    """
    target = "peptides"
    return None


def _create_base_ptmsites(df, quan):
    """
    _create_base_ptmsites(df) -> (df) pandas.DataFrame

    Create and save base file for proteinGroups.txt

    Parameters
    ----------
    - df (pandas.DataFrame)
    - quan (str) : (None, tmt, silac, lfq)

    Notes
    -----
    This file is the BASE file on ToxicoProteomics LAB.
    """
    target = "ptm(X)sites"
    return None


if __name__ == "__main__":
    # debug
    pass