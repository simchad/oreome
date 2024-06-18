"""
viz_david_dual.py
~~~~~~~~~~~~~~~~~

- This module doubly visualize DAVID result txt file


See Also
--------
markdown -> *.md
notebook -> *.ipynb
"""
__author__ = "github.com/simhc0714"
__version__ = "0.1.0"


# Load packages
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

# DAVID API
# https://david.ncifcrf.gov/content.jsp?file=DAVID_API.html
# Developer version: 240617_HFD_DAVID.ipynb


class david_tree:
    def __init__(self, type):
        self.type = type

    def show_list(self):
        if self.type =="short":
            short_list = """Annotation Categorical Terms (Short-list)
                            ├ Disease
                            │ ├ OMIM_DISEASE
                            │ └ UP_KW_DISEASE
                            ├ Funtional_Annotations
                            │ ├ UP_KW_BIOLOGICAL_PROCESS
                            │ ├ UP_KW_CELLULAR_COMPONENT
                            │ ├ UP_KW_MOLECULAR_FUNCTION
                            │ ├ UP_KW_PTM
                            │ └ UP_SEQ_FEATURE
                            ├ Gene_Ontology
                            │ ├ GOTERM_BP_DIRECT
                            │ ├ GOTERM_CC_DIRECT
                            │ └ GOTERM_MF_DIRECT
                            ├ Interactions
                            │ └ UP_KW_LIGAND
                            ├ Pathways
                            │ ├ BBID
                            │ ├ BIOCARTA
                            │ └ KEGG_PATHWAY
                            └ Protein_Domains
                              ├ INTERPRO
                              ├ PIR_SUPERFAMILY
                              ├ SMART
                              └ UP_KW_DOMAIN"""
            print(short_list)
        
        elif self.type == "long":
            long_list = """Annotation Categorical Terms (Long-list)"""

        else:
            raise ValueError
        
        return None


# Preprocessing DAVID txt result
class preprocessing_david:
    # Set: GeneRatio, BgRatio
    # Set: Fold Enrichment
    # Set: Tests (Benjamini, p-value, FDR, bonferroni, fisher)

    def __init__(self, df):
        self.df = df



class david_plot_scatter:
    def __init__(self, df1, df2, x, term, p, dot_feature, sort_feature):
        self.df1 = df1
        self.df2 = df2
        self.x = x
        self.term = term
        self.p = p
        self.dot_feature = dot_feature
        self.sort_feature = sort_feature


    def plot_scatter(self):


        return
    

    def plot_dualscatter(self):
        self.df1


def preprocess_david(data):
    # GeneRatio = Count / List Total
    data['GeneRatio'] = data['Count']/data['List Total']

    # BgRatio = Pop Hits / Pop Total
    data['BgRatio'] = data['Pop Hits'] / data['Pop Total']

    # Logarithmic Fisher Exact (-log10)
    data.loc[:, '-log10(Fisher Exact)'] = np.log10(data.loc[:, 'Fisher Exact'])
    data['-log10(Fisher Exact)'] *= -1

    # Logarthmic Fold Enrichment (log2)
    data.loc[:, 'Fold Enrichment'] = np.log2(data.loc[:, 'Fold Enrichment'])
    
    return data


def pick_go_term_up(data, type="bp", p="fisher", top=10):   
    # Terms
    if type == "bp":
        data_tmp = data[data['Category'] == "GOTERM_BP_DIRECT"]
    elif type == "cc":
        data_tmp = data[data['Category'] == "GOTERM_CC_DIRECT"]
    elif type == "mf":
        data_tmp = data[data['Category'] == "GOTERM_MF_DIRECT"]
    elif type == "kegg":
        data_tmp = data[data['Category'] == "KEGG_PATHWAY"]
    else:
        raise ValueError

    # Fold-enrichment into log2 scale
    # data_tmp['Fold Enrichment'] = np.log2(data_tmp['Fold Enrichment'])
    data_tmp.loc[:,'Fold Enrichment'] = np.log2(data_tmp.loc[:, 'Fold Enrichment'])

    # p
    data_p = data_tmp[data_tmp['FDR'] <= 0.01]
    data_sort = data_p.sort_values(by="Fold Enrichment", ascending=False)
    data = data_sort[:top]
    return data


