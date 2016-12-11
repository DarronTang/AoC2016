import re

inputFile = open("input.txt","r")

input = inputFile.read()

x = 0
y = 0
direction = 0

input = re.sub('[\s+]','',input).split(",")

for i in input:
	dir = i[0]
	magnitude = int(i[1:])
	if(dir == 'R'):
		direction = (direction +1) % 4
	else:
		direction = (direction -1) % 4
	if direction == 0:
		y += magnitude
	elif direction == 1:
		x += magnitude
	elif direction == 2:
		y -= magnitude
	elif direction == 3:
		x -= magnitude

print abs(x) + abs(y)
