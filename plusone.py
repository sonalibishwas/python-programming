class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
	B = []
	carry = 1
	for i in range(len(A)-1,-1,-1):
		sum = A[i]+carry
		if sum ==10:
			carry = 1
			B.append(0)
		else:
			carry =0
			B.append(sum)
	B.reverse()
	if carry == 1:
		B = [1]+B
	import pdb
	pdb.set_trace()
	while B[0]==0:
		B.pop(0)
	return B

if __name__ == "__main__":
	A=[0,0,9,9]
	print A
	obj = Solution()
	B = obj.plusOne(A)
	print B
	
