"""
viz_david.py
~~~~~~~~~~~~

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

# DAVID API: https://david.ncifcrf.gov/content.jsp?file=DAVID_API.html
# DAVID Documentation (Annotation part): https://david.ncifcrf.gov/content.jsp?file=functional_annotation.html
# Developer version: 240617_HFD_DAVID.ipynb


class DavidInfo:
    """
    DavidInfo
    ---------
    A class including fundamental info of DAVID system
    """
    def __init__(self, term:str='go', term_ls='short'):
        """
        Params.
        -------
        term(str) : 'dss', 'go', 'pth'. default: 'go'

        term_ls(str) : 'short', 'long'. default: 'short'
            Show short/long trees of DAVID annotation terms
            Short list is red-colored annotation terms,
            long list is every available annotation terms
        """
        self.term = term
        self.term_ls = term_ls
        self.seps = {'go':'~', 'kegg':':', 'interpro':':'}
        

    def show_list(self):
        if self.type =='short':
            short_list = """Annotation Categorical Terms (Short-list)
            ├ Disease
            │   ├ OMIM_DISEASE
            │   └ UP_KW_DISEASE
            ├ Funtional_Annotations
            │   ├ UP_KW_BIOLOGICAL_PROCESS
            │   ├ UP_KW_CELLULAR_COMPONENT
            │   ├ UP_KW_MOLECULAR_FUNCTION
            │   ├ UP_KW_PTM
            │   └ UP_SEQ_FEATURE
            ├ Gene_Ontology
            │   ├ GOTERM_BP_DIRECT
            │   ├ GOTERM_CC_DIRECT
            │   └ GOTERM_MF_DIRECT
            ├ Interactions
            │   └ UP_KW_LIGAND
            ├ Pathways
            │   ├ BBID
            │   ├ BIOCARTA
            │   └ KEGG_PATHWAY
            └ Protein_Domains
                ├ INTERPRO
                ├ PIR_SUPERFAMILY
                ├ SMART
                └ UP_KW_DOMAIN"""
            print(short_list)
        elif self.type == 'long':
            long_list = """Annotation Categorical Terms (Long-list)
            ├ Disease
            │   ├ OMIM_DISEASE
            │   └ UP_KW_DISEASE
            ├ Funtional_Annotations
            │   ├ UP_KW_BIOLOGICAL_PROCESS
            │   ├ UP_KW_CELLULAR_COMPONENT
            │   ├ UP_KW_MOLECULAR_FUNCTION
            │   ├ UP_KW_PTM
            │   └ UP_SEQ_FEATURE
            ├ Gene_Ontology
            │   ├ GOTERM_BP_DIRECT
            │   ├ GOTERM_CC_DIRECT
            │   └ GOTERM_MF_DIRECT
            ├ Interactions
            │   └ UP_KW_LIGAND
            ├ Pathways
            │   ├ BBID
            │   ├ BIOCARTA
            │   └ KEGG_PATHWAY
            └ Protein_Domains
                ├ INTERPRO
                ├ PIR_SUPERFAMILY
                ├ SMART
                └ UP_KW_DOMAIN"""
            print(long_list)
        else:
            raise ValueError
        return None


    def call_term_delim(self):
        """
        call_term_delim
        ---------------
        call delimiter chracter of term; i.e., ``go`` calls `~`, ``kegg`` calls `:`
        """
        return self.seps[self.term]


# Preprocessing DAVID txt result
class Preprocessing:
    """
    Preprocessing
    -------------
    ### Preprocessing what?
    - Count=List Hits (LH), List Total (LT), Pop Hits (PH), Pop Total (PT)
    - GeneRatio (LH/LT), BgRatio (PH/PT)
    - Fold Enrichment (=GeneRatio/BgRatio)
    - Tests (Benjamini, PValue, FDR, bonferroni, fisher)
    - PValue: modified Fisher Exact p-value.
    """
    
    def __init__(self, df):
        self.df = df

    
    def base(self):
        """
        base()
        ------
        ### Generate features
        - GeneRatio, BgRatio, -log10(P), log2(FE)

        ### Separate Terms into Identifier&Term
        """
        # GeneRatio = Count / List Total
        # data['GeneRatio'] = data['Count']/data['List Total']
        self.df.loc[:, 'GeneRatio'] = self.df.loc[:, 'Count'] / self.df.loc[:, 'List Total']

        # BgRatio = Pop Hits / Pop Total
        # data['BgRatio'] = data['Pop Hits'] / data['Pop Total']
        self.loc[:, 'BgRatio'] = self.df.loc[:, 'Pop Hits'] / self.df.loc[:, 'Pop Total']

        # P-value (modified Fisher Exact p-value)
        self.df.loc[:,'-log10(P)'] = np.log10(self.df.loc[:, 'PValue'])
        self.df['-log10(P)'] *= -1

        # Logarthmic Fold Enrichment (log2)
        self.df.loc[:, 'Fold Enrichment'] = np.log2(self.df.loc[:, 'Fold Enrichment'])
        
        # Logarithmic Fisher Exact (-log10)
        if 'Fisher Exact' in self.df.columns:
            self.df.loc[:, '-log10(Fisher Exact)'] = np.log10(self.df.loc[:, 'Fisher Exact'])
            self.df['-log10(Fisher Exact)'] *= -1
        else:
            pass
        return None
    

    def terms_in(self):
        """
        terms_in
        --------
        Find which TERMS in your data.
        
        - Future -> DAVID_API
        """


    def pick_goterm_up(self, type, p, top:int=10):
        """
        pick_goterm_up(self, type, p, top:int=10) -> self
        -----------------------------------
        ### Generate features
        """
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

        # p
        data_p = data_tmp[data_tmp['FDR'] <= 0.01]
        data_sort = data_p.sort_values(by="Fold Enrichment", ascending=False)
        data = data_sort[:top]
        return None
    

    def pick_goterm_down(self, type, p, top:int=10):
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

        # p
        data_p = data_tmp[data_tmp['FDR'] <= 0.01]
        data_sort = data_p.sort_values(by="Fold Enrichment", ascending=False)
        data_sort['Fold Enrichment'] *= -1
        data_sort['Term'] = ' '+ data_sort['Term']
        data = data_sort[:top]
        return data



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
    DPATH = "../../example/maxquant_opendata/mq_open-david.txt"

    df_ex = pd.read_csv(filepath_or_buffer=DPATH, sep='\t', encoding='utf-8')
    df_up = pd.read_csv(filepath_or_buffer=DPATH+"/*.CSV", encoding='utf-8')
    df_down = pd.read_csv(filepath_or_buffer=DPATH+"/*.CSV", encoding='utf-8')

    # Run and store
    prep = Preprocessing(df_ex)

    df_ready = prep.base()
    df_up_ready = preprocess_david(df_up)
    df_down_ready = preprocess_david(df_down)

    df_bc_up = pick_go_term_up(df_up_ready, type="kegg")
    df_bc_down = pick_go_term_down(df_down_ready, type="kegg")

    df_plot = pd.concat([df_bc_up, df_bc_down])

    # Visualize