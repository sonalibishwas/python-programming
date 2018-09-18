class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
	size = len(A)
	start = 0
	end = size-1
	while start <=end:
		mid = (start+end)/2
		next = (mid+1)%size
		prev = (mid+size-1)%size
		if A[mid]<A[next] and A[mid]<A[prev]:
			return A[mid]
		elif A[mid]<=A[end]:
			end = mid -1
		else:
			start = mid + 1
	return None

if __name__== "__main__":
	obj = Solution()
	A = [5,6,7,8,2,3]
	print obj.findMin(A)
