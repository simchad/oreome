# setup.py
"""proteome-tool: Proteomics tool for ToxicoProtoemics LAB member.

Hello World!
"""
from setuptools import find_packages, setup

setup_requires = [
    ]

install_requires = [
    'pandas>=1.5.3',
    'requests>=2.28.2',
    'scipy>=1.10.0',
    'seaborn>=0.12.2',
    ]

setup(
   name='proteometool',
   version='0.1.0',
   author='Hyunchae Sim',
   author_email='simhc0714@gmail.com',
   packages=find_packages(where='proteome-tool', include=['api_request', 'lib']),
   install_requires=install_requires,
   setup_requires=setup_requires,
   )

# Package 설정
# https://velog.io/@rhee519/python-project-packaging-setuptools#getting-started
# https://data-newbie.tistory.com/770
# http://www.flowdas.com/blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-setuptools/
#
# pip install -e .
#
# Obtaining file:
#   Installing build dependencies ... done
#   Checking if build backend supports build_editable ... done
#   Getting requirements to build editable ... done
#   Preparing editable metadata (pyproject.toml) ... done
# Building wheels for collected packages: proteometool
#   Building editable for proteometool (pyproject.toml) ... done
#   Created wheel for proteometool: filename=proteometool-0.1.0-0.editable-py3-none-any.whl 
#   Stored in directory: C:\Users\
# Successfully built proteometool
# Installing collected packages: proteometool
# Successfully installed proteometool-0.1.0