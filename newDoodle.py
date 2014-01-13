import glob
import datetime
header = """Title:
Author: doubletony
Date: TODAY
"""
header = header.replace("TODAY", datetime.datetime.today().strftime("%d %B %Y"))
allDoodle = glob.glob("doodle*.md")
newId =  len(allDoodle) + 1
newDoodleName = "doodle"+str(newId).zfill(4)+".md"
print newDoodleName
f = open(newDoodleName, 'w+')
f.write(header)
f.close()