def pick_go_term_down(data, type="bp", p="fisher", top=10):   
    # Terms
    if type == "bp":
        data_tmp = data[data['Category'] == "GOTERM_BP_DIRECT"]
    elif type == "cc":
        data_tmp = data[data['Category'] == "GOTERM_CC_DIRECT"]
    elif type == "mf":
        data_tmp = data[data['Category'] == "GOTERM_MF_DIRECT"]
    elif type == "kegg":
        data_tmp = data[data['Category'] == "KEGG_PATHWAY"]
    else:
        raise ValueError

    # Fold-enrichment into log2 scale
    # data_tmp['Fold Enrichment'] = np.log2(data_tmp['Fold Enrichment'])
    data_tmp.loc[:,'Fold Enrichment'] = np.log2(data_tmp.loc[:, 'Fold Enrichment'])

    # p
    data_p = data_tmp[data_tmp['FDR'] <= 0.01]
    data_sort = data_p.sort_values(by="Fold Enrichment", ascending=False)
    data_sort['Fold Enrichment'] *= -1
    data_sort['Term'] = ' '+ data_sort['Term']
    data = data_sort[:top]
    return data


def david_plot(data):
    # GeneOntology Dot Plot Generator
    font = {'family':'Arial',
            'weight':'normal',
            'size':6}
    font_ticks = {'family':'Arial',
                'weight':'normal',
                'size':6}
    spectrum_colors = sns.color_palette("coolwarm_r", as_cmap=True)


    fig = plt.figure(figsize=(1, 4), dpi=150, facecolor="none")
    scatterplot = sns.scatterplot(data=df_plot, x="Fold Enrichment", y="Term", size="Count", hue="FDR", palette='coolwarm_r', legend="brief")

    # Custom legends
    h, l = scatterplot.get_legend_handles_labels()
    plt.legend(h[6:], l[6:], bbox_to_anchor=(1.0, 0.5), loc="upper left", title="Counts", frameon=False, borderaxespad=0., fontsize=6, title_fontsize=6)


    # ColorBar
    cmap = cm.bwr
    vmin = df_plot['FDR'].min()
    vmax = df_plot['FDR'].max()
    vmm = vmin + vmax
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    cbar = fig.colorbar(sm, ax=plt.gca(), fraction=0.04, pad=0.1, anchor=(1.0, 0.9), format='%.0e')
    cbar.ax.spines['outline'].set_visible(False) # outline remove
    cbar.ax.tick_params(size=0, labelsize=6) # remove ticks
    cbar.set_label('FDR', rotation=270, size=6)


    # Details
    plt.title('KEGG', font='Arial', size=8)
    plt.xlabel("log2 Fold Enrichment", fontdict=font)
    plt.ylabel(None)
    plt.xticks(fontproperties=font_ticks)
    plt.yticks(fontproperties=font_ticks)

    # Add grid lines to both x and y axes with gray color and a lower z-order
    plt.grid(True, color='gray', linewidth=0.2, zorder=0)

    plt.show()


if __name__ == "__main__":
    # Load the example file
    USER = os.getlogin()
    CWD = os.getcwd()
    DPATH = "example"

    df_up = pd.read_csv(filepath_or_buffer=DPATH+"/*.CSV", encoding='utf-8')
    df_down = pd.read_csv(filepath_or_buffer=DPATH+"/*.CSV", encoding='utf-8')

    # Run and store
    df_up_ready = preprocess_david(df_up)
    df_down_ready = preprocess_david(df_down)

    df_bc_up = pick_go_term_up(df_up_ready, type="kegg")
    df_bc_down = pick_go_term_down(df_down_ready, type="kegg")

    df_plot = pd.concat([df_bc_up, df_bc_down])

    # Visualize