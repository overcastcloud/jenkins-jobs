#!/usr/bin/env python
import argparse
import xml.etree.ElementTree

parser = argparse.ArgumentParser()
parser.add_argument('manifest', help='Manifest file')
parser.add_argument('prefix', help='Prefix to search for')

args = parser.parse_args()

t = xml.etree.ElementTree.parse(args.manifest)

for project in t.findall('project'):
    if project.attrib.get('path', '').startswith(args.prefix):
        print '''- project:
    name: %s
    jobs:
      - "%s-{name}"
''' % (project.attrib['name'], args.prefix)
