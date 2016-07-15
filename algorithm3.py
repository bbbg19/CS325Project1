#!/usr/bin/python
import time
import random

def mss(array, low, high):
	if(low == high):
		return array[low], low, high
		
 	mid = (low+high)/2
	
	#Get lower values
	leftValue, leftX, RightX = mss(array, low, mid)
	midValue, mleftX, mRightX = getCS(array, low, mid,high)
	rightValue, rLeftX, rRightX = mss(array, mid+1,high)
	
	if max(leftValue, midValue, rightValue) == leftValue:
		return leftValue, leftX, RightX
			
	elif max(leftValue, midValue, rightValue) == midValue:
		return midValue, mleftX, mRightX
		
	else:
		return rightValue, rLeftX, rRightX
		
	#return max(	mss(array, low, mid), mss(array, mid+1,high), getCS(array, low, mid,high))

	
 
 
def getCS(array,low,mid, high):

	maxleft = -9999999
	maxright = -9999999
	maxLeftIndex =mid
	maxRightIndex =mid
	sum =0
	#get left sum
	for x in range(mid,low-1, -1):
		sum += array[x]
		if sum > maxleft:
			maxleft = sum
			maxLeftIndex =x
                      
	
	#get right sum 
	sum =0
	for x in range(mid+1,high+1):		
		sum += array[x]
		if (sum > maxright):
			maxright = sum	
			maxRightIndex = x
	return (maxleft + maxright), maxLeftIndex, maxRightIndex  

 
def generateArray(x):
	myList =[]
	for i in range(1,x):
		myList.append(random.randrange(-1000,1000))
		
	return myList
 
  	

def manualTest(myList, w):
	value, left, right  = mss(myList,0, len(myList)-1)
	outputString= '['
	for x in range(left,right+1):
		outputString +=  str(myList[x]) +','
	outputString = outputString[:-1]
	outputString += ']'
	w.write(outputString+'\n')
	w.write(str(value)+'\n')


#main function
#file = open("MSS_Problems.txt", "r")

#outputFile = open('MSS_Results.txt', "a")
#outputFile.write("Algorithm 3\n")
#outputFile.write("****************************************************************\n")
#for line in file.readlines():
#	print line
	#manualTest(line,outputFile)
	#manualTest([2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2],outputFile)
	#manualTest([10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19],outputFile)
	#manualTest([31,-41, 59, 26, -53, 58, 97, -93, -23, 84],outputFile)
	#manualTest([3, 2, 1, 1, -8, 1, 1, 2, 3],outputFile)
	#manualTest([12, 99, 99, -99, -27, 0, 0, 0, -3, 10],outputFile)
	#manualTest([-2, 1, -3, 4, -1, 2, 1, -5, 4],outputFile)
#outputFile.write("****************************************************************\n")
#experimental partition 

sizes = [11,51,101,501,1001,5001,10001,20001, 30001, 50001]

for size in sizes:
	print "Running sizes for " + str(size)
	#run ten trials in this size
	for x in range (1,11):
		To = time.time()
		myList = generateArray(size)		
		value, left, right= mss(myList,0, len(myList)-1)
		print value
		print "Trial Run " + str(x) + ". Time: " + str(time.time()-To)
	
	
