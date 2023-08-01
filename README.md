# __Proteome-Tool__
## What is Proteome-Tool?
- Proteome-Tool 은 단백체학 학위 과정 중에 만들고 있는 취미 생활 겸 자기 계발 프로젝트입니다.
- 원활한 연구활동을 위해 데이터 전처리 자동화, API를 이용해 인포매틱스 정보를 인앤아웃하는 등 다양한 기능들을 구현함을 목표로 하고 있습니다.

<br>

---

## Tree

<br>

### Maxquant 데이터 핸들링 


### 데이터 전처리와 API 활용방안
1. [[Uniprot API] id mapping A to Z][Ext1]
2. [유용한 데이터 Parsing (예시 수록)]
   1. Uniprot idmapping.json
      1. idmapping_raw.json 데이터 구조
   2. SIB Prosite
      1. Prosite protein domain search
      2. 최대 10개?
   3. DAVID Bioinformatic Resources
   4. Gene Ontology
   5. KEGG
   6. Reactome

<br>

### 시각화 중심의 데이터 분석
1. [Motif 분석을 위한 sequence alignment][Ext2]
2. [데이터 N수에 따른 평균 차이 검정]
3. 연계 활용
   1. DAVID 에서 GO와 KEGG 연계하기
4. Clustering
   
<br>

### 같이 보기
1. [사용자 패키지는 setup.py 로 관리하자][Ext3]
2. [자주 등장하는 통계]
3. [Data integration tools]
4. [PrimerBank 에서 primer 검색 자동화]

<br>

---

## Upcomming

<br>

### Process *.txt file from MaxQuant Software.
- evidence.txt
- modification (X)Sites.txt
- peptides.txt
- proteinGroups.txt

### Visualization
- Correlations
- LE(%) for TMT, SILAC
- Box-plot, Venn-diagram, Volcano-plot
- Clustering: Hierachical, UMAP


### The others
- Uniprot: (ID mapping)
- DAVID
- Omics integration

# Updates (Major)
2022.06.16. Project released.<br>
2023.01.17. Renew (organize old files, Update folder structure.)<br>
2023.01.19. Uniprot API - id mapping


[Ext1]:https://github.com/simhc0714/proteome-tool/blob/main/notebook/upid_mapping.md
[Ext2]:https://github.com/simhc0714/proteome-tool/blob/main/notebook/ptm_logos.md
[Ext3]:https://github.com/simhc0714/proteome-tool/blob/main/notebook/setup-py.md
