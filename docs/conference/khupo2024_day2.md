# KHUPO 2024 - Day 2

## SYM B3: PTMs in diseases

### Cheolju Lee - KIST
> Distinguishing N-Terminal Methylation from Near-isobaric Modifications by Statistically Analysis of Mass Error Distributions of Fragment ions

- acetylation is the most abundant PTMs on N-termini region in mammalians, numbers of types of N-term mods exist (i.e., propiony, ...)
- N-terrminal methylation & Nt-methylome. Nt-Methylation is a Rare PTM so it requires enrichment for deep analysis.
- Canonical motifs... "XPK"
- N-terminal methylation charge positive, hydrophobic and hinderance.
- If you want to measure in MS, (mesurement error = measured - theoretical). Have to re-calibrate them. because, multiple electrons are skewed. 전자쌍 한쪽으로 몰림으로 m/z 측정시, peak 가 강한 치우침 생겨.
- y ion 다르고 b ion 다르다. 
- score: log10(pvalue-trimethyl) - log10(pvalue-acetyl)

#### Ex. 1 by 한결 Lee, student
> Chemically methylated BSA peptides.
- Before mass error test: acetyl, after that it assigned trimethyl. ppm 9.599, -1.9 ppm.

#### Ex.2 
> Methylated HeLa cell lysate, b-ion proprotion
- positive charge at n-termini higher probability of b-ion production -> compared the b-ion intensities.

#### Ex. 3.
> Methylated and acetylated HeLa cell Lysate
- positive charge at n-termini -> tmtm vs acac. RT is predicted by SSRCalc using unmodified peptide and then compare to observed RT of the corresponding modified peptides. (acac peptide was more later RT than tmtm)
- Comparison PSMs in actm and tmac models. 
- profiling of biological Nt-methylome
- Before going real applications, we are going one more models.

#### Ex.4 n-terminal peptides of HeLa Cell Lysate spiked with methylated BSA
> MET is useful not only to find true positive, but also remove false positive.
- with  increase of spiked-in amount: tmtm, acac BSA increases.
- highly likely true-positive trimethyl because they are from BSA

#### Deep-profiling of HCT 116N-terminome
- Nt-enriched by iNrich.
- Motifs: 
- after remove of the Met, first of amino acid sequence, acetyl transferases: A, S after removal of iMet, secondary acetyl transferase ME, MD.
- XPK is the main known canonical motif in dimethyl.
- Still discovering... I think Trimethyl motif is 50% acetyl and 50% dimethyl. so, guess that motif is M-D/E-K

#### Summary
- each ms2 spectrum b-ions will have mass error distribution compared to y-ions if the specturm is falsely assigned to near-siobaric nt-modification
- statistically to correct the nt-modification, a procedure we name as mass error test (MET)

#### Comment to Chair
> Main research theme is enrichment of n-terminal mthylation.

---

### Feng Ge - Chinese Academy of Sciences
> Lysine Acetylaion and Its Regulatory Enzymens in Cyanobacteria

- Lysine acetylation is dynamic, reversible. I focused on the N-termial amino acetylation.

#### Cyanobacteria
- Aldest photosynthetic organism and made the oxygen.
- Algal blooms, microalgae biofuels
- 23 different PTMs with high confidence in cyanobacteria.
- lysien acetylome in cyanobacterium, 1653 Kac on 802 proteins; involved in photosynthesis and carbon metabolism (MCP 2017; 16(7): 1297-1311)
- PsbO, 33kDa polypeptidem extrinsic subunit of photosystem II. it pplays an indespensable role in the ocygen evolution reaction.
- CddA play regulatory on photosynthesis.

---
### Young Joo Jeon - College of Medicine, Chungnam Univ.
> Protein language: post-translational modifcations (PTMs) talking to each other in cancer

- When she was kid of proteomics fields.
#### PTMs briefly introduce
- Wirters, Erasers and Readers on PTMs.
- Allow to regulate the protein fuction. i.e., singnaling, diversity, functionality of proteome.
- PTMs never exist in isolation. PTM cross talks on same or different proteins.
- PTMs, PQCs and Organismal Homestasis. 
- Ubs and UBLs. Ubs diverse roles depending on the type of Ub linkages. UBL, ISG15, specially relating on cancer.

