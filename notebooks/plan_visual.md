# Visualization
> How to visualize data and analyze statistically. <br/>
> Normally in proteinGroups.txt<br/>

pip install: matplotlib, seaborn, scipy

## Visualize (Figures)
> Routinely, process with Perseus by Maxquant.<br/>
> Crucial disadvantage of perseus: NOT completely save plot images

- Identified/Quantified proteins (Bar plot)
- id/Quan proteins by cell type. (Bar plot)
- Nth-order Venn diagram
- Pearson's correlations (scatter plot)
- Volcano plot (for DEP., Differentially Expressed Proteins)
- Enrichment test processed with GO/KEGG plot (Horizontal bar plot)


## Statistically processing (by figures)
> (Crucial !!) Normalize all data<br/>

> identified, quantified proteins (bar plot)
1. pre-processing
2. determine number of id proteins and quan proteins

> Pearson's correlation (Heatmap, scatter plot)
solution: pandas, scipy

> Volcano-plot
