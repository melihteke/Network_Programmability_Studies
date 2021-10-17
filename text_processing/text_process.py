#!/usr/bin/env python

import re

pattern = 'router ospf.*ip http server'

f = open("switch_config.cfg", "r")

text = f.read()
result = re.search(pattern, text, re.DOTALL)
s = result.start()
e = result.end()
#print(s)
#print(e)
#print(result)
print(text[s:e])


print(text[s:e]) - 14     # removed "ip forward-protocol nd" command by deleting 14 characters

f.close()
