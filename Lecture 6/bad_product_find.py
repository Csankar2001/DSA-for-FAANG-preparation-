 #Time Complexity: O(log(X)). 
#Auxiliary Space: O(1).

def binarySearch(v, bad_product):
	lo = 0
	hi = len(v) - 1

	for i in range(len(v)):
		mid = (hi + lo) // 2
		if v[mid]==bad_product:
		    if v[mid-1]==bad_product:
		        hi=mid
		    else:
		        return(mid)
		else:
		    lo=mid+1
		
                    
v=[0,0,0,1,1,1,1,1,1] 
bad_product=1
print(binarySearch(v, bad_product))



