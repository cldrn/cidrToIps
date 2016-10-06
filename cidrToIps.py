#!/usr/bin/python
#This simple script reads a list of IP ranges in CIDR notation 
# and prints the individual IP addresses. 
#
#Posted this script because I got tired of re-writing the same script
# everytime I needed this. If you write security tools, please support 
# CIDR notation.
#
#Usage: cidrToIps.py -i <inputfile>
#

from netaddr import IPNetwork
import sys
import getopt

def main(argv):
  inputfile = ''
  try:
    opts, args = getopt.getopt(argv,"i:",["ifile="])
    print opts, args
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