#### ISG15
- Ubiquitin like protein.
- Have three sequential modifications: E2 -> E3 -> USP18 conjugate target protein.

#### Long journey to explore ISGlyome
> since 2003 to 2024.

- 2019: Nat comms. Combingin of ISG15 deficiency and enhanced ISGlyation with quantitaitve proteomics.
  
#### ISG15 & Me
- 2008 to 2016.

#### SIRT1 from the inactive state to promote deaceylase...
- Mammals involves SIRT1 to 7.
- SIRT1 known to nuclear shuttling. closely associated with chromatin remodeling in cancer.
- SIRT1 as a novel taret of ISGylation.

- SIRT1 ISGylation enhances its deacetylation activity
- SIRT1 ISGylation promotes tumor progression and limits therapeutic efficacy of lung cancer cells.
- SIRT1 ISGylation limits tumor responses to doxorubicin.
- Is associated with poor prognosis in human lung cancer
- Could amplify the antitumor effect of DNA damge-based theraeputics in cancer.

#### Next Journey: determine Kac dynamics by SIRT1 ISGylation.

---

## CW-2 (SCIEX)
### Doyoung Choi - Sciex Korea
> Next Generation SCIEX HRMS Zeno TOF System for BioPharma and Omics


---

## SS-2 (NCC)
### Sun-Yong Kong, NCC
> Proteogenomic analysis reveal prognostic subclass in early-onset breast cancer

- Molecular subtype analysis... 
- 조기발견은.. on the other hand... 연구용으로 좋지 않다.
- Young-age BCs (YBC) = early onset BCs.


### K. Sa - Korea Univ.
> Comprehensive molecular chracterizaion of krean advanced pan-cancer patients facilitates..

- Precision medicine era: background information, early detection, early treatment is most optimal therapy
- Current medicine: One tratement fits all
- Future medicine: More personalized diagnostic

#### Precision medicine era
- since obama legislation...
- Joe biden: cancer moonshot, by half within 25 years.
- Proof-of-concept: The three NEJM paper shown that personalized medicine drives well prognosis, and treatment.

#### Evolution of human genome research
- The human genome project contributes revolutionized the field of genomics
- Accerlation and advancement of the genome technology. REduction of costper genome, exponential growth in sequencing.
- Adaption and revolution of the cancer genomics field: TCGA, ICGC, initiated to perform series of large-scale moelcular characterization
- Real-world application of sequencing technilogy to guide clincial decisions. choice based on the genetic,,, driver of tumor progression. (NCI-Match Clincal Trial)

#### Ethnicity differences.
- Non American Ethnicity hard to directly use data sets.
- US ongoing comparison ethnicity e.g., black, white and hispanics


#### Korean-specific precision oncology intiative (Main)
- 4,028 patients with advanced solid tumors have been enrolled and molecularity charcterized ti identify major driver alterations.
- K-MASTER Pan-Cancer Cohort: not full sequncing, it is target-sequencing. target-sequencing is enought to analzses.
- Microsatellite instability is associated with increased response to immunotherapy. In clinical applcations. highly mutatated patients have good prognosis for immunotherapy.
- Mutational signature have revolutionized our understanding of cancer etiology. predictable prognosis of cancer patient.
- Dynamic interactions among major canonical oncogenic pathways. 9 to 10 major signaling pathway were identified on cancer. correalations between those pathways and cancer prognosis... then clustered.
- Bayesian model based probabilitic model identified co-occurence normal and cancer patients.

#### Genomic diverstiy (K-MASTER vs. TCGA)
- ~6,000 patients across two datasets. highly correlated. but, white were more activated PI3K than blacks.
- TP53 dynamically changed by ethincity. So, TP53 was higly dynamic mutation genes.
> comment: whty TP53 was easily mutated?

