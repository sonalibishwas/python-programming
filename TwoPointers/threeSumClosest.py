'''


Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
	A.sort()
	diff = float("inf")
	result = 0
	import pdb
	pdb.set_trace()
	for i in range (0,len(A)-2):
		first = A[i]
		second = A[i+1]
		third = A[i+2]
		sum = first+second+third
		if sum-B == 0:
			return sum
		if abs(sum-B)<abs(diff):
			diff = sum-B
			result = sum
	return result
if __name__ == "__main__":
	obj = Solution()
	A = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
	B = -3
	print obj.threeSumClosest(A,B)
