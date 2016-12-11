import re

inputFile = open("input.txt","r")

input = inputFile.read().strip().split('\n')

for i in range(0,len(input)):
	input[i] = input[i].split()

count = 0

for line in input:
	first = int(line[0])
	second = int(line[1])
	third = int(line[2])
	if  first + second > third and first + third > second and second + third > first:
		count += 1

print count