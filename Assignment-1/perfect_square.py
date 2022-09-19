#Time Complexity: O(log(X)). 
#Auxiliary Space: O(1).
def isPerfectSquare(x):
	
	left = 1
	right = x
	
	while (left <= right):
	
		mid = (left + right) >> 1
		if ((mid * mid) == x):
			return True

		if (mid * mid < x):
			left = mid + 1

		else:
			right = mid - 1
	return False

x=int(input())
if x == 0:
	print("Yes, it is a perfect square.")
elif (isPerfectSquare(x)):
	print("True")
else:
	print("False")
