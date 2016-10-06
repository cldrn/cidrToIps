# cidrToIps
This simple script reads a list of IP ranges in CIDR notation and prints the individual IP addresses.

Posted this script because I got tired of re-writing the same script everytime I needed this. If you write security tools, please support CIDR notation and make my life easier.

Usage: ./cidrToIps.py -i <inputfile>

~~~~
$ cat cidr-list.txt
192.168.0.1/29
192.168.1.1/30
$ ./cidrToIps.py -i cidr-list.txt
Reading IP ranges in CIDR notation from file: cidr-list.txt
192.168.0.0
192.168.0.1
192.168.0.2
192.168.0.3
192.168.0.4
192.168.0.5
192.168.0.6
192.168.0.7
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3

~~~~

calderon@websec.mx


