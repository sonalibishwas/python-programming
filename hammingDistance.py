class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
	from itertools import combinations_with_replacement
	combi = combinations_with_replacement(A,2)
	modulo = 0
	for i in combi:
		print i
		modulo = modulo + self.distance(i)
		print modulo
	return (2*modulo)

    def distance(self,i):
	x = i[0]
	y = i[1]
	count = 0
	z = x ^ y
	count = self.binary(z)
	
	return count
    def binary(self,num):
	result = 0
	while num >0:
		if num%2==1:
			result +=1
		num = num/2
	return result

if __name__ == "__main__":
	obj = Solution()
	A = [2,4,6]
	import pdb
	pdb.set_trace()
	print obj.hammingDistance(A)
