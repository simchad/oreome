# __Oreome__
## Introduction
- tOxicopROtEOMics Lab. Expansions
- 성균관대학교 독성단백체학 연구실 단백체 분석을 위한 자동화 파이프라인 프로젝트
- 원활한 연구활동을 위해 데이터 전처리, API를 이용해 인포매틱스 정보를 인앤아웃하는 등의 기능들을 구현함으로 연구실 데이터 처리 프로세스를 자동화함을 목표로 하고 있습니다.


<br>

---

## Context
우리 연구실에 적용하는 옵스

<br>

### Chapter 1. Shotgun Proteomics 데이터 핸들링
1. Maxquant
   1. Search 후의 디렉터리
   2. combined/txt 디렉터리의 파일들
      - proteinGroups.txt
      - Modification (X)Sites.txt
      - 그 외
   3. Maxquant, Perseus 데이터 export

2. Mascot

3. Proteome Discoverer
</br>

### Chapter 2. 데이터베이스 파싱과 API 활용방안
1. Uniprot: 넘버원 단백질 데이터베이스
   1. [Uniprot API 이용한 ID mapping][Ext1]
   2. [idmapping_yyyy_mm_dd.json 트리와 파싱][Ext4]

</br>

2. SIB Expasy: 인포매틱스 툴 여기 다 모였네
   1. Prosite & ScanProsite
   2. 최대 10개?

</br>

3. DAVID Bioinformatic Resources

</br>

4. Gene Ontology

</br>

5. KEGG

</br>

6. Reactome

<br>

### Chapter 3. 시각화 중심의 데이터 분석
1. [Motif 분석을 위한 sequence alignment][Ext2]

2. [데이터 N수에 따른 평균 차이 검정]

3. 연계 활용
   1. DAVID 에서 GO와 KEGG 연계하기

4. Clustering
   
<br>

### Chapter 4. 같이 보기
1. [사용자 패키지는 setup.py 로 관리하자][Ext3]

2. [자주 등장하는 통계]

3. [Data integration tools]

4. [PrimerBank 에서 primer 검색 자동화]

5. [ProteomeXchange 데이터 업로드와 SDRF]

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


[Ext1]:https://github.com/simhc0714/proteome-tool/blob/main/notes/upid_mapping.md
[Ext2]:https://github.com/simhc0714/proteome-tool/blob/main/notes/ptm_logos.md
[Ext3]:https://github.com/simhc0714/proteome-tool/blob/main/notes/setup-py.md
[Ext4]:https://github.com/simhc0714/proteome-tool/blob/main/notes/upidmapping_tree-parse.md
