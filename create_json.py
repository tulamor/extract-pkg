#!/usr/bin/env python

from os import environ, popen
from argparse import ArgumentParser
import sys
import re
from glob import glob
import os
import json
from os.path import dirname

def extract_data(inputfile):
  list_of_dicts = []
  with open(inputfile, 'r') as file:
    pattern = re.compile('^([a-z]+)\+([\w-]+)\+([\w.-]+)\s\(([\w]+)\)')
    matched_lines = [pattern.match(l) for l in file.readlines()]
    for line in matched_lines: 
      if line: 
        list_of_dicts.append(dict(
          package_type = line.group(1),
          name = line.group(2),
          ver_suffix = line.group(3),
          hashtag = line.group(4)
        ))
  print(json.dumps(list_of_dicts, sort_keys=True, indent=2))
  return json.dumps(list_of_dicts, sort_keys=True, indent=2)


path = dirname(dirname(realpath(__file__)))
with open("%s/data.json" % path, 'w' ) as file:
  file.write(extract_data("%s/logfile" % path))