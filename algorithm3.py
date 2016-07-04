#!/usr/bin/python
import time
import random

def mss(array, low, high):
	if(low == high):
		return array[low]
 	mid = (low+high)/2
	#Get lower values

	return max(	mss(array, low, mid), mss(array, mid+1,high), getCS(array, low, mid,high))

	
 
 
def getCS(array,low,mid, high):

	maxleft = -9999999
	maxright = -9999999
	sum =0
	#get left sum
	for x in range(mid,low, -1):
		sum += array[x]
		if sum > maxleft:
			maxleft = sum
	
	#get right sum 
	sum =0
	for x in range(mid+1,high):		
		sum += array[x]
		if (sum > maxright):
			maxright = sum	
	return maxleft + maxright 

 
def generateArray(x):
	myList =[]
	for i in range(1,x):
		myList.append(random.randrange(-1000,1000))
		
	return myList
 
  	
#main function
sizes = [11,51,101,501,1001,5001,10001,50001]

for size in sizes:
	print "Running sizes for " + str(size)
	#run ten trials in this size
	for x in range (1,11):
		To = time.time()
		myList = generateArray(size)
		
		print mss(myList,0, len(myList)-1)
		print "Trial Run " + str(x) + ". Time: " + str(time.time()-To)
	

