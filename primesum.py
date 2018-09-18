import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
	for i in range(2, A):
		if self.isPrime(i) and self.isPrime(A-i):
			return [i,A-i]
	return []

    def isPrime(self, A):
        if A == 1 or A == 0:
                return False
        for i in range(2, int(math.sqrt(A))+1):
                if A%i == 0:
                        return False
        return True
    def generateprime(self,A):
	primes = self.sieve(A)
	for i in primes:
		if (A-i) in primes:
			return [i,A-i]	
	return []
    
    def sieve(self, A):
        primes = range(0,A+1)
        primes[1]=0
        for i in range(2,int(math.ceil(math.sqrt(A)))+1):
                if not primes[i] == 0:
			if self.isPrime(A-primes[i]):
				return [primes[i],A-primes[i]]
                        j = 2
                        while i * j <= A:
                                primes[i*j]=0
                                j+=1
        #result = [x for x in primes if not x ==0]
        #return result
	return []
if __name__=="__main__":
	obj = Solution()
	A = 16777214
	print obj.sieve(A)
