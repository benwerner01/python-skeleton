# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish


def question01(portfolios):
	portfolios.sort(reverse=True)
	print portfolios
	
	binaryIndexList = [] 

	x = 0
	for item in portfolios:
		binaryNumber = bin(item)[2:]
		x += 1

		binaryIndexList.append([int(binaryNumber), inverseBinary(binaryNumber)])


	if binaryIndexList[0][1] == 0:
		binaryIndexList.remove(binaryIndexList[0])

#test for perfect matches for longest lengths

	longestLengths = len(str(binaryIndexList[0][0]))

	for binaryNumber in binaryIndexList:
		if len(str(binaryIndexList))


	print binaryIndexList
	answer = 0
	return answer

def inverseBinary(num):
	result = ""
	for binaryNumber in list(num):
		if binaryNumber == "0":
			result += "1"
		elif binaryNumber == "1":
			result += "0"
	return int(result)



#test
print question01([15, 8, 6, 7])