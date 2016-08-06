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
	start = time.time();
	distanceCovered, path = tspRun(input_point_labels)
	print ("Time: " + str(time.time() - start))
	
	#Print out results 
	printResults(outputFile, path, distanceCovered)
	
	
def tspRun(inputValues):
	path =[]
	startingPoint = inputValues[1]
	originalPoint= inputValues[1]
	nextPoint = inputValues[1]
	path.append(1)
	del inputValues[1]
	originalIndex=0
	shortestPath = 10000000000000
	distanceCovered=0
	deleteIndex=0
	#for lenght of array calculate shortest point and store 
	while len(inputValues) > 0: 
		deleteIndex=0	
		shortestPath = 10000000000000
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

