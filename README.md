

### python command each_line tool

**Instructions**
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
```
./package_cli_tool.py -h
usage: package_cli_tool.py [-h] [--arch ARCH]

optional arguments:
  -h, --help   show this help message and exit
  --arch ARCH  Enter any of the architecture, such as amd64, arm64...
```
```
./package_cli_tool.py --help
usage: package_cli_tool.py [-h] [--arch ARCH]

optional arguments:
  -h, --help   show this help message and exit
  --arch ARCH  Enter any of the architecture, such as amd64, arm64...
```

## AMD64 Demo
```
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
```
'''
