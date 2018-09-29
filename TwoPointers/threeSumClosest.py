'''


Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self,A,B):
	#working code
	import pdb
#	pdb.set_trace()
	A.sort()
	min_diff = float('inf')
	for a in range(0,len(A)-2):
		i = a+1
		j = len(A)-1
		req = B-A[a]
		while i<j:
			if i ==a or j==a:
				break
			diff = req-(A[i]+A[j])
			if diff==0:
				pdb.set_trace()
				return A[a]+A[i]+A[j]
			if abs(diff) < min_diff:
				min_diff=abs(diff)
				idx = a,i,j
			if A[i]+A[j]<req:
				i+=1
			elif A[i]+A[j]>req:
				j-=1
	a,i,j=idx
	pdb.set_trace()
	return A[a]+A[i]+A[j]
				
			
    def notworkingthreeSumClosest(self, A, B):
	A.sort()
	diff = float("inf")
	result = 0
	import pdb
	pdb.set_trace()
	for i in range (0,len(A)-2):
		first = A[i]
		second = A[i+1]
		third = A[i+2]
		sum = first+second+third
		if sum-B == 0:
			return sum
		if abs(sum-B)<abs(diff):
			diff = sum-B
			result = sum
	return result
if __name__ == "__main__":
	obj = Solution()
	A=[2, 1, -9, -7, -8, 2, -8, 2, 3, -8]
	B = -1
	print obj.threeSumClosest(A,B)
