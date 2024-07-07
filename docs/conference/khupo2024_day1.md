# KHUPO 2024 - Day 1

## CW-1 (Thermo Fisher Scientific)

### Alexander Makarov - known for orbitrap development team leader
> How Astral make analysis

- Mulitple oscillations

- Quantitation at low-picogram protein loads
  
    i.e. ASMS 24 - single cell proteomics inter experimental research
- Long term mass stability.
  - 90 SPD 
  - stability garantee over 170+ days
- Multi passes operation (Ongoing research): multiplexing ion detection

> His comment: 
> 
> - HP is really nice. Around 2,000$,
> - Preparation is key. nano-scale prep.
> - QE HF-X as good as 480.
> - In single cell proteomics, preparation is crucial key. MS-step is not important as prep.


### Kim Hyunho - Stellar MS
> How can you bridge the gap between discovery and the clinic

- Introduction for Stella MS which specifically focused on targeted proteomics.

### Yue Xuan - Senior Manger, Precision Medicine
> Streamline the biomarkers tranformation from discovery to validation at unprecedented scale

- How we can combined those technology together in biomarker phases?
- High accuracy & precision with CV < 20% and LFQ
- Skyline conductor tool is nice.


## Opening Cermony


## PL1
### John R. Yates III - Known for development of SEQUEST algorithm

> How a Single Mutation in CFTR Cause the Cystic Fibrosis
> : Interactions, PTMs, And Structure


#### Interactions
- Cystic Fibrosis is a protein misfolding disease, cause by mutation of CFTR,
an anion channel regulating chlroide homeostasis.
- There are 6 types of different wt-CFTR, half of them doen't have function or not discovered.
- Using MS to understand misfolding disease such as Cystic Fibrosis
  - Assess PPI & PTMs
- Are differential interactions responsible ofr F508 mis-folding?
- The CoPIT workflow: experimental, anlytical and statistical frame work for Co-IP/MS analysis.
- Shotgun Proteomics: uLC -MS - MS/MS - ProLuCID (GPU) - Datasheet
- Reveals new pathways and interactor affected by the F508 CFTR mutation.
  - disease specific clustered. i.e. EF quality control, degradation, tarffiking...
- Comparative systems-analysis of TS and HDACi datasets reveals key interactors
- Assessment of therapeutic potential of novel F508 interactors.
- Rescue of F508 CFTR channel activity by knockdown of 8 novel interactors
  - Specific representative traces and quantification

#### PTMs
- Extensive PTMs modification of CFTR in disordred regions (Pankwo et al., Science Signaling)
- wt-RI phosphorylation is mediated by CK2a in vivo.
  - Normalized to non-modified CFTR spike-in peptide.
- Phosphorylation of the RI element is an indicator of CFTR traffing success
- A quantitative and qualitative PTM Code for CFTR Maturation
- Molecular mechanisms of PTM code redognition?
  - HSP90 can bind RI element near position 421 in vitro (Coppinger et al., 2012)


#### Structure
> What the protein look like in vivo not in vitro.

- Protein foot printing methods on a protein to the 3d proteome: chance, gross, jones, englander, griffin...
- PNAS: Whole proteome footprinting (PNASm 119(3), e2114858118)
- How protein look like inside the cell, inside the proteome...: Covalent Protein Painting
- JPR: 2022, 2021 (JPR. 2021, 20, 5, 2762-2771)
- CryoEM reveals, solvent accesible surfaces


#### Current therapeutics
- Trikafta is working, but has severe side effects
- Trikafta is PROTAC


## SYM A1 - New Technologies in Proteomics I

### Yue Xuan - Rethink Waht is Possible: Astral MS

- Worldwide 11 LAbs & 9 Countries/Regions (in Gallery)

### Tae Hyun Yoon - Hanyang Univ.
> Mass cytometry, or cytometry by time-of-flight (CyTOF);
>
> Its principle, applications, and prospects in single cell proteomics

#### Principle

- Mass Cytometry: Mass Spectrometry + Flow Cytometry
- CyTOF; Ctyo: Cell, Metry: Measurement
- 2^10 dimensions: (# of markers) X (# of cells) X (# of Samples)
- How overcoming the curse of dimesionality?
  - Nat Immunol 17, 890-895, 2015. Mass cytometry: Blessed of dimensionality.
- Continuosly growth of mass-cytometry clinical trials research.

#### Applications

- Cell type classfication (i.e., CD4/8 naive/memory T-cells)
- External Stimuli: nanoparicle (size, shape, surface coatings/charge)
  -  Metal tagged CyTOF: Ha et al., 2020. Environ. Sci. Nano
  -  Bacterial, infectious disease (Sepsis): comparison of maually gated cell proportion and phenotype in leukocytes between health donors and sepsis patient. (Park S. et al., 2024. ACS infection Disease.) Population differences of healthy donors and sepsis patinet on PhenoGraph clusters. In-depth profiling of B cell. Manually gated cel ltypes overlaid on UMAP visualization (Bae J. et al. 2022, Frontiers in Immmunology)
  -  MALD: Phenohrap clusters and manually gated cell types ... UMAP


> Comments "Hoon Kim" in last semester lecture: DEG... 일단, clustering 부터 해보세요.

#### Future Prospect
- Imaging Mass Cytometry
  - Imaging is possible. tissues or cells cutting with laser, then imaging. 
  
> Comments "Me" : Not only single-cell, homogeneous group also reasonably clustered themselves.


### Junho Park - School of Medicine, CHA Univ.
> Establishment of a universal label-free proteomic method for spatial proteomics.


- Proteomics of limited protein input (i.e., region of interest (ROI) )
- Two major dissection: Micro (LCM, as small as single-cell resolution) and Macro (Manually, group of cell)
- Directions: High-res spatial -> Local cell-cell interaction -> TME -> SCP
- TMTpro32, CellenONE, NanoPOTs, Liquid Hander are higly cost to applicable for lab-size. Those are challenge.

> Comments "Me": How democritize cost-drive proteomics?

#### How drive cost-effective proteomics?
1. Upgrade of LC-MS data acquisition
  - DDA to DIA, DIA to BoxCar-DIA
  - BoxCar-DIA to acheive an improved dynamic range of MS1 and precursor fragmentation.
  - New BoxCar-DIA: Single-shot, library-free... and low peptide input. Wider dynamic range than conventional BoxCar-DIA
- LC column systems
  - One column systems more good than double-column ones.
  - sesitivity, peptode loss, and also gradients times
  - one column system a little bit reduced the number of proteins that identified, but this system specifications is higher SPD than conventional ones.

2. Universal sample reparation method for low protein input
   - More Minimizer, More Sensitivier

#### Application
1. Spatially-isolated 1,000 cells
   - Nearly 7,000+ proteins in total, across three cell-lines.
   - Pefectly clustered three breast cancer cell lines.
2. Spatially-isolated FFPE tissue section
   - 1mm x 1mm ROI was dissected then MS analyzed.