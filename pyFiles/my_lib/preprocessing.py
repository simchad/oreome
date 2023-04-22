# preprocessing.py
"""
preprocessing
~~~~~~~~~~~~~

This module contains pre-processing functions
"""
__author__ = "github.com/simhc0714"
__version__ = "0.0.1"

# Load packages
import pandas as pd
import re


# class: API using functions

# class: Non-API functions


# 처음, MQsearch.txt 에서 주요 column 기준에 따라 필터링.
# kwargs = filter
# base_filter = {'Potential contaminant':'+',
#                'Reverse':'+',
#                'Only identified by site':'+',
#                'Razor + unique peptides':1}
# Razor + unique peptides: 기본값 False로 주고, True 이면 1로.

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
    - Potential contaminant: +
    - Reverse: +
    - Only identified site: +
    - Razor + unique peptides: 1
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

    split items by delimiter and leave first value of them

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
    column_tnt_reporter(df) -> reporter (list)

    Return the list that contains type of reporter ion columns contained column name.

    Parameters
    ----------
    df (pandas.DataFrame)
    type : Default is None. Available types are (None, corrected and count).

    Notes
    -----
    The TMT (Tandem Mass Tags) is crucially useful for multiplex sample analyze.
    The TMT have bunch of product line-up, e.g., TMT-duplex, TMT6plex, TMT10plex.
    (N)plex TMT contains N different reporter ions.

    Mostly, reporter intensity N corrected and reporter intensity N is same.
    """
    reporter = []

    return None