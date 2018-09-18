import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
	factors = []
	for i in range(1,int(math.ceil(math.sqrt(A)))+1):
		if A%i == 0:
			factors.append(i)
			factors.append(A/i)
	factors=list(set(factors))
	factors.sort()
	return factors
if __name__ == "__main__":
	obj = Solution()
	A = 182
	factors = obj.allFactors(A)
	print factors
