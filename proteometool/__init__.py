# __init__.py
"""
proteometool: A protoemic tool for ToxicoProteomic LAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subpackages
-----------
- api_request
- my_lib
"""
from .api_request import requests_uniprot
from .my_lib import preprocessing

from .proteinGroups import *