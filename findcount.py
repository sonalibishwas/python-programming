class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
	first = self.binarySearch(A,B,True)
	if first == -1:
		return 0
	last = self.binarySearch(A,B,False)
	result = last - first +1
	return result
	
    def binarySearch(self,A,B,firsthalf):
	start = 0
	end = len(A)-1
	result = -1
	while (start<=end):
		mid = (start+end)/2
		if A[mid] == B:
			result = mid
			if firsthalf:
				end = mid-1
			else:
				start = mid+1
		elif A[mid]>B:
			end = mid-1
		else:
			start = mid+1
	return result
if __name__ == "__main__":
	obj = Solution()
	A = [0,1,2,3,3,4,4,5]
	B = 0
	print obj.findCount(A,B)
