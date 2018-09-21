class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
	if A == 0:
		return "0"
	result = ""
	while A>0:
		result = str(A%2) + result
		A = A/2
	return result

if __name__ == "__main__":
	obj = Solution()
	A = 10
	print obj.findDigitsInBinary(A)	
