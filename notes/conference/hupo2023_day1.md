# September 18, 2023. Monday

## PL02: Evolution to Micro-to-nano proteomics toward prceision oncology
__Keywords: precision medicine, DIA-MS, iProChip, EGFR__

Many challenges in a patinet journey…
mRNA != protein expression
proteogenomics very good tools..

### non-smoking lung cancer case (Cell, 2020)
	- proteogenomics revelas molecular subtypes.
	- that tools can nominate many unmet needs.
	- early detection and treatment for more cures.
	- high recurrence in "Late like" subtypes
	- ELISA diagnosis kits for early management.
	- 4-protein panel
	- blockade: different stage of patient…
	- traditional tissue proteomics (space-scale)
	- DIA based global phosphoproteomics system (GPS)
	- DIA greatly reduce missing values in phopshoproteome data.
	- DIA offers high sensitivity and coverage for tissue-phosphoproteome.

### Microproteomics
	- needle biopsy

### iProChip

### Smaple size-comparable spectral libraries for low-input samples.
	- small sample should adopt the other library.
	- sample-size compatible library DIA.

### Spectronaut version17.
	- LibDIA more powerful to detect low-abundance proteins than Direct DIA.


## CS01 Multi-omics

### CS01.1. Transformin Health with Deep Data and Remote Profiing
_Keynote Speaker: Michael Snyder (Standford University)_

__Between molecules and wearbles?__

- Billions of Measurements...
- wearable device and novel algorithms can mesure outliers, even covid-19 positive from physiological data.
- People react differentially on same action.
- Wearable data (over 2,000 person) >>> multi-omics
- microsampling make the lagged correlation possible.

__hPOP: humna personalized omics profiling__

__Notes__

웨어러블 디바이스를 이용한 수 많은 생리학적 신호를 바탕으로 수백~수천명의
개인에게서의 데이터(DGM, step, RHR, HRV, sleep and foold log)를 융합해서 의미있는 결과를 만들 수 있었음.
제시한 예시로

1. 생리학적 신호의 outlier 가 covid-19 detection 과 연관이 있었음.
2. 밤에 쉐이크를 마셨을 때 carbohydrate score가 사람마다 다르게 나타났는데, core diabetes marker를 설명함.


### CS01.2. Population Proteomics: A Path to Precision Medicine.
_Keynote Speaker: Chris Whelan (Neuroscience Data Science J&J)_

__'precision medicine' is still a buzzword (scienfiction). why?__
- Right drug X.
- Right patient X.
  - mRNA != protein levle
- Right time X.

but proteomics possible.
- Drug
- Patient
- Time
  - Protein is dynamic.

__New Paradigm: Genomics >>> Proteomics__

- DBs: UK Biobank(UKB), PPP(Pharma Proteomics Project), pQTL
- Population proteomics is helping us translate humanity's instruction book
- Find hundreds of new therapeutic targets.
- Find more disease-specific biomarkers.
- Over 3,000 proteins from over 5,000 different individual.
- Build better diagnostics.
- 5-20 biomarkers... Proteomic prediction of common and rare diseases, medRxiv, 2023
- UK Biobank is an international research power-house, open-access

__next for population-scale proteomics__
- Greater diversity
- More disease-specific profiling
- ELISA (NULISA?) at scale
- MS, at scale
- Most importantly, complex of biology, We need to MS and integrate them.
  

__Note__

2000년대 초반부터 genomics 가 유행했는데 여전히 precision medicine은 공상과학처럼 들린다. 이 이유는 genomics 바탕의 것은 한계가 있기 때문에.
그래서 genomics 에서 조금 더 dynamic 한 proteomics 로의 전환을 시도했다.

UK Biobank 데이터와 PPP project 를 통해서 인구집단의 proteomics 


QA, 많은 제약사에서 drug의 부작용을 PTM을 통해서 제어하려고 시도 중임.

### CS01.4. Proteomic Analysis of Human Pancreatic Ductal Adenocarcinoma
_Do Young Hyeon (SNU)_

Published: Hyeon et al., Nature Cancer, 2023 (doi.org/10.1038/s43018-022-00479-7)

- 196 individuals, Exome-seq, RNAseq, MS based prtein abudnace and phospho-


### CS01.5. Integrative Proteogenomics Profiling Uncovers Non-histone Protein Methyltransferases as Novel Therapeutic Targets in Diffuse Midline Glioma
_Arun Kumaran Anguraj Vadivel (The Hospital for Sick Childeren, Toronto, Canada)_

