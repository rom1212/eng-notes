#!/usr/bin/env python
import sys
import json

if len(sys.argv) < 2:
    print 'Usage pprint-json.py filename'
    exit(1)

filename = sys.argv[1]
with open (filename, "r") as myfile:
    data=myfile.read()
    parsed = json.loads(data)
    print json.dumps(parsed, indent=4, sort_keys=True)
