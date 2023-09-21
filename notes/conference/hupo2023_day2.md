# September 19, 2023. Tuesday

## PL04: Technological Advances in MS-based Proteomics Applied to Single Cell Type Analysis in Cancer Tissues
_Matthias Mann, Germany_

__Our LC-MS workflows__
- Bravo, Opentrons
- PepSep, Ionopticks, uPAC

__Interests__
- 10X Proteomics
- Bioinformatics and the dark proteome
- PTM etc.

### Research Fields

__AlphaX packages__

Tens of python based packages available online, and applied mojo which lang for ai.

__PTM colocalization in 3D space__

__And what is next?__

- Combining in chatAI with proteomcis
- AlphaPeptStats
- PASEF
- nanoTips for single cell: All procedures are included in this.

### Main topic

__Deep Visual Proteomics (DVP)__
- Disease progression is related to spatial proteomic changes
- In human tissue smaple.... H&E staining sample...
  - tissue
  - cell types
  - cells
  - single-cell

### Notes
다양한 프로테오믹 툴을 제공함. 깃허브 마티아스랩 참조. 단일세포의 공간적 정보를 바탕으로 하는 DVP workflow에 포커스를 맞추고 있음. DVP의 골자는 환자 조직을 염색하고 cell type 을 분류한뒤 셀 타입별로 단일세포 분석을 해서
7~8천개의 depth 가 나옴. 임상에서 적용 예시로는 rash (발진, 두드러기) 를 소개하였음. 심한 발진의 경우에 interferon 관련 단백질이 크게 작용하는 것으로 보여 연구를 진행 중이라고 함.

## CS15: Spatial and Imaging Proteomcis

### CS15.01: Bioorthogonal Chemistry enabled Spatial-temporal Proteomics
_Peng Chen, China_

- the spatial-temporally organized proteome is essential for life.
- genetically enconded bioorthogonal chemistry in living systems?
  - single protein study: biochemistyr, x-ray, nmr, cryoEM
  - but cell has so many multiple protein: how spatial in cell?
  - "Click link" in protein
- Activated one protein in cell. "One-at-a-time" ?
- Activate just one kianse in kinase group, then what happening?
- How? use BCRs for "Protein Decaging", pocket-specific ATP.
- RAF-MEK-ERK pathway...
- Weng T et al. Nat Chem Biol. In Press: Y55 Phosphoryltion UBA1
- protein pocket에 genetically modified 된 caging 장치를 부착해서 substrate의 결합을 control 할 수 있음. 이 곳에다가 ATP를 보내는 식으로 단백질 활성화를 조절할 수 있음.

- Spatial proteomics enabled by bioorthogonal photocatalysis
  
__Note__

단일 단백질의 spatial 보는 것은 이미 잘 알려져있다. cryoEM, X-ray, NMR 등을 사용하면 된다. 그런데 세포에는 하나의 단백질만 있는 것은 아니야. 그렇다면 다중의 단백질의 spatial한 정보는 어떻게 접근해야하나?

그래서 본 연구팀은 세포에서 하나의 단백질 만을 활성화 시킬 수 있는 방법을 연구했다. 수 많은 kinase 들 중에서 단 하나만의 kinase를 활성화 시킨다면 어떤 일이 벌어지는 지를 연구했다.

유전적으로 변형된 단백질(caging 장치를 붙여서) substrate의 결합을 조절할 수 있게 만들었다. 단백질을 활성화 시키는 ATP 가 결합하는 자리에 caging을 만듦으로써 ATP 조절을 통해 단백질 활성화를 조절할 수 있게 됨. 이런 caging 장치는 uv light을 줌으로써 열리게(substrate 결합할 수 있게) 할 수 있음.

PTM 조차도 UV Xlinking을 함. Lingking chromatin mark-defined proteome and genome.

QA1. bioorthogonal photocatalytic decaging은 genetically mutation이 필요없음. transfection이 필요 없다는 말.

