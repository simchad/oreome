# preprocessing.py
"""
preprocessing
~~~~~~~~~~~~~

This module aims pre-processing of dataframe

Contains
--------

::
 _create_csv(df, target)
 _create_base_df(df, target, columns, drop=False)
 
 base_pept()
 base_proteingroups()
 base_ptmxsites()
 column_filter_dict(df, **kwargs)
 column_silac(df, type)
 column_tmt_reporter(df, type)
 split_itmes(df, **kwargs)

See Also
--------

markdown ->
notebook ->
"""
__author__ = "github.com/simhc0714"

# Load packages.
import os
import pandas as pd
import re
from time import localtime, strftime
from oreome.api_request import requests_uniprot # 2025.3.19
#from api_request import requests_uniprot

# Constants
LOGGEDUSER = os.getlogin()

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
    The Tandem Mass Tags (TMT) is useful for multiplexed-sample analysis.
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


def _create_csv(df, target:str=None):
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
    if target not in ["proteinGroups", "peptides"]:
        raise ValueError
    else:
        ntm = strftime('%Y%m%d-%H%M%S', localtime())
        saved_path = 'C:/Users/'+LOGGEDUSER+'/Documents/GitHub/oreome/output/'+target+'_base_'+ntm+'.CSV' # 2025.3.19 (output -> path)

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


def base_proteingroups(df, quan=None, mapping=False):
    """
    _create_base_proteingroups(df) -> (df) pandas.DataFrame

    Create and save base file for proteinGroups.txt

    Parameters
    ----------
    - df (pandas.DataFrame)
    - quan (str) : (None, tmt, silac, lfq) None 이외 미구현(2025.3.21)
    - mapping (bool) : (False, True) uniprot idmapping service


    Notes
    -----
    This file is the BASE file on ToxicoProteomics LAB.

    Issues
    ------
    - parameter quan: None 아닌 tmt, silac 일 때, column 이 섞여서 출력되는 문제.

    """
    # initialize.
    rest_cols = []
    rest_tmt = []
    rest_silac = []
    target = "proteinGroups"

    # Set rest_columns.
    # 2025.3.19 Essential columns set to base_cols, rest_cols are stayed.
    # base cols 기준이 아니라, 제거할 컬럼빼고는 모두 가져가야한다.
    # 이 기준에따라 코드 변경 필요함.
    # 2025.3.20 이전 base_cols
    """
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
        rest_cols = set(base_cols) | set(rest_tmt)
    elif quan == "silac":
        # Case SILAC
        rest_silac = column_silac(df, type=None)
        rest_cols = set(base_cols) | set(rest_silac)
    else:
        raise ValueError
    """
    
    # Set filter options (base).
    base_filter = {'Potential contaminant':'+',
                   'Reverse':'+',
                   'Only identified by site':'+',
                   'Razor + unique peptides':1,}
    # Set which column split items.
    split_cols = {'Protein IDs':';',
                  'Best MS/MS':';',}
    
    # Process (Non-API).
    df_tmp = column_filter_dict(df, **base_filter)
    df_tmp = split_items(df_tmp, **split_cols)
    #df_base = _create_base_df(df_tmp, target="proteinGroups", columns=rest_cols) 2025.3.21.
    df_base = df_tmp.copy(deep=True)
    df_base.reset_index(drop=True, inplace=True)
        
    if mapping == True:
        # Process (with API).
        request_rst = requests_uniprot.mapping_to_xtract(df_base['Protein IDs']) # 2025.3.19 parser_id_mapping -> mapping_to_xtract: protein/gene name 단일화 위하여 json mapping 사용.
        df_respond = request_rst[0] # 2025.3.20 request_uniprot.mapping_to_xtract return 은 tuple (df, link) 이므로 0번째 리턴해줘야 dataframe 형식임.
        df_base['Protein names'] = df_respond['Protein Name'] # 2025.3.19 fix: mapping_to_xtract df_mapped 설정에 맞게.
        df_base['Gene names'] = df_respond['Gene Name'] # 2025.3.19 fix: mapping_to_xtract df_mapped 설정에 맞게.
        #df_base['Sequence length'] = df_respond['Length'] # 2025.3.19 does not essential anymore...
    elif mapping == False:
        pass
    else:
        raise ValueError

    # Create csv file
    _create_csv(df_base, target='proteinGroups')
    return df_base


def base_diann(df, quan=None, mapping=False):
    """
    (df)pandas.DataFrame -> (df) pandas.DataFrame

    process DIA-NN result; report.pg_matrix.tsv

    Parameters
    ----------
    - df (pandas.DataFrame)
    - quan (str) : (None, lfq) None 이외 미구현(2025.3.21)
    - mapping (bool) : (False, True) uniprot idmapping service
    """
    # initialize.
    rest_cols = []
    rest_tmt = []
    rest_silac = []
    target = "proteinGroups"
    
    # Set which column split items.
    split_cols = {'Protein.Group':';'}
    
    # Process (Non-API).
    df_tmp = split_items(df, **split_cols)
    #df_base = _create_base_df(df_tmp, target="proteinGroups", columns=rest_cols) 2025.3.21.
    df_base = df_tmp.copy(deep=True)
    df_base.reset_index(drop=True, inplace=True)
        
    if mapping == True:
        # Process (with API).
        request_rst = requests_uniprot.mapping_to_xtract(df_base['Protein.Group'])
        df_respond = request_rst[0]
        df_base['Protein.Names'] = df_respond['Protein Name']
        df_base['Genes'] = df_respond['Gene Name']
    elif mapping == False:
        pass
    else:
        raise ValueError

    # Create csv file
    _create_csv(df_base, target='proteinGroups')
    return df_base


def base_peptides(df, quan):
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


def base_ptmxsites(df, quan):
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


class FromBase():
    def __init__(self, df, target, quan):
        self.df = df
        self.target = target
        self.quan = quan

    def split_names(self):
        return None
    
    def quan_ratio(self):
        # Set control, and experimental group(s)

        # Recognize how many experimental groups

        # N-plex tmt or silac
        return None


def from_base_split_names(df, quan):
    """
    from_base_split_names(df, quan) -> (df) pandas.DataFrame

    base_file still have sets of separated values (protein names, Gene Names).
    This function aims separate entry values or parsing well.
    
    Sure that, Gene Names sep is {space}.
    But, really problem is how separate Protein names.
    For example,
    - Immunoglobulin lambda constant 7 (Ig lambda-7 chain C region)
    - N-acyl-aliphatic-L-amino acid amidohydrolase (EC 3.5.1.14) (N-acyl-L-amino-acid amidohydrolase)
    - Acylamino-acid-releasing enzyme (EC 3.4.19.1) (Acyl-peptide hydrolase) (Acylaminoacyl-peptidase)

    (Solutions) How could they separate?
    - Uniprot Protein names `subsection`
    - https://www.uniprot.org/help/protein_names

    Parameters
    ----------

    Notes
    -----
    """


if __name__ == "__main__":
    print(__doc__)