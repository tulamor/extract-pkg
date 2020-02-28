#!/usr/bin/env python

from os import environ, popen
from argparse import ArgumentParser
import sys
import re
from glob import glob
import os
import json

dir_path = "%s/logfile" % os.path.dirname(os.path.realpath(__file__))
parser = ArgumentParser()
parser.add_argument('-in', '--inputfile', dest = "infile", default = dir_path)
args = parser.parse_args()

def extract_data(inputfile):
  list_of_dicts = []
  dict_ = {}
  package_type = name = version = suffix = hashtag = ''





  with open(inputfile, 'r') as file:
    pattern = re.compile('^([a-z]+)\+([\w-]+)\+([\w.]+)-?([\w\.-]*).\(([\w]+)\)')
    # pattern = re.compile(r'^([a-z]+)\+([\w-]+)\+([\w.]+)-?([\w\.-]*).\(([\w]+)\)')
    matched_lines = [pattern.match(l) for l in file.readlines()]
    for line in matched_lines: 
      if line: 
        # print line.group(0,1,2,3,4,5)
        list_of_dicts.append(dict(
          package_type = line.group(1),
          name = line.group(2),
          version = line.group(3),
          suffix = line.group(4),
          hashtag = line.group(5)
        ))
    # print list_of_dicts
    # json.dumps(list_of_dicts, sort_keys=True, indent=2)
  return json.dumps(list_of_dicts, sort_keys=True, indent=2)
    # for count, dict_ in enumerate(list_of_dicts): print count, dict_


    # for line in matched_lines:print line.group()
    # for count, l in enumerate(file.readlines()):
    #   if pattern.match(l):
    #     print count, pattern.match(l).group(0,1,2,3,4,5) #1315

extract_data(args.infile)
# print args.infile

with open("%s/data.json" % dir_path, 'w' ) as file:
  file.write(extract_data(args.infile))


#^([a-z]+)\+([\w-]+)\+([\w.]+)-?([\w-\.]*).\(([\w]+)\)