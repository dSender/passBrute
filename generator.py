import sys


def convertToString(l):
	return ''.join(l)


def writeInFile(passList):
	with open('wordpasswords.txt', 'w+') as file:
		for i in passList:
			file.write('{}\n'.format(i))
		file.close()



def generator(alphabit):
	passList = [[]]
	for i in alphabit:
		try:
			passList = [[y] + x for y in i for x in passList]
		except MemoryError:
			pass
	passList = list(map(convertToString, passList))
	return passList


args = sys.argv
args = args[1:]
length = 0
alphabit = list()

for i in range(len(args)):
	if args[i] == '-l':
		length = int(args[i + 1])
	if args[i] == '-a':
		alphabit = args[i + 1]
		alphabit = [[k for k in alphabit]]


if len(alphabit) == 0 or length == 0:
	print("""

		/python generator.py -l 'password length' -a 'alphabit without spaces'

	""")
else:
	alphabit *= length
	passws = generator(alphabit)
	writeInFile(passws)
