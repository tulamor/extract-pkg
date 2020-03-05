#!/usr/bin/env python

from os import environ, popen
from argparse import ArgumentParser
import sys
import re
from glob import glob
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
parser = ArgumentParser()
parser.add_argument('-in', '--inputfile', dest = "infile", default = dir_path)
args = parser.parse_args()

def extract_data(inputfile):
  list_of_dicts = []
  dict_ = {}
  package_type = name = version = suffix = hashtag = ''



  with open(inputfile, 'r') as file:
    pattern = re.compile('^([a-z]+)\+([\w-]+)\+([\w.-]+)\s\(([\w]+)\)')
    # pattern = re.compile(r'^([a-z]+)\+([\w-]+)\+([\w.]+)-?([\w\.-]*).\(([\w]+)\)')
    matched_lines = [pattern.match(l) for l in file.readlines()]
    for line in matched_lines: 
      if line: 
        # print line.group(0,1,2,3,4,5)
        list_of_dicts.append(dict(
          package_type = line.group(1),
          name = line.group(2),
          ver_suffix = line.group(3),
          hashtag = line.group(4)
        ))
    # print list_of_dicts
    # json.dumps(list_of_dicts, sort_keys=True, indent=2)
  return json.dumps(list_of_dicts, sort_keys=True, indent=2)
    # for count, dict_ in enumerate(list_of_dicts): print count, dict_


    # for line in matched_lines:print line.group()
    # for count, l in enumerate(file.readlines()):
    #   if pattern.match(l):
    #     print count, pattern.match(l).group(0,1,2,3,4,5) #1315

print(extract_data("%s/logfile" % args.infile))

# print args.infile

with open("%s/data.json" % dir_path, 'w' ) as file:
  file.write(extract_data("%s/logfile" % args.infile))


'''
^([a-z]+)\+([\w-]+)\+([\w.]+)-?([\w-\.]*)(?!.*-([\w-\.]*)).\(([\w]+)\)
^([a-z]+)\+([\w-]+)\+([\w.-]+)\s\(([\w]+)\)

external+geneva+1.0-RC3-bcolbf4 (2b480b9f9a45841216f52eb743807d20)
cms+data-SimTransport-TotemRPProtonTransportParametrization+V00-01-00-nmpfii (ba5334461fceeca2283f4430bb296c4d)
cms+data-Validation-Geometry+V00-07-00 (bcfe191179d4d874edbe78e9a07b8dd0)
external+dd4hep+v01-10x-cms (dce0b4d36a0d9c56cea3ef3d42b464dd)
cms+distcc-gcc-toolfile+2.0-pafccj (e686501eeee3c45140f5b167f061ba88)
external+dmtcp+3.0.0-dev-pafccj (510f05f11c4b571909e2795c7222eccc) 
external+gbl+V02-01-03-bcolbf (8a3c27468b6155e7066268fb539d058a)
external+geneva+1.0-RC3-bcolbf4 (2b480b9f9a45841216f52eb743807d20)
external+glibc+2.17-78.el7_2.12-1.166.el6_7.3 (501ff0d0db57404aa94e576db5819c8a)
sam+2.0.4-33b41ed-nmpfii3 (fedce1cc95deafd8463fced96cbcaf52)
external+gosamcontrib+2.0-20150803-pafccj (471674113ed2bb9988d924b19091ed30)
external+millepede+V04-06-00 (5d6b579edc920a13e83a0c976e228131)
external+tkonlinesw+4.2.0-1_gcc7-cms (75d8cd6cef59d4d2ba834b16efcd81c2)
'''