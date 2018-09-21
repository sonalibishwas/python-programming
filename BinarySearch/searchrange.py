class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
	import pdb
	pdb.set_trace()
	first = self.binarySearch(A,B,True)
	last = 	self.binarySearch(A,B,False)
	return [first,last]
    def binarySearch(self,A,B,first):
	result = -1
	low =0
	high = len(A)-1
	while low <=high:
		mid = (low+high)/2
		if A[mid] == B:
			result=mid
			if first:
				high = mid -1
			else:
				low = mid + 1
		elif A[mid] >B:
			high = mid -1
		else:
			low = mid+1
	return result 

if __name__=="__main__":
	obj = Solution()
	A = [1,2,3,4,8,8,9]
	print obj.searchRange(A,2)
