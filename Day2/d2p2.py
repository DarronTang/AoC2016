import re

inputFile = open("input.txt","r")

input = inputFile.read().split("\n")

bathroomCode = []

position = 5

for line in input:

	for direction in line:

		if direction == 'U':
			if position not in [1,2,4,5,9] :
				if position in [3,13]:
					position -= 2
				else:
					position -= 4

		if direction == 'R':
			if position not in [1,4,9,12,13]:
				position += 1

		if direction == 'L':
			if position not in [1,2,5,10,13]:
				position -= 1

		if direction == 'D':
			if position not in [5,9,10,12,13]:
				if position in [1,11]:
					position += 2
				else:
					position += 4

	if position == 10:
		bathroomCode.append('A')
	elif position == 11:
		bathroomCode.append('B')
	elif position == 12:
		bathroomCode.append('C')
	elif position == 13:
		bathroomCode.append('D')
	else:
		bathroomCode.append(position)

print bathroomCode