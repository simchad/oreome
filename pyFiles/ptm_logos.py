"""
ptm_logos.py

notebook -> ptm_site_logo.ipynb
"""
__author__ = "github.com/simhc0714"
__version__ = "0.0.1"

# import packages
import pandas as pd
import numpy as np

# Generate Logos data.
def logo_align(df_site, df_sequence, d:int=7, aa='K'):
    """
    logo_align(df_site, df_sequence) -> (logos) pd.DataFrame

    Parameters
    ----------
    - df_site: Dataframe that contains UniprotAC-ID and site, must be formed (UniprotAC_Site) (pandas.DataFrame).
    - df_sequence: Dataframe that contains UniprotAC and its sequence (pandas.DataFrame).
    - d: Default is 7. Cut sequence forward and backward with 7 amino acids. 7aa-X-7aa (int).
    - aa: Default is K (Lysine). Amino acid one letter code. Capital letter.

    Notes
    -----
    Format for df_site.
    - File format: .csv
    - Header: None
    - Context: (UniprotAC-ID)_(site). The UniprotAC-ID is Uniprot Accession ID,
    and the site is the position number of modification on sequence.
    """
    # Initialize params
    aa = aa.upper()
    entries = []
    logo = []
    start = []
    end = []
    
    # 1. UniprotAC-ID_Site
    for (i, entry) in df_site.iterrows():
        entries.append(entry[0].replace('_', '_'+aa))
        ent_name, ent_site = entry[0].split('_')
        ent_site = int(ent_site)
        # 2. Match entry in reference_sequence.
        try :
            seq = df_sequence.loc[ent_name]['Sequence']
            # For ent_site on sequence residue is lysine (K) if not -> else
            if seq[ent_site-1] == aa:
                # 3. Cases.
                # 3.1. If site residue locates too close forward of sequence.
                if ent_site-d-1 < 0:
                    start.append(int(1))
                    space = ""
                    for i in range(d+1-ent_site):
                        space += " "
                    logo.append(space+seq[:ent_site+d])
                    end.append(ent_site+d)
                # 3.2. If site residue locates too close backward of sequence.
                elif ent_site+d > len(seq):
                    start.append(ent_site-d)
                    space = ""
                    for i in range(ent_site+d-len(seq)):
                        space+=" "
                    logo.append(seq[ent_site-d-1:]+space)
                    end.append(len(seq))
                # 3.3. Normal condition.
                else:
                    start.append(ent_site-d)
                    logo.append(seq[ent_site-d-1:ent_site+d])
                    end.append(ent_site+d)
            else:
                start.append("NaN")
                logo.append("")
                end.append("NaN")
        # ent_site on sequence is not lysine (K) it is other amino acid.
        except:
            start.append("NaN")
            logo.append("")
            end.append("NaN")
    # Organize DataFrame
    logos = pd.DataFrame(np.column_stack([entries, logo, start, end]), columns=['Entry', 'Logo', 'Start residue', 'End residue'])
    return logos


def multiple_logo_align():
    return None


if __name__ == "__main__":
    # Load example files.
    site = pd.read_csv(filepath_or_buffer='example\Acetyl(K)Sites.csv', encoding='utf-8')
    ref_sequence = pd.read_csv(filepath_or_buffer='example\Reference_sequence.csv', index_col=0, encoding='utf-8')

    # Run
    logos = logo_align(df_site=site, df_sequence=ref_sequence)
    logos.to_csv(path_or_buf='.\output\logos.csv', index=False, encoding='utf-8')

    # Show the first 5 rows.
    print(logos.head())