DMG: H3K270altered (H3K27M or EZHIP O.E.)

Methods

- WGS, DNAmethylation, RNAseq
- TMT11plex
- LC-MS3 (Fusion Lumos)
- Proteome discoverer

Translation initiation highly phosphorylated and translation elongation is hughly methylated.


## Thermo Lunch Symposium
### ISS04: Deep Exploration into Proteome Universe Combinding Proteograph XT Worflow with Orbitrap Astral MS

_Daniel Hornburg, USA (Seer Inc)_
- PosDoc in Pfizer, and standford synder lab.

Seer's enriched plasma solutions.

__Combination of depth and scale is required for discovery__
- Depth of coverage and study size
- Limited potential for discovering more biomarkers
- "ProteographXT"

Negatively charged protein in your blood...

You can engineering in biosamples.

__ProteographXT__
- compatible with different sample types.
- 4~7.7X improvements in blood (serum, plasma)
- 1.5~12X for media

__Specific data__
1. AD Plasma
- AD plasma from 1,800 subjects DIA LC0MS with Exploris 480... over 5k proteins.
- Large-scale AD plasma study reveals potentially new insights into complex disease.
- 10+ new biomarkers.
- potential mechanisms, signaling...

2. non-small cell lung cancer (NSCLC)
- DEPs can lead to better biomarker discovery and disease charaterization
- Differential abundance analysis between cancer and healthy subject from lung carcinoma study
- Poster# PP05.109 "Proteoform Detection in Deep Plasma Proteomics using Peptide..."
- Isoform also important! Protein splice variants.

__Quantification__
- peptide abundacne changes across conditions.
- Linearity for biomarkers.
  - selecting most linear peptide to evaluate performance in rapid untargeted lc-ms workflows
  - Huang et al., BioRxiv, 2022.
  - 

__Astral MS__
- DIA-NN v1.8.1 software.

__Deep plasma proteome of astronaut shwos spaceflight response__
- 7 astronauts across 2 space X mission with 37 samples collected pre-flight, the day of landing form space and post-flight, +7k proteins.
- What expect?
- on going study.

__Notes__
아스트랄은 single-cell 특화 장비이기도 한데, seer 의 plasma platform 을 겸용해서 coverage 향상시키는데 big-step을 밟았다고 설명. 두가지 적용 사례를 소개 했는데 첫번째인 AD에서 high abundance protein을 따로 정제하지 않고서도 5천개 이상의 단백질 그룹을 뽑아냈고 여기서 새로운 바이오마커들을 10개정도 발굴함.

두번째 연구는 NSCLC 에 관한 것으로 포스터 PP05.109를 참고.

정량에 관해서... peptide abundance를 가지고 linearity 하게 정량함. 이를 통해서 단백질의 편차를 줄일 수 있었음.


## CS06: 3 minutes thesis competition

__Mane Polite Roneldine Mesidor__
- nanoCSC platform
  - surface proteins are important
  - 50% reduction in starting material.
  - only 8 hours: 80% reduction in processing time.
  - so develop nanoCSC platform

</br>

__Alireza Nameni (VIB-UGent)__
- iDeepLC: Unraveling proteins mysteries using AI
- amino acid sequence for input data set >>> AI >>> 30min.

</br>

__Dian Schuster (ETH Zurich)__

How to study flexible domain on membrane proteins.

- combining cyroEM, limited proteolysis-coupled ms and croslinking ms.
- posters on wednesay

</br>

__Janaian Silva, Brazil__

Protein arginylation: A new ky palyer in SARS CoV-2 infrction

- Such as PTM, mediate ATE1 enzyme.
- ATE1 silencing reduces profilation in GBM.

</br>

__Justin Sing, Canada (Rost LAB, Univ. of Toronto)__

Enhancing Cosistent Quantification of Site-Localized PTM in Large-scale DIA-MS Experiments

- consistent quan. of PTM isomers challenge
- PTM inference with ion mobility information

</br>

__Dafni Skiadopoulou (Univ. of Bergen, Norway)__

Precesion medicine to proteome level.

</br>

__Xue Sun, (Bejing university, China)__

</br>

__d__

Host-pathogen interaction

- streptolysin O (SLO) bind to juman palsminogen (PLG)
- Bacteria acquire additional plasmin actibity.

