#Given an array of integers, every element appears twice except for one. Find that single one.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
	for x in A:
		if A.count(x)==1:
			return x
    def xorsolution(self,A):
	result = A[0]
	for i in range(1,len(A)):
		result^=A[i]
	return result
if __name__=="__main__":
	obj = Solution()
	A = [1,1,1,2]
	print obj.xorsolution(A)
