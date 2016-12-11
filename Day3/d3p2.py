import numpy as np

inputFile = open("input.txt","r")
input = inputFile.read().split("\n")
input = np.loadtxt(input).T.reshape(-1,3).T

count = 0

for x in range(0,len(input[0])):
	first = input[0][x]
	second = input[1][x]
	third = input[2][x]
	if  first + second > third and first + third > second and second + third > first:
		count += 1

print count