---
## SYM-A5: AI Driven Drug Development
### Sangtae Kim - NGeneBioAI Inc.
> AI-Enriched Proteomics: From Study Design to Data Interpretation

1. Experimental planning
- Creating a Lab Protocl usnig a LLM "Potato"
  - A ready-to-review protocol in minutes
  - Suggest the protcol in the lab.
  - Experimental designer: AI-aided experimental design
  - Experimental designer integration with the Cloud Platform. Easily to managing file names, file attributes, sample type, bunch of tags to manage them.
  
2. Data Collection
   - Quick het more sensitive signals
   - Hyubrid targeted-discovery methods. (Co. with Sang-won Lee, Korea Univ.)

3. Peptide digestion and data collection
   - DelPi: Deep Learning for Peptide Identification
   - Still, Over 50% of the dtaa remain uninterpreted
   - Interpreted: Canonical proteins, unmodified peptides, expected PTMs
   - How can dealing un-interpreted data?: Spectrum representation as a sentence. (e.g., CEFE -> (C,E,F,E))
   - ** Eric Kim, HUPO CANCUN, worked at google for 16 years.

#### How transffered "Black Box Diagnosis" into "Biomarker Discovery" ?


4. QC and Statistical analysis
   - ChatSQ: Analyze proteomics data using english as a programming language. Upload the data, chat on command then visualize the result of data.

#### Summary: We can enchanced every steps of proteomic pipelines

### Woo Youn Kim - KAIST
> AI-based accerlation of drug discovery

#### History of the computer-aided drug design
QSAR (1960s) -> CADD (1980s) -> Schoredinger (1990s) -> big-data based (2012) -> AF2 (2020) -> AF3 (2024)

- AI for fast & reliable virtual screening
  - Physics-based docking method. Two major problems of conventional approach: low reliability, reliatively slow, and trade-off between accuracy and speed.
  - Prediction of protein-ligand interaction: crystals vs in-vivo model completely different.
  - Solution A. Physics-informed deep learning. (Moon et al., Chem. Sci.)
  - Solution B. Data augmentation. (Moon et al., Digital Discovery. 2024)
  - Ultrafast virtual screening with pharmacophore (Seo & Kim, NeurIPS 2023, AI4DD workshop). 10^4 times faster with higher accuracy than the fasted docking method (Vina 3s vs PharmacoNet 0.0070). 

- Generative AI for de novo drug design

- Hyper LAb
  - Hyperlab platform. design the molecule.
  - launch this platform on Aug. 2023.
  - https://hyperlab.hits.ai/en


#### Comment: Significant motif region scaffolding with AF2 BLASTP --> profiling KAC. KAC도 PTM 있어야 Kac transferase 가능한가?


### Yirang Kim - Oncocross
> AI induced indication expansion based on transcriptome

1. AI 신약개발현황
- 2.5조 비용, 10-15년 걸리는 기간. AI 회사들이 하고 있는 일이.. 이를 획기적으로 줄이는 것.
- 그렇게 해도, 여러 제약사항 때문에 획기적으로 줄이기는 어렵고.. 임상이 5년정도 걸려. 10년 안쪽은 될 듯.
- https://github/com/CSB-L/AnoChem

2. 전사체 기반 AI 적응증 확대
- 보통 AI 기술은.. 후보물질 발굴과 임상시험에서 어떻게 대처해야할지 (병용요법 등) 을 사용함.
- ReDRUG algorithm, RAPTOR AI: 약물의 최적 적응증 또는 최적 병용투여약물 도출 예측.
- 데이터 수집 생성 -> 데이터 전처리 -> DEG, ONCO 3D scoring -> 세포-조직 비교: 약물의 세포와 질병 조직의 유사도 측정 -> 약물-질병 비교분석 -> 분석 결과 종합:Hybrid Score -> 추가 분석, MOA, 타겟 등.: 약물의 구조 정보와 전사체 정보를 종합하여 MOA 예측.


##  PL3: Glyco-redox and its role in EMT/MET and Cancer
### Nayuki Taniguchi - Osaka International Cancer Institute, Japan
> Glyco-redox and its role in EMT/MET and Cancer

