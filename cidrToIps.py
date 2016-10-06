#!/usr/bin/python
#This simple script reads a list of IP ranges in CIDR notation 
# and prints the individual IP addresses. 
#
#Posted this script because I got tired of re-writing the same script
# everytime I needed this. If you write security tools, please support 
# CIDR notation.
#
#Usage: ./cidrToIps.py -i <inputfile>
#
#$ cat cidr-list.txt 
#192.168.0.1/29
#192.168.1.1/30
#$ ./cidrToIps.py -i cidr-list.txt
#Reading IP ranges in CIDR notation from file: cidr-list.txt
#192.168.0.0
#192.168.0.1
#192.168.0.2
#192.168.0.3
#192.168.0.4
#192.168.0.5
#192.168.0.6
#192.168.0.7
#192.168.1.0
#192.168.1.1
#192.168.1.2
#192.168.1.3
#
#calderon@websec.mx
#

from netaddr import IPNetwork
import sys
import getopt

def main(argv):
  inputfile = ''
  try:
    opts, args = getopt.getopt(argv,"i:",["ifile="])
  except getopt.GetoptError:
    print 'cidrToIps.py -i <inputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'cidrToIps.py -i <inputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg

  print 'Reading IP ranges in CIDR notation from file:', inputfile
  fo = open(inputfile, "r+")
  for line in fo:
    for ip in IPNetwork(line):
      print '%s' % ip

if __name__ == "__main__":
  main(sys.argv[1:])
