# parsings.py
"""
parsing
~~~~~~~
- xtract_json
- xtract_fasta

Using Assets
------------
- Uniprot_mouse_20181213.fasta


See Also
--------
markdown -> xxx.md
notebook -> xxx.ipynb
"""

__author__ = "github.com/simhc0714"
__version__ = "0.1.0"


# import packages
import pandas as pd
import numpy as np
import re

# initialize
f_path = "./assets/Uniprot_mouse_20181213.fasta"


def xtract_fasta(filepath=f_path, pars_what="sequence"):
    """
    Params
    ------
    - filepath (file): default is uniprot_mouse_20181213.fasta FASTA formmatted file path
    - pars_what (str): default is sequence. accession, description, organism

    Notes
    -----
    """
    # Define the regular expression pattern
    pat = r'>(.*?) (.*?) \[(.*?)\](.*)'

    with open(filepath, 'r') as f:
        all_fasta = f.read()

        # Split entry by entry
        fasta_list = re.split(r'\n(?=>)', all_fasta)

        # Filter out empty srings
        fasta_list = list(filter(None, fasta_list))

        # Match with pattern
        match = re.match(pat, )



    return None


def xtract_json():
    return None


if __name__ == "__main__":
    print(__doc__)