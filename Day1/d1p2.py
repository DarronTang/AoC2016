import re

inputFile = open("input.txt","r")

input = inputFile.read()

x = 0
y = 0
direction = 0
path = []
crossoverX = 0
crossoverY = 0

input = re.sub('[\s+]','',input).split(",")

for i in input:
	
	dir = i[0]
	magnitude = int(i[1:])
	if(dir == 'R'):
		direction = (direction +1) % 4
	else:
		direction = (direction -1) % 4

	for mag in range(0,magnitude):
		if direction == 0:
			y += 1
			path.append([x,y])
		elif direction == 1:
			x += 1
			path.append([x,y])
		elif direction == 2:
			y -= 1
			path.append([x,y])
		elif direction == 3:
			x -= 1
			path.append([x,y])

for p in range(0,len(path)):
	first, rest = path[p], path[p+1:]
	if first in rest:
		crossoverX = first[0]
		crossoverY = first[1]
		break

print abs(crossoverX) + abs(crossoverY)