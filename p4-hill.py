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
		outFile.write(str(points['index']) + '\n' )	
	return
	
	
def distance(point1, point2):
	calcDistance = round(math.sqrt(math.pow(point2['x']-point1['x'],2) + math.pow(point2['y']-point1['y'],2)))
	# print calcDistance
	return calcDistance

def hillClimb(inputValues):
	path = []
	distanceCovered = 0
	path.append(inputValues[0])
	for i in range(1, len(inputValues)):
		path.append(inputValues[i])
		d = distance(path[i-1], path[i])
		print d
		distanceCovered += d
		
	d = distance(path[0], path[len(path)-1])
	print d
	distanceCovered += d
	
	print "start " + str(distanceCovered)
	
	for i in range(1, len(path)-1):
		for j in range(i+1, len(path)):
			if (j-i == 1):
				e1 = distance(path[i-1], path[i])
				newE1 = distance(path[i-1], path[j])
				if (j == len(path)-1):
					e2 = distance(path[j], path[0])
					newE2 = distance(path[i], path[0])
				else:
					e2 = distance(path[j], path[j+1])
					newE2 = distance(path[i], path[j+1])
				if ((newE1+newE2) < (e1+e2)):
					temp = path[i]
					path[i] = path[j]
					path[j] = temp
					distanceCovered -= (e1+e2)
					distanceCovered += (newE1 + newE2)
			else:
				e1 = distance(path[i-1], path[i])
				e2 = distance(path[i], path[i+1])
				e3 = distance(path[j-1], path[j])
				newE1 = distance(path[i-1], path[j])
				newE2 = distance(path[j],path[i+1])
				newE3 = distance(path[j-1], path[i])
				if (j == len(path)-1):
					e4 = distance(path[j], path[0])
					newE4 = distance(path[i], path[0])
				else:
					e4 = distance(path[j], path[j+1])
					newE4 = distance(path[i], path[j+1])
				if ((newE1 + newE2 + newE3 + newE4) < (e1 + e2 + e3 + e4)):
					temp = path[i]
					path[i] = path[j]
					path[j] = temp
					distanceCovered -= (e1 + e2 + e3 + e4)
					distanceCovered += (newE1 + newE2 + newE3 + newE4)
				
	return distanceCovered, path
	
def main(inputFile, outputFile):
	#Read in input Files
	input_point_labels = read_input_vals(inputFile)
	
	# print (distance(input_point_labels[1],input_point_labels[2]))
	#Final Algorithm
	start = time.time();
	distanceCovered, path = hillClimb(input_point_labels)
	print ("Time: " + str(time.time() - start))
	
	#Print out results 
	printResults(outputFile, path, distanceCovered)

	
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])

