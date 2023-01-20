# processing_base.py

# --------------------------------------
# - proteinGroups.txt 로드 후 다음의 column data를 필터함.
# : contaminants, reverse, only identified site, uniquepeptide = 1 entries
# - protein names, Best MS/MS 항목에서 세미콜론(;) 구분된 데이터 요소를 split.
# - filter가 된 것을 *_base.xlsx 로 저장함.
# --------------------------------------
# processing_base.py 는 base-processing에 관한 것.
# proteingroups, peptides, evidence 등에 대해 각기 접근해야.
# class process_base() 만들고 각기 다른 파일에 대하여  class에 정의할 것.
# 그렇게 해야: __name__ == "__main__" 활용도가 높아져.
# __name__ == "__main__" 에서는 process_base 클래스에 배치된 def 함수만 사용할 것.
# --------------------------------------
# vscode 터미널에서 pip 안될때
# 원인: python 옳게 설치했더라도 윈도우 클래스에서 pip 위치를 알지 못하기에 발생.
# python3 부터는 pip 내장이므로 python.exe 디렉터리 연결하면 됨.
# C:\Users\Simon\AppData\Local\Programs\Python\Python39\Scipts 를 다음에 추가하면됨.
# (고급 시스템 설정 보기) - (환경변수 탭) - (사용자에 대한 사용자 변수 및 시스템 변수의 path에 추가)
# --------------------------------------
# 주피터 노트북에 익숙해지지 말고 파이썬 커널에 익숙해 져야해.
# --------------------------------------

# Load packages
import os
import csv
import pandas as pd
from api_requests import uniprot_requests
from time import localtime, strftime



# Set test sample path
global txtpath
txtpath = './raw_files/TestSample/LTQ_QC_DU145/'
# txtpath = './raw_files/proteinGroups.txt' <-- raw_files 폴더에 데이터 놔두면 실행 !!!



class DB_request_tools:
    # processing.py - DB_request class 로 관리할 것들은 ???
    def __init__(self, df):
        self.df = df
    
    # Uniprot DB request & respond
    def uniprot_request(self):
        # import uniprot_requests as unireq
        Prot_ids = pd.Series(self.df['Protein IDs'])
        #Prot_ids = ('A0FGR8', 'Q99613', 'O00148')
        #Prot_ids = ('A6NHR9', 'E9PAV3', 'O00151')

        link = uniprot_requests.execute(Prot_ids)
        # %2C[attribute]
        tsv_rst = uniprot_requests.get_id_mapping_results_stream(str(link)+'?compressed=true&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Clength%2Csequence&format=tsv')
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



class process_base_tools:
    # The tools for base-processing (drop column, split ';')
    def __init__(self, df, *args, **kwargs):
        self.df = df
        self.args = args
        self.kwargs = kwargs

    def isDrop(self):
        # **kwargs: keyword argument 줄임말. 인수를 딕셔너리로 받음.
        for key, value in self.kwargs.items():
            tmp1 = len(self.df)
            tmp2 = len(self.df[self.df[key] == value])
            ratio = (100*tmp2)/tmp1
            
            # key에 해당하는 value를 가진 entry 드랍.
            self.df.drop(self.df[self.df[key] == value].index, inplace=True)
            
            # value가 숫자인 경우: column 드랍하지 않음.
            # e.g., Razor + unique peptides의 경우, value = 1 인 entry 드랍 하지만, 나머지 entry는 남아야하므로.
            if isinstance(value, str):
                self.df.drop(columns=[key], inplace=True)
                print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped, [' %ratio +key+'] column removed.')
            else:
                print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped. ['%ratio +key+' = '+str(value)+']')
                # print('message! >>> '+str(tmp2)+' (%.2f%%) entries were dropped, ['+key+'] column removed' %ratio) <- 이 구문은 동작안함. %~~ 이게 string으로 나눈 같은 구역에 있어햐 함.
        
        # complete column drop
        print('message! >>> '+str(len(self.df))+' entries left.')
        return self.df

    # Split할 column 이름을 tuple (c1, c2)로 주고, delimiter의 기본값은 세미콜론(;)으로 되어있다.
    def split_items(self):
        for arg in self.args:
            tmp_series = pd.Series(self.df[arg])
            for ele in tmp_series:
                tmp = ele.split(';')[0]
                tmp_series.replace(ele, tmp, inplace=True)
            print('message! >>> ['+arg+'] elements were splitted')
        
        # reset index (important! --> <class>process_base:df1[]=df2[])
        self.df.reset_index(drop=True, inplace=True)            
        return self.df
    
    def create_base_df(self):
        rest = [
            'Protein IDs', 'Protein names', 'Gene names', 'Razor + unique peptides',
            'Unique sequence coverage [%]', 'Mol. weight [kDa]','Sequence length',
            'Q-value', 'Score', 'Intensity', 'id', 'Peptide IDs', 'Evidence IDs',
            'Best MS/MS'
        ]
        self.df = self.df[rest].copy()
        return self.df
    
    def create_csv(self):
        ntm = strftime('%Y%m%d_%H%M%S', localtime())
        cwd = os.getcwd()
        file_path ='./output/ProteinGroups_base'+ntm+'.csv'
        self.df.to_csv(path_or_buf=file_path, sep=',', index=False, encoding='utf-8')
        path_saved = cwd.replace('jobs','')+file_path
        print('message! >>> file created. '+path_saved)
        return None



class process_base:
    # The base-processing of each *.txt files.
    def __init__(self, df):
        self.df = df

    def proteinGroups_base(self):
        # For proteinGroups.txt
        #self.df = pd.read_table(filepath_or_buffer=txtpath+'proteinGroups.txt', index_col=False)
        base_filter = {'Potential contaminant':'+', 'Reverse':'+', 'Only identified by site':'+', 'Razor + unique peptides':1}
        split_cnames = ('Protein IDs', 'Best MS/MS')
        
        # Drop and split(;) on upper columns
        t = process_base_tools(self.df, *split_cnames, **base_filter)
        self.df = t.isDrop() 
        self.df = t.split_items()
                
        # Request protein.gene names to Uniprot-API
        f = DB_request_tools(self.df)
        pg_names = f.uniprot_request()
        
        # Replace protein/gene names from Uniprot-API 
        self.df['Protein names'] = pg_names['Protein names']
        self.df['Gene names'] = pg_names['Gene names']
        
        # Create base file (ProteinGroups_base.csv)
        self.df = t.create_base_df()
        self.df = t.create_csv()
        return None
    
    def peptides_base(self):
        self.df = pd.read_table(filepath_or_buffer=txtpath+'peptides.txt', index_col=False)
        return None
    
    def evidence_base(self):
        self.df = pd.read_table(filepath_or_buffer=txtpath+'evidence.txt', index_col=False)
        return None



# 아래의 딕셔너리 key:value 에 해당하는 entry를 제거하고 contam, reverse, only는 열을 제거합니다.
# 모든 열 이름 나열, 없으면 None. None이면 pass, 순차적 드랍.
if __name__ == "__main__":
    df = pd.read_table(filepath_or_buffer=txtpath+'proteinGroups.txt', index_col=False)
    job = process_base(df)
    job.proteinGroups_base()
    #job.peptides_base()
    #job.evidence_base()

