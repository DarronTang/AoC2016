import re

inputFile = open("input.txt","r")

input = inputFile.read().split("\n")

bathroomCode = []

position = 5

for line in input:

	for direction in line:
		if direction == 'U':
			if position >= 4 :
				position -= 3
		if direction == 'R':
			if position not in [3,6,9]:
				position += 1
		if direction == 'L':
			if position not in [1,4,7]:
				position -= 1
		if direction == 'D':
			if position <= 6:
				position += 3

	bathroomCode.append(position)

print bathroomCode