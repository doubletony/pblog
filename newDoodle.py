import glob

allDoodle = glob.glob("doodle*.md")
newId =  len(allDoodle) + 1
newDoodleName = "doodle"+str(newId).zfill(4)+".md"
print newDoodleName
f = open(newDoodleName, 'w+')
f.close()