</br>

__Marvin Thielert(Max Planck, Germany)__

Making single-cell proteomics biologically relevant

</br>

__Takehiro Tozuka, Japan__

Mutual phophorylation ~ in mutant NSCLC

- FAK and Src inhibition may be novel treatment strategies for Osi-resistant NSCLC.
- Phopshoproteomics analysis may help elucidate the mechanisms of resistance to targeted therapy.

</br>

__Yun-Jung Yang, Taiwan__

Anotibody Glycosylation as COVID-19 Vaccine Response Indicators in ESRD Patinets

Responders and non-responders are glycosylated differently
- Their Abs function differntly.
- Responders are glycosylated as general population, but with a delayed Ab response.

</br>

__Yu Zong, China__

DeepFLR facilitates false localization rate(FLR) controls in Phosphorylation

FLR estimated = (decoy + target) / (decoy) X (D/T+D)

## Bioinformatics Hub M4: HPP Metrics and Knowledge Base

_Release 2023-09-11 NextProt_

- Most contributing new datasets (peptide atals): PXD028647 (5) and PXD019643 (32)
- all FDR per PSM is same
- FDR can dfferentially move by search engine.
- An olfactory receoptor: we don't have full coverage of it.

Why dataset numbers were drop?
- criteria of amino acid polymorphysm, excluding them.

## Bioinformatics Hub M5: ProteomeXchange Data Repositories
### General
- no nedd to convert raw files for Thermo RAW files
- mcml, mgf

__Improved support for USIs__
- ms peak generator

### (Clinical) Human Sensitive Proteomic data

__Legislation - Patient protection and general regulations__
- Patinet consent
  - The patient must have control over the data generate by using their own samples.
- General regulations like GDPR in EUrope

__Need to have controlled access data repositories for proteomics data__
- PRIDE and MassIVE to have dedicated controlled-access.
- Work in Progress:
  - Infrastructure - Data security is critical
  - Legal framework
- Researchers will have to apply to get access to these datasets.
  - But this is preferable.

__MAGE-TAB-Proteomics: IDF + SDRF-Proteomics__

- New tool for creating SDRF-Proteomics: lesSDRF

__Note__
PRDIE 에서 clinical 하거나 human sensitive 정보를 업로드 하려면 어떻게 해야하는가?

기본적으로 규정으로 정해져있다. 환자에게서 나온 모든 데이터는 환자가 관리할 수 있어야 한다는 기본 원칙. 그렇다면 이러한 환자 단백체 데이터는 어떻게 관리하여야 하는가? DB 공급자가 자체적으로 접근할 수 있는 권한을 관리해야함. 연구자들은 이러한 데이터에 접근하기 위해서는 접근 권한에 대해서 신청해야함.

## PL03: Manuscript Competition

### PL03.01. Immobility-associated Thromboprotection is Conserved across Mammalian Species from Bear to Human
_Johannes Bruno Muiller-Reif (Matthias LAB., Max-planck, Germany)_

How to study a non-model organism on molecular level? (Bear)

Publication: "Sleep like a bear". Science. 2023

__Note__

</br>

### PL03.02. Global Detection of Human Variants and Isoforms by Deep Proteome Sequencing
_Pavel Sinitcyn, (COON LAB. United States)_

Who is MaxQaunt, MaxDIA algorithm conributed.

Human genome >> different slice (mRNA variant) >> site-specific modify >> proteoform

- Trypsin and Glu+C digested peptide pooling.
- Different protease have different coverage.

__single amino acid polymorphisms (SAPs)__

- hard to detect

__Alternative Splicing (AS)__

- Alternative splicing events and isoforms totally different
- not local we called events.

example, amyloid precursor protein
- exon skipping vs no skipping

__Out-of-frame AS are not present on the proteome level__

__Note__

</br>

### PL03.03. Dissecting the Blood Ecosystems in SARS-CoV-2 Omicron Patients
_Hong Wang, (Pecking Union Medical College, China)_

__Focus__
- Host response dynamics along disease stages
- Re-positivity (Turn positive again) for viral RNA in Omicron patients.

__Blood ecosystem approach to dissect systemic diseases__

__3M Strategy: Multi-omics, Multi-specimens, Multi-phases__
- Plasma integration shows platelet dynamics
- MOFA (Multi Omics Factor Analysis)

__Note__