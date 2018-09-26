'''
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.
Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
	min = float('inf')
	A.sort()
	for i in range(0,len(A)-1):
		if A[i]^A[i+1]<min:
			min = A[i]^A[i+1] 
	return min
if __name__ == "__main__":
	obj = Solution()
	A = [0,2,5,7]
	print obj.findMinXor(A)
