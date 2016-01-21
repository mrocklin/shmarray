#!/usr/bin/env python

import os
from setuptools import setup
import sys

setup(name='shmarray',
      version='0.0.1',
      description='Array dump in shared memory',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      install_requires=['numpy', 'posix_ipc'],
      packages=['shmarray'],
      long_description=(open('README.md').read() if os.path.exists('README.md')
                        else ''),
      zip_safe=False)
