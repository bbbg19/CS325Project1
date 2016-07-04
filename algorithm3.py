

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
		print "x:" + str(x)
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

  
  	
#main function
mylist = [31, -41, 59, 26, -53, 58, 97, -93, -23, 8]
print mss(mylist,0, len(mylist)-1)

