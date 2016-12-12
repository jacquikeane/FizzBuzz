import os
import glob
import shutil
import sys
from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version='0.1.0',
    description='description of fizzbuzz',
    packages = find_packages(),
    author='Martin Hunt',
    author_email='path-help@sanger.ac.uk',
    url='https://github.com/martinghunt/fizzbuzz',
    scripts=glob.glob('scripts/*'),
    test_suite='nose.collector',
    tests_require=['nose >= 1.3'],
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)

