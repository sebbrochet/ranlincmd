ranlincmd
=========

Generic tool to track changes based on command output for your linux servers

Requirements:
-------------

* linux box
* Python 2.6 or higher
* Create/Commit rights to a CVS or Subversion repository
* cvs or svn binaries in the PATH

Installation:
-------------

To install, just do:

python setup.py install

Usage:
------

usage: ranlincmd [-h] [-c CONFIG] [--v] action

Generic tool to track changes based on command output for your linux servers.

positional arguments:
  action                Action to execute (GENCONFIG or RUN)

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Configuration file to use or create
  --v                   Print program version and exit.

GENCONFIG: generate default configuration file, to be customized with your environment.
RUN: execute command based on each server/IP and generates corresponding files.

Documentation:
--------------

Please visit the project page at: https://code.google.com/p/ranlincmd/
