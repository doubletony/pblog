import glob

allDoodle = glob.glob("doodle*.txt")
newId =  len(allDoodle) + 1
newDoodleName = "doodle"+str(newId).zfill(4)+".txt"
print newDoodleName
f = open(newDoodleName, 'w+')
f.close()
