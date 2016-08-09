#!/usr/bin/python

import math, re, sys
import time

#Read in input files and return array 
def read_input_vals(in_file):
	points = []
	file = open(in_file,'r')
	line = file.readline()
	while len(line) > 1:
		line_parse = re.findall(r'[^,;\s]+', line)
		index = int(line_parse[0])
		x = int(line_parse[1])
		y = int(line_parse[2])
		points.append({'index': index , 'x': x,  'y': y})
		line = file.readline()
	return points 


def printResults (outfile, resultsData, distanceCovered):
	print "Results can be found in " + outfile
	outFile = open(outfile,'w')
	outFile.write(str(int(distanceCovered)) + '\n')
	for index, points in enumerate(resultsData):
		outFile.write(str(points) + '\n' )	
	return
	
	
def distance(point1, point2):
	calcDistance = round(math.sqrt(math.pow(point2['x']-point1['x'],2) + math.pow(point2['y']-point1['y'],2)))
	return calcDistance
	
	
def main(inputFile, outputFile):
	#Read in input Files
	input_point_labels = read_input_vals(inputFile)
	
	print (distance(input_point_labels[1],input_point_labels[2]))
	
	
	#Final Algorithm
	distanceCovered, path = optimizetsp(input_point_labels)
	
	#Print out results 
	printResults(outputFile, path, distanceCovered)

def optimizetsp(input_point_labels):
	#Final Algorithm
	myTime = 0
	startPosition = 0
	minimalDistance = 1000000000000
	optimalPath =[]
	originalInputs = input_point_labels[:]
	start = time.time();
	while myTime < 175 and startPosition < len(originalInputs)-1: 
		input_point_labels = originalInputs [:]		
		
		distanceCovered, path = tspRun(input_point_labels, startPosition,start)
		#check if new distance is less than optimal 
		if distanceCovered <minimalDistance:
			minimalDistance = distanceCovered
			optimalPath = path 	
		myTime = time.time() - start
		startPosition += 1
		print "Time " + str(myTime)
	
	return 	minimalDistance, optimalPath
	
def tspRun(inputValues,startPosition, startTime):
	path =[]
	startingPoint = inputValues[startPosition]
	originalPoint= inputValues[startPosition]
	nextPoint = inputValues[startPosition]
	path.append(startPosition)
	del inputValues[startPosition]
	originalIndex=0
	shortestPath = 10000000000000
	distanceCovered=0
	deleteIndex=0
	#for lenght of array calculate shortest point and store 
	while len(inputValues) > 0: 
		deleteIndex=0	
		shortestPath = 10000000000000
		#add abort condition for time out
		myTime = time.time() - startTime
		if myTime>175:
			distanceCovered =100000000000000
			return distanceCovered, path 
		
		for index, point in enumerate(inputValues):			
			newPath = distance(originalPoint,   point)
			if newPath <shortestPath:
				shortestPath = newPath
				nextPoint = point 	
				deleteIndex= index
				originalIndex = point['index']
			#calculate shortest distance between paths
			#record index of smallest path		
		del inputValues [deleteIndex]
		originalPoint=nextPoint
		
		#store
	
		path.append(originalIndex)
		distanceCovered+= shortestPath
	#add return trip 
	
	distanceCovered += distance(startingPoint, originalPoint)
	return distanceCovered, path 


	


	
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])

