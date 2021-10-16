#!/usr/bin/env python

import re

pattern = 'router ospf'

f = open("switch_config.cfg", "r")

text = f.read()
result = re.search(pattern, text)
s = result.start()
e = result.end()
print(s)
print(e)
print(result)
#print(text[s:e])

f.close()
