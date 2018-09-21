class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
	import re
	A=re.sub("\W",'',A)
	A=A.lower()
	B = A[::-1]
	if A == B:
		return 1
	else:
		return 0

if __name__ == "__main__":
	obj = Solution()
	A = "A man, a plan, a canal: Panama"
	print obj.isPalindrome(A)
