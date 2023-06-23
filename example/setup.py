# setup.py

from setuptools import find_packages, setup

install_requires = [
    'pandas==1.5.3',
    'scipy==1.10.0',
    'seaborn==0.12.2'
    ]

setup(
    name='ex_setuppy',
    version='0.1.0',
    packages=find_packages(where='example', include=['tool_A', 'tool_B']),
    install_requires=install_requires
    )