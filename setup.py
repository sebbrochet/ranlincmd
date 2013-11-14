#!/usr/bin/env python

import os
import sys

from distutils.core import setup

__version__ = '0.1.0'
__author__ = '@sebbrochet'

setup(name='ranlincmd',
      version=__version__,
      description='Generic tool to track changes based on command output for your linux servers',
      long_description='This command-line tool lets you track remotely, between successive runs, changes made based on output of a command run your linux servers. You get a mail for each change detected on a specific server with detail of the changes.',
      author=__author__,
      author_email='contact@sebbrochet.com',
      url='https://code.google.com/p/ranlincmd/',
      platforms=['linux'],
      license='MIT License',
      scripts=[
         'bin/ranlincmd'
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: System :: Monitoring',
          ],
      )