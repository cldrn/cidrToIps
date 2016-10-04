#!/usr/bin/python

from netaddr import IPNetwork
import sys
import getopt

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print 'cidrToIps.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  print opts
  print args
  for opt, arg in opts:
    print opt
    print arg
    if opt == '-h':
      print 'cidrToIps.py -i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg

  print 'Reading CIDR list from file:', inputfile
  fo = open(inputfile, "r+")
  for line in fo:
    for ip in IPNetwork(line):
      print '%s' % ip

if __name__ == "__main__":
  main(sys.argv[1:])
