#!/usr/bin/env python
import glob
import datetime
allDoodle = glob.glob("doodle*.md")
allHTML = glob.glob("doodle*.html")

ret = ""
for i in range(1, len(allDoodle)+1):
    HTMLName = "doodle"+str(i).zfill(4)+".html"
    if HTMLName not in allHTML:
        ret += "doodle"+str(i).zfill(4)+".md\n"

if ret == "":
    print "No working item."
else:
    print ret