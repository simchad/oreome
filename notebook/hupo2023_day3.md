# September 19, 2023. Tuesday

## CS27: Single Cell

### CS27.01: Is it Possible to Analyze 5000 Proteins from a Single Human Cell?
_Karl Mechtler, Austria_

- cellenOne
- Loss-less and reproducible one pot sample prep. _E. Muiller et al., Alnal Chem. 2023_
- possible to increase instrument: lc-ms, data analysis method...
- 1~2 PSM in single-cell sample 50%.
- scp can goes to inside of precision medicine..!

__QA__

UCSD prof
- DDA로 찍어봤나? A. Never, 그리고 SW에 따라 다르다.


__Note__

중간 부터 들음.
사람을 믿고 팀원을 믿고 프로토콜을 믿어라. Yes 좋아함.

</br>

### CS27.02: Interfacing Optics, Microfluids, and Mass Spectrometry to Advance Single cell and Spatial Proteomics
_Ying Zhu, United States_

- The improvements of technology in proteomics. (e.g., micro-spray to nano...)
- Miniaturization is benefitable.
- FACS to CellenONE
- Mannual to Auto-prep
- DDA to DIA and also libraries and s/w


__Trnascripts and protein correlation__
- transcriptiion/translation kinetics
- RNA/protein degradation
- Co-profiling transcripts and proteins from the same single cells (NAnoSPLITS)  doi:10.1011/2022/05.17.492137

__Region-specific and cell type-specific proteomes__
- MCP, 2018, 17, 1864

__Tissue microsampling based laser dissection__
- Thermo, LCM
- Leica, LMD
- Zeiss, LCM

__Integrating DUV-LA sampling with nanoPOTs__
- DUV로 셀 표면 때리면 셀이 나노~마이크로 급의 이온화가 됨. 이거를 nanoPot 에 넣는 방식으로 spatial lc-ms

__Notes__

DUV-LA with nanoPOTs 방식으로 단일 세포에서 x,xxx개 동정.

(내 의견) 전사체-단백질 데이터 correlation 이해가 떨어지는 거는 그 사이 과정을 아직은 완벽하게 이해하지 못해서 이기때문이라고 생각함. PTM이 그 linker가 될 것임.

low correlation에 관한 발표자의 의견. 전사체는 항상 발현하는게 아니며, 단백질은 항상 있기에,,, single-cell에서는 corr가 0.2 미만 이었음.

</br>

### CS27.03: Single Cell Proteomics Study of Drugs Responses
_Bogdan Budnik, Harvard Medical School, United States_

__Patients-derived organoid model__

__CricaVent: Access Neuroinflammation__

__Note__

- 환자 유래 오가노이드를 정상과 케이스 그룹의 단일 세포에 대해서 세 종류의 약물(WD, Li, Risp)을 치고 UMAP 분석을 했음
- Biopolar Microglia (양극성 MG) 에서 cluster가 뚜렷히 구분.
- Li drug에 대해서 뉴런 반응의 분석을 비지도 분석을 수행함.
- 결론을 내면, 2D UMAP은 클러스터를 잘 구분하지 못했고 3D UMAP이 필요했음. 단, bipolar MG에 대해서는 좋은 결과.
- There is a different in the response of different brain celsl to the same type of drug
- 1,000 cells are enough for depth in proteomics.

</br>

### CS27.04: Platform for Single Cell Science (PSCS) Repository Enables No-Code Single Cell Proteomic Data Analysis and Sharing
_Alexandre Hutoon, Omics Data Sci. LAB., United State_

- Why is the threshold higher for coursework than for publication?
  - Reproducibility
    - Experimental protocols vs. data analysis procedures
  - Data & Analyses
    - Proeomexchange combines fantastic resources for data
    - But that need technical know-how, xaminig parameters is difficult.

- Proposal
  1. Promote reproducibility
    - make std analysis tools available without tehcnical things
  2. Offer flexibility
    - Enable custom piplelines by combining individual analysis steps
    - Allow custom steps
  3. Provide publication mechanismss for analysis+results
    - Tie results directly to data+analysis
    - Allow external users to examin peipeline and params.
    - Make results interactive!

- Platform for Single-Cell Science
  - Reporiducibility through accessbiilty
    - no-code pipeline designer
    - pipielines version-controlled
    - GUI-based, drag-and-drop system
  - Broad usefulness
  - Linked publication for analysis+results

Packages
__CZ CellXGene__
__Scanpy__

__QA__

UCSD prof: different workflows, how applied to all single-cell data for everyone.

A: scale is not solved yet, user scale is more difficult. 
</br>

### CS27.05: Spatial Proteomic Approaches for Tripe-Negative Breast Cancer on Sinle-Cell Resolution
_Gangsoo Jung, Bertis, Republic of Korea_



</br>