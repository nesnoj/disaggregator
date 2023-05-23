# Manually added setup file not shipped in the original version

import os
from setuptools import find_packages, setup

setup(
    name='disaggregator',
    packages= ['disaggregator'],
    include_package_data=True,
    install_requires=['numpy',
                      'pandas<=1.5.3',
                      'tables',
                      'pyyaml',
                      'requests',
                      'geopandas',
                      'descartes',
                      'xarray',
                      'xlrd',
                      'matplotlib',
                      'holidays',
                      'openpyxl',
                      'ruamel.yaml'],
    package_data={
        "": ["*.csv", "*.xlsx"]}
)
