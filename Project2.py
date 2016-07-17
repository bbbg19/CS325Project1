
import ast
import sys


def dynamicCoins(inputArray, inputValue):
	solutionArray = []
	
	# intialize array for storing solution
	for x in range(0 , inputValue+1):
		solutionArray.append({'minValue':10000000, 'values': [0]* len(inputArray)} )
	if inputValue == 0:
		solutionArray[0]['minValue']= 0
		print (solutionArray)
		exit
		
	solutionArray[0]['minValue']= 0
	for val in range(1, inputValue+1):
		# go through each value up to input value and find min coins for each 	
			
		index = 0
		for coin in inputArray:
		#take current value and minus coin value  		
			if val >=  coin:		
				remainder = val-coin	
				#get previous solution 
				minCoins = solutionArray[remainder]['minValue']+1
		
			#check if new solution is less than value in array 
				if minCoins < solutionArray[val]['minValue']:
					#Copy array values over 					
					for i in range(0, len(inputArray)):
						solutionArray[val]['values'][i] = solutionArray[remainder]['values'][i]
					#increase current coin denomination by 1
					solutionArray[val]['values'][index] += 1
					
					#update min number of coins
					solutionArray[val]['minValue'] = minCoins
				index += 1



	#print out array 


	#print ("Final Solution for Value: " + str(inputValue))
	return solutionArray[inputValue] 
	#print ('\n')

def greedyCoin(inputArray, inputValue):
	coins = []
	changeToMake = inputValue
	coinVals = inputArray[:]
	coinVals.reverse()
	totalCoins = 0
	for coin in coinVals:
		coinCount = 0
		while changeToMake >= coin:
			coinCount += 1
			totalCoins += 1
			changeToMake -= coin
		coins.append(coinCount)
	coins.reverse()
	return {"coins": coins, "numCoins": totalCoins}
	
	
#Main Method

inputFileName =  sys.argv[1]
print "Trying to Read File Name: " + inputFileName
	
with open(inputFileName + '.txt', 'r') as ins:
	inputArrays = []
	inputValues = []
	index = 1
	for line in ins:
		if(index %2 == 0):
			#print "Even: " + line
			inputValues.append(int(line))
			
		else:
			#print "Odd: " + line 
			inputArrays.append(ast.literal_eval(line))
		index +=1
	
outputFile = open(inputFileName + 'change.txt', 'w')

outputFile.write("Algorithm 2: Change Greedy**********************************\n")

for values in range(0,len(inputArrays)):
	result = greedyCoin(inputArrays[values],inputValues[values])
	#print result['values']
	outputFile.write(str(result["coins"]) + '\n')
	outputFile.write(str(result["numCoins"]) + '\n')

outputFile.write("Algorithm 2: Change DP**************************************\n")

for values in range(0,len(inputArrays)):
	result = dynamicCoins(inputArrays[values],inputValues[values])
	#print result['values']
	outputFile.write(str(result['values']) + '\n')
	outputFile.write(str(result['minValue']) + '\n')

	
	
#dynamicCoins(inputArray, inputValue)
