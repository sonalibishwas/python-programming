class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
	C = sorted(A+B)
	if len(C)%2 == 0:
		result = (C[len(C)/2]+C[(len(C)/2)-1])/2.0
		return result
	else:
		return C[(len(C))/2]

if __name__ == "__main__":
	obj = Solution()
	A= [1,3]
	B = [2,4]
	print obj.findMedianSortedArrays(A,B)
