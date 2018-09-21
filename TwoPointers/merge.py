class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
	if not A:
		return B
	if not B:
		return A
	result = []
	i = 0
	j = 0
	while i <len(A) and j<len(B):
		if A[i]<B[j]:
			result.append(A[i])
			i+=1
		elif A[i]>B[j]:
			result.append(B[j])
			j+=1
		else:
			result.append(A[i])
			result.append(B[j])
			i +=1
			j+=1
	if i<len(A):
		for x in range(i,len(A)):
			result.append(A[x])
	elif j<len(B):
		for x in range(j,len(B)):
			result.append(B[x])
	print(" ".join(str(x) for x in result) + " ")
if __name__ == "__main__":
	obj = Solution()
	A = [-4,3]
	B = [-2,-2]
	print obj.merge(A,B)
