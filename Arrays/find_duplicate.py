class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
	if not A:
		return -1
	B= [A[0]]
	for i in range(1,len(A)):
		if A[i] in B:
			return A[i]
		else:
			B.append(A[i])
	return -1

if __name__ == "__main__":
	obj = Solution()
	A = [1,2,3]
	result = obj.repeatedNumber(A)
	print result
