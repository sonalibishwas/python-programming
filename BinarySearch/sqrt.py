class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
	if A <=1:
		return A
	low = 0
	high = A/2
	result = 0
	while low <=high:
		mid = (low+high)/2
		if (mid*mid)==A:
			return mid
		if (mid*mid)>A:
			high = mid-1
		else:
			result = mid
			low = mid+1
		
	return result
if __name__ == "__main__":
	obj = Solution()
	print obj.sqrt(1)
