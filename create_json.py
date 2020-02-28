#!/usr/bin/env python

from os import environ, popen
from argparse import ArgumentParser
import sys
import re
from glob import glob
import os

parser = ArgumentParser()
parser.add_argument('-in', '--inputfile', dest = "infile", default = "logfile")
args = parser.parse_args()

def extract_data(inputfile):
  with open(inputfile, 'r') as file:
    fullmatch = re.compile(r'(^[a-z]+)\+([\w-]+)\+([\w.]+)-?([\w-\.]*).\(([\w]+)\)')
    


extract_data(args.infile)
