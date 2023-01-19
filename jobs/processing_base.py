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

# Load packages
# import os
import pandas as pd
from time import localtime, strftime



# Set test sample path
global txtpath
txtpath = './raw_files/TestSample/LTQ_QC_DU145/proteinGroups.txt'

#cwd = os.getcwd()
#print(cwd)
#print(__name__)



# Load proteinGroups.txt
df = pd.read_table(filepath_or_buffer=txtpath)

df.info()



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
    


# read txt file.
df = pd.read_table(filepath_or_buffer=txtpath, index_col=False)



# 아래의 딕셔너리 key:value 에 해당하는 entry를 제거하고 contam, reverse, only는 열을 제거합니다.
base_filter = {'Potential contaminant':'+', 'Reverse':'+', 'Only identified by site':'+', 'Razor + unique peptides':1}
f = isDrop(**base_filter)



# Protein IDs, Best MS/MS 의 delimeter (;) 로 구분된 데이터를 나누어 첫 번째 항목을 저장합니다.
# 해당 column 이름을 1차원 series로 저장하고, deilmeter를 기준으로 구분한 뒤,
# 첫번째 값으로 replace 합니다.
# split에 사용한 객체는 초기화 되어야 합니다.

# (1) Protein IDs
prot = pd.Series(df['Protein IDs'])
for ele in prot:
    tmp = ele.split(';')[0]
    prot.replace(ele, tmp, inplace=True)
print('message! >>> [Protein IDs] splitted.')

# (2) Best MS/MS
bmsms = pd.Series(df['Best MS/MS'])
for ele in bmsms:
    tmp = ele.split(';')[0]
    bmsms.replace(ele, tmp, inplace=True)
print('message! >>> [Best MS/MS] splitted.')




# requests module 사용하여 web request-repond 프로세스를 수행합니다.
# uniprot accession 형식의 Protein IDs 를 Uniprot ID Mapping에 요청-응답 수행.
# 데이터프레임의 protein/gene name 및 sequence 등 항목을 수정해야 합니다.

# 참고페이지
# Uniprot API Help

import uniprot_requests
uniprot_requests.execute_ac_to_kb()

# link 통해 나온 결과는 stream.. 말그대로 텍스트의 엄청난 스트림!!
# get_id_mapping_results_stream 함수가 이 텍스트를 디코딩해서 필요한 부분만 뽑을 수 있게 해줌
# 규칙은 %2C[식별자], tap separated (.tsv) 형식 텍스트임.

tsv_rst = get_id_mapping_results_stream(str(link)+'?compressed=false&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Clength%2Csequence&format=tsv')


# 여기서 .tsv 형식을 df으로 바꿀 수 있음.

import csv
import pandas as pd

def get_data_frame_from_tsv_results(tsv_results):
    reader = csv.DictReader(tsv_results, delimiter="\t", quotechar='"')
    return pd.DataFrame(list(reader))

tmp = get_data_frame_from_tsv_results(tsv_rst)

tmp.head()