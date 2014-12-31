# -*- coding: UTF-8 -*-

import setuptools
from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='flatkeys/__init__.py'
with open(VERSIONFILE, 'rt') as vf:
    verstrline = vf.read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='flatkeys',
    version=verstr,
    author='Baptiste Fontaine',
    author_email='b@ptistefontaine.fr',
    packages=['flatkeys'],
    url='https://github.com/bfontaine/flatkeys',
    license=license,
    description='flat dictionnaries',
    long_description="""\
An easy way to flatten dictionnaries""",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
