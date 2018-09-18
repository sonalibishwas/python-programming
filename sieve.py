import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
	primes = range(0,A+1)
	primes[1]=0
	for i in range(2,int(math.sqrt(A))+1):
		if not primes[i] == 0:
			j = 2
			import pdb
			pdb.set_trace()
			while i * j <= A:
				primes[i*j]=0
				j+=1
	result = [x for x in primes if not x ==0]
	return result

if __name__ == "__main__":
	obj = Solution()
	A = 15
	print obj.sieve(A)
