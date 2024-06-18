"""
evidence.py
~~~~~~~~~~~

This module pre-process evidence.txt
"""
# Load packages
from lib.processing_base import process_base

if __name__ == "__main__":
    # evidence, peptides, proteingroups.txt 가 있는지 확인하고 실행할 수 있어야.
    txtpath = './raw/'
    job = process_base(txtpath)
    job.evidence_base()