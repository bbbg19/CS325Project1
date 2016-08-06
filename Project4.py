#!/usr/bin/python

import math, re, sys


#Read in input files and return array 
def read_input_vals(in_file):
	points = []
	file = open(in_file,'r')
	line = file.readline()
	while len(line) > 1:
		line_parse = re.findall(r'[^,;\s]+', line)
		x = int(line_parse[1])
		y = int(line_parse[2])
		points.append({'x': x,  'y': y})
		line = file.readline()
	
		

	return points 


def printResults (outfile, resultsData, distanceCovered):
	print "Results"
	outFile = open(outfile,'w')
	outFile.write(str(distanceCovered) + '\n')
	for index, points in enumerate(resultsData):
		outFile.write(str(index) + " " + str(points['x']) + " " + str(points['y']) + '\n' )	
	return
	
	
def distance(point1, point2):
	calcDistance = math.sqrt(math.pow(point2['x']-point1['x'],2) + math.pow(point2['y']-point1['y'],2))
	
	return calcDistance
	
	
def main(inputFile, outputFile):
	#Read in input Files
	input_point_labels = read_input_vals(inputFile)
	#Final Algorithm

	
	distanceCovered, path = tspRun(input_point_labels)
	#Print out results 
	printResults(outputFile, path, distanceCovered)
	
	
def tspRun(inputValues):
	path =[]
	originalPoint= inputValues[0]
	nextPoint = inputValues[0]
	path.append(originalPoint)
	del inputValues[0]
	shortestPath = 10000000000000
	distanceCovered=0
	deleteIndex=0
	print "Starting Point: " + str(originalPoint)
	#for lenght of array calculate shortest point and store 
	#print "Input Values: " + len(inputValues)
	while len(inputValues) > 0: 
		deleteIndex=0	
		shortestPath = 10000000000000
		for index, point in enumerate(inputValues):			
			x1= point['x']
			y1= point['y']
			newPath = distance(originalPoint,   point)
			if newPath <shortestPath:
				shortestPath = newPath
				nextPoint = point 	
				deleteIndex= index
			#print "Delete Index: " + str(deleteIndex)
			#calculate shortest distance between paths
			#record index of smallest path		
		del inputValues [deleteIndex]
		originalPoint=nextPoint
		path.append(nextPoint)
		distanceCovered+= shortestPath
		#print "Next Point: " + str(nextPoint)
	#print out results
	
	print path
	print "Total Distance: " + str(distanceCovered)
	print len(path)
	
	return distanceCovered, path 
	
	
	
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
	#main("tsp_example_1.txt", "outputfile.txt")
