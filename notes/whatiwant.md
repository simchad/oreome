# 무엇을 구현할까

#### 이 문서와 연관된 파일
/root

</br>

#### C.U.R.D.
* Created : 2023/06/24
* Uploaded: 2023/06/24
* Revision: 2023/06/24

</br>

#### 목차
1. 무엇을 구현할까


</br>

# 1. 무엇을 구현할까?

> maxquant search 이후 파일. 특히, evidence, peptides, proteingroups

- 1.1 proteinGroups.txt

- 1.2 Modification (X)Sites.txt

- 1.x evidence

- 1.x peptides

    iPTMnet, dbPTM 매칭해서 매핑하는 것.

</br>

## 1.1 proteinGroups_vN.csv

첫번째로. proteinGroups.txt

버전 별로 포함된 feature가 달라짐.

*.txt 로 불러와서 *.csv/tsv 확장으로 저장.

</br>

### 1.1.1. proteinGroups_v0

</br>

> TMT, SILAC 등 정량적 분석에 관계없이 기본적인 데이터 전처리 목적

- Potential contaminant 제거.
- reverse 제거.
- only identified by site 제거.
- unique + razor peptides = 1 제거.
- Proteins IDs 등 ; (세미콜론) 구분 데이터에서 첫번째 값 남기기.
- Uniprot idmapping을 통해 protein name, gene name 가져오기.

> Uniprot idmapping.json parsing
- Protein name (RecName, AltName 등)
- Gene Name, sequence 등 필요한 데이터 파싱.

</br>

### 1.1.2. protinGroups_v1

</br>

> Reporting 용도의 feauture 만 포함

</br>

## 1.2. Modification (X)Sites.txt

- Logo 분석을 위한 alignment (ptm_logos.py)
- idmapping --> Sequence extract (Uniprot idmapping parsing)
- pLogo request
  - API 는 없을 것 같고, requests package 사용
- Motif 분석 중... Prosite 에서 ptm 포함되는 protein domain 있는지

</br>

# Reference
(1) 저자명 et al. 저널명 연도, 권(호):쪽수. doi:10.xxxx/xxxx.