QA2. Really photo-switchable catalyst 라서 uv-off 하면 deactivate 가 되기에 photo-toxic에 대해서 critical 하게 생각하지 않아도 된다.

QA3. Our research is more substrate identification.
두가지 방법. genetically modified OR photo-switchable caging

</br>

### CS15.02: A Spatio-temporal Single-cell Type Map of Human Tissues
_Cecila Lindskog, Sweden_

- HPA is the open access resource for human proteins
- 2023.06 release interaction ATLAS

__today focus tissue and single cell type ATLAS__

Pub. "Tissue-based map tof the human proteome", Science. 2015

- UMAP clustering based on expression similarity across all cell types and also nearest neighbours.
- Increasing resolution of the tissue-based data
  - new cell types, rare tissues

__Single cell type - In which cell types are proteins expressed?__
- Taking tissue and single cell type specificity to the next level.

__Example: Testis__
- Many cell types, germ maturation...
- scRNAseq clustered subcluster for spermatogonial, spermatocytes, spermatids.

__Ongoing works__
- Automated annotation of protein expression
- Female tissues
- Visualization in the HPA databases
  
__Note__

HPA는 human 단백질에 대한 오픈액세스 DB인데, 90년대 후반 부터해서 계속 단백질 관련 db를 업데이트 해왔음. 올해 6월에 interaction관련 atlas를 공개했는데 오늘 주제는 tissue와 single-cell 에 관련하여 발표하였음.

개략적인 워크플로우는 조직을 염색하고 scRNA를 한 뒤에, antibody-specific 데이터와 합침.

예시로는 testis 선택. 그 이유로, testis 는 germ cell 이 maturation 되는 등 temporal 정보가 많기 때문이었음.

</br>

### CS15.03: Statistical Approach to Predict Lymph Node Metastasis in Endometrial Cancer using Mass Spectrometry Imaging
_Peter Hoffmann, Austraila_



</br>

### CS15.04: Multiplex-DIA and Deep Visual Proteomics Enhances Spatially-Resolved Proteome Resolution to Uncover the Landscape of Pancreatic Islet Biology
_Marvin Thielert, PhD Candidate, Matthias LAB., Germany_

- Type-2 diabetes disrupts pancreatic islets compared to normal one.

__DVP with multiplex-DIA__

Workflows

    archive pateint tissue sample >> high-resolution imaging >> imageing segmentation using DL >> ML algorithms are trained to predict cellualr phenotypes >> MS >> Bioinformatics analysis

Reference proteome: Higher amount of sample (multiple single cells in one pot)

Automated sample prep and dimethyl labeling, EvoTip.

__mDIA with (sc)DVP: advancing cell type and sc resolved spatial proteomics__
- Methodology: Ammonia fixation, OXPHOS
- shows cell type signatures

</br>

__Summary__
- DVP
- Automated workflow with reference chnnel
- Precision diagnostics & sc tissue proteomics

</br>

__QA__

염색 후에 well 에다가 tissue의 cell을 채워 넣을 수 있음.

__Note__



</br>


### CS15:05: Near Single Cell Proteomics on FFPE Tissue Sections Using Hydrogel-Based Tissue Expansion and DIA Based Mass Spectrometry
_Zhen Dong, Westlake Laboratory, China_

- Several exampels of botom-up MS-based spatial proteomics workflows.
  - LCM-SISPROT, DVP, nanoPOT etc.

__Tissue expansion__

- Linear expansion factor at X4.7
- cell structure distortion error is below 5.5%
- hProteomEX workflow

</br>

__Note__

Tissue expansion method: 조직을 물에 불리듯이 크게 만들어도 조직의 구조적인 형태는 유지하더라. 이렇게 해서 크게 만들면 조직에서 세포의 분리가 비교적 쉬워짐.
이렇게 확장된 조직으로부터 세포를 분리하고 In-Tip-FASP 시행해서 peptide 97.7% 증가, protein groups 30.6% 증가.

</br>