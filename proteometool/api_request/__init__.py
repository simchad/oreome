# __init__.py
"""
api_request
~~~~~~~~~~~

.. currentmodule:: proteometool.api_request

This module contains a number of api-related jobs.
For example, DAVID, KEGG, UniProt and so on.
"""

# APIs
from ._api_uniprot import *

# User-defined
from .requests_uniprot import *