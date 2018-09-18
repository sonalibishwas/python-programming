import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
	if A == 1 or A == 0:
		return 0
	for i in range(2, int(math.sqrt(A))+1):
		if A%i == 0:
			return 0
	return 1

if __name__ == "__main__":
	obj = Solution()
	A = 7
	print (obj.isPrime(A))
