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

# Load packages
import pandas as pd
from time import localtime, strftime

# Set test sample path
global txtpath
txtpath = './raw_files/TestSample/LTQ_QC_DU145/proteinGroups.txt'

# Load proteinGroups.txt
df = pd.read_table(filepath_or_buffer=txtpath)

# df.info()
