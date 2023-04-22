"""
proteinGroups.py
~~~~~~~~~~~~~~~~

This module pre-process proteinGroups.txt
"""
# Load packages
from my_lib.processing_base import process_base

if __name__ == "__main__":
    # evidence, peptides, proteingroups.txt 가 있는지 확인하고 실행할 수 있어야.
    txtpath = './raw/'
    job = process_base(txtpath)
    job.proteinGroups_base()