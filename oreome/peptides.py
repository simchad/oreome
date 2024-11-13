"""
peptides.py
~~~~~~~~~~~

This module pre-process peptides.txt
"""
# Load packages
from lib.processing_base import *

if __name__ == "__main__":
    # evidence, peptides, proteingroups.txt 가 있는지 확인하고 실행할 수 있어야.
    txtpath = './raw_files/'
    job = process_base(txtpath)
    job.peptides_base()