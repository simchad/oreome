# Comment (2023.01.18.)
# - MQpy/old_notebooks/pg_03_3_processing.ipynb 에서 시작.
# - 복붙 x. 타이핑 해가며 기억 깨우기...!
# - directory 달라져서 변경해야함. raw_files 폴더 위치 파일 사용하기.

# Scope

# - proteinGroups.txt 로드 후 다음의 column data를 필터함.
# : contaminants, reverse, only identified site, uniquepeptide = 1 entries

# - protein names, Best MS/MS 항목에서 세미콜론(;) 구분된 데이터 요소를 split.

# - filter가 된 것을 *_base.xlsx 로 저장함.

# vscode 터미널에서 pip 안될때
# 원인: python 옳게 설치했더라도 윈도우 클래스에서 pip 위치를 알지 못하기에 발생.
# python3 부터는 pip 내장이므로 python.exe 디렉터리 연결하면 됨.
# C:\Users\Simon\AppData\Local\Programs\Python\Python39\Scipts 를 다음에 추가하면됨.
# (고급 시스템 설정 보기) - (환경변수 탭) - (사용자에 대한 사용자 변수 및 시스템 변수의 path에 추가)

# 주피터 노트북에 익숙해지지 말고 파이썬 커널에 익숙해 져야해.

# 이 .py 파일이 기본처리(processing_base)인 만큼
# class를 proteingroups, peptides, evidence로 나누어서
# path를 알맞게 할당하면 멋진 .py 파일이 될 것.
# ------------------------
# Ex
# class ProteinGroups(txtpath)
#   def 1:
#   def 2:
#
# class Peptides(txtpath)
#   def 1:
#   def 2:

# class Request_and_respond()
# ------------------------

# Load packages
# import os
import csv
import pandas as pd
import uniprot_requests as unireq
from time import localtime, strftime



# Set test sample path
global txtpath
txtpath = './raw_files/TestSample/LTQ_QC_DU145/proteinGroups.txt'
# txtpath = './raw_files/proteinGroups.txt' <-- raw_files 폴더에 데이터 놔두면 실행 !!!


#cwd = os.getcwd()
#print(cwd)
#print(__name__)



# **kwargs 인수로 받는 함수... 클래스에 들어가면 init 잘 해야.
def isDrop(**kwargs):
    # **kwargs: keyword argument 줄임말. 인수를 딕셔너리로 받음.
    for key, value in kwargs.items():
        tmp1 = len(df)
        tmp2 = len(df[df[key] == value])
        ratio = (100*tmp2)/tmp1
        
        # key에 해당하는 value를 가진 entry 드랍.
        df.drop(df[df[key] == value].index, inplace=True)
        
        # value가 숫자인 경우: column 드랍하지 않음.
        # e.g., Razor + unique peptides의 경우, value = 1 인 entry 드랍 하지만, 나머지 entry는 남아야하므로.
        if isinstance(value, str):
            df.drop(columns=[key], inplace=True)
            print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped, [' %ratio +key+'] column removed.')
        else:
            print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped. ['%ratio +key+' = '+str(value)+']')
            # print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped, ['+key+'] column removed' %ratio) <- 이 구문은 동작안함. %~~ 이게 string으로 나눈 같은 구역에 있어햐 함.

    return print('message! >>> '+str(len(df))+' entries left.')



# Split할 column 이름을 tuple (c1, c2)로 주고, delimiter의 기본값은 세미콜론(;)으로 되어있다.
def split_items(*args, delimiter=';'):
    for arg in args:
        tmp_series = pd.Series(df[arg])
        for ele in tmp_series:
            tmp = ele.split(delimiter)[0]
            tmp_series.replace(ele, tmp, inplace=True)
        print('message! >>> ['+arg+'] elements were splitted')
    
    # reset index***
    df.reset_index(drop=True, inplace=True)    
    
    return None
    # return df.info




class DB_request_tools():
    # processing.py - DB_request class 로 관리할 것들은 ???
    def __init__(self, df):
        self.df = df
    
    # Uniprot DB request & respond
    def Uni_request(self):
        # import uniprot_requests as unireq
        
        Prot_ids = pd.Series(self.df['Protein IDs'])
        # Prot_ids = ('A0FGR8', 'Q99613', 'O00148')
        # Prot_ids = ('A6NHR9', 'E9PAV3', 'O00151')

        link = unireq.execute(Prot_ids)
        tsv_rst = unireq.get_id_mapping_results_stream(str(link)+'?compressed=true&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Clength%2Csequence&format=tsv')
        reader = csv.DictReader(tsv_rst, delimiter="\t", quotechar='"')
        df_sub = pd.DataFrame(list(reader))

        # 별일 없으면 순서는 같다. 단, indicies 일치해야.
        self.df['Protein names'] = df_sub['Protein names']
        self.df['Gene names'] = df_sub['Gene Names']
        self.df['Sequence length'] = df_sub['Length']

        return self.df

                
    
    # DAVID DB request & respond
    def DAVID_request(self):
        pass

    # KEGG DB request & respond
    def KEGG_request(self):
        pass

    # Reactome request & respond
    def Reactome_request(self):
        pass


    

# 로드한 파일의 모든 열에 대한 필터 옵션을 제공하는 것이 좋을지도
# split 도 마찬가지.
def ProteinGroups_base(drop_rule, split_cnames):
    # read txt file.
    isDrop(**drop_rule)
    split_items(*split_cnames)

    f = DB_request_tools(df)
    tmp = f.Uni_request()

    return tmp



# 아래의 딕셔너리 key:value 에 해당하는 entry를 제거하고 contam, reverse, only는 열을 제거합니다.
# 모든 열 이름 나열, 없으면 None. None이면 pass, 순차적 드랍.
if __name__ == "__main__":
    df = pd.read_table(filepath_or_buffer=txtpath, index_col=False)
    base_filter = {'Potential contaminant':'+', 'Reverse':'+', 'Only identified by site':'+', 'Razor + unique peptides':1}
    split_cnames = ('Protein IDs', 'Best MS/MS')
    tmp = ProteinGroups_base(base_filter, split_cnames)
    gname = pd.Series(tmp['Gene names'])
    tmp2 = gname[:6]

    print(tmp2)
    
# 아래: 필요한 column 추출해서 ./output/*.xlsx 만들기.