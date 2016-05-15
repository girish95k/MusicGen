import os, string

args = ""
flag = True

with open('WhatHappened.txt', 'w+') as WH:
	WH.write("hello" + "\n")

with open('parameters.txt', 'r+') as file:
	for line in file:
		if flag:
			line = line.split(":")
			print line[1]
			if line[0] == "tempo":
				args += " -q " + line[1].translate(string.maketrans("\r\n", "  "))
			elif line[0] == "raaga":
				args += " -r " + line[1].translate(string.maketrans("\r\n", "  "))
			elif line[0] == "numNotes":
				args += " -n " + line[1].translate(string.maketrans("\r\n", "  "))
			elif line[0] == "octave":
				args += " -t " + line[1].translate(string.maketrans("\r\n", "  "))
			elif line[0] == "learnfile":
				with open('musicData.txt', 'w+') as mD:
					print "This gets called"
					mD.write(line[1])
				args += " musicData.txt"
				flag = False
		else:
			with open('musicData.txt', 'a+') as mD:
				# print "This gets called after flag"
				mD.write(line)

print "Args:"
print args



os.system("python main.py" + args)

