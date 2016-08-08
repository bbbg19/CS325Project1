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
        distance = distanceOrigin(x, y)
        points.append({'index': index , 'x': x, 'y': y, 'distance': distance})
        line = file.readline()
	return points 


def printResults (outfile, resultsData, distanceCovered):
	print "Results can be found in " + outfile
	outFile = open(outfile,'w')
	outFile.write(str(int(distanceCovered)) + '\n')
	for index, points in enumerate(resultsData):
		outFile.write(str(points) + '\n' )	
	return
	

    
#Altered to calculate the distance from the origin    
def distanceOrigin(x, y):
	calcDistance = round(math.sqrt(math.pow(x,2) + math.pow(y,2)))
	return calcDistance


    
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
    distanceCovered = 0 
    sortedPoints = sorted(inputValues, key=attrgetter('distance'))
    path.append(sortedPoints.pop()) 
    path.insert(0, sortedPoints.pop()) 
    distanceCovered += distance(path[0], path[1]) 
    path.append(sortedPoints.pop()) 
    distanceCovered += distance(path[-1], path[-2]) 
    endCheck = 0 
    
	#While there are still points in the sortedPoints array continue
    while len(sortedPoints) > 0: 
        if endCheck == 0:
            one = distance(path[0], sortedPoints[-1]) 
            two = distance(path[0], sortedPoints[-2]) 
            
            #inserts whichever point is closest and removes it from sortedPoints
            if one < two:
                path.insert(0, sortedPoints.pop())
                distanceCovered += one
            else:
                path.insert(0, sortedPoints[-2])
                del sortedPoints[-2]
                distanceCovered += two
                
        if endCheck == 1:
            one = distance(path[-1], sortedPoints[-1]) #gets the distance to the next furthest point
            two = distance(path[-1], sortedPoints[-2]) #gets the distance to the second furthest point
            
            #inserts whichever point is closest and removes it from sortedPoints
            if one < two:
                path.append(sortedPoints.pop())
                distanceCovered += one
            else:
                path.append(sortedPoints[-2])
                del sortedPoints[-2]
                distanceCovered += two
        if endCheck == 0:
            endCheck = 1
        else:
            endCheck = 0
    
    #compute the distance from the last two points added to each end
    distanceCovered += distance(path[0], path[-1])
    return distanceCovered, path 


	


	
if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])