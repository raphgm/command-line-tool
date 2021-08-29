#!/usr/bin/python3

'''
This is Raphael Gab-Momoh's Code for Canonical Interview
Your task is to develop a python command each_line tool that takes the
architecture (amd64, arm64, mips etc.) as an argument and downloads the
compressed Contents file associated with it from a Debian mirror. The
program should parse the file and output the statistics of the top 10
packages that have the most files associated with them.
- This codes downloads architecture file, reads its contents and
returns top 10 packages in terms of associated number of files.
Contents file.

- Python3 was used in this scripting.
https://docs.python.org/3/library/io.html#io.BufferedReader
https://docs.python.org/3/library/io.html#io.BufferedIOBase

- Time spent: about 3 hours.

- Data structure used: heapq
https://docs.python.org/3.0/library/heapq.html#heapq.nlargest

Demo
./package_cli_tool.py -h
usage: package_cli_tool.py [-h] [--arch ARCH]

optional arguments:
  -h, --help   show this help message and exit
  --arch ARCH  Enter any of the architecture, such as amd64, arm64...

./package_cli_tool.py --help
usage: package_cli_tool.py [-h] [--arch ARCH]

optional arguments:
  -h, --help   show this help message and exit
  --arch ARCH  Enter any of the architecture, such as amd64, arm64...

AMD64 Demo
 ./package_cli_tool.py --arch amd64
#####################################################################
Downloading Content Index file: Contents-amd64.gz
Downloading from: http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz
--2021-08-29 15:58:31--  http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz
Resolving ftp.uk.debian.org (ftp.uk.debian.org)... 78.129.164.123, 2001:1b40:5600:ff80:f8ee::1
Connecting to ftp.uk.debian.org (ftp.uk.debian.org)|78.129.164.123|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10001297 (9.5M) [application/octet-stream]
Saving to: ‘Contents-amd64.gz.14’

Contents-amd64.gz.14              100%[==========================================================>]   9.54M  1.28MB/s    in 16s     

2021-08-29 15:58:48 (604 KB/s) - ‘Contents-amd64.gz.14’ saved [10001297/10001297]

Reading Content Index file: Contents-amd64.gz 

    PACKAGE NAMES                  NUMBER OF FILES
              piglit                51784
       esys-particle                18015
    libboost1.74-dev                14333
          acl2-books                12668
     golang-1.15-src                 9005
 liboce-modeling-dev                 7457
          zoneminder                 7002
        paraview-dev                 6178
linux-headers-5.10.0-8-amd64                 6153
linux-headers-5.10.0-8-rt-amd64                 6149
'''

import argparse
from argparse import RawTextHelpFormatter
import os
import gzip
from heapq import nlargest
import io
#from tabulate import tabulate

# Constants
DEBIAN_MIRROR_URL = "http://ftp.uk.debian.org/debian/dists/stable/main/"
NUMBER_OF_RESULTS = 10

# Dictionary for packages
package_dict = {}


# Function for downloading Debian packages 
def download_content_indice_file(file):
    wget_command = "wget {} --no-check-certificate".format(file)
    os.system(wget_command)

# Function for counting the number of files
def read_content_indice_file(file):
    gz = gzip.open(file, 'rb') # rb, packages are compiled files, in other words packages are binary files
    read_binary_file = io.BufferedReader(gz)
    for each_line in read_binary_file:
        each_line = each_line.decode("utf-8")
        each_line = each_line.rstrip()
        file_name, space, package_name = each_line.rpartition(' ')
        package_name = package_name.split(',')
        # get the package name
        for package in package_name:
            package = package.rpartition('/')[2]
            # Uniquessness in keys
            if package not in package_dict.keys():
                package_dict[package] = []
            package_dict[package].append(file_name)

    gz.close()
    for package in nlargest(NUMBER_OF_RESULTS,
                            package_dict, key=lambda e: len(package_dict[e])):
            print(
                "{: >20} {: >20}".format(package, len(package_dict[package]))
            )

# Cli Argument definition
parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument('--arch',
                    help="Enter any of the architecture, such as amd64, arm64...")
args = parser.parse_args()

if args.arch:
    content_indice_file = "Contents-{arch}.gz".format(
        arch=args.arch
    )
    content_indice_file_url = "{deb_mirror}{content_indice_file}".format(
        content_indice_file=content_indice_file,
        deb_mirror=DEBIAN_MIRROR_URL,
    )
    print("#####################################################################")
    print("Downloading Content Index file: %s" % content_indice_file)
    print("Downloading from: %s" % content_indice_file_url)
    download_content_indice_file(content_indice_file_url)
    print("Reading Content Index file: %s \n" % content_indice_file)
    print("    PACKAGE NAMES" +"                  "+ "NUMBER OF FILES")
    read_content_indice_file(content_indice_file)