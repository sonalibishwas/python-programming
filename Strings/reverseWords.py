class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
	B = A.split()
	B.reverse()
	result = " ".join(B)
	return result

if __name__ == "__main__":
	obj = Solution()
	A = "Hello  World"
	print obj.reverseWords(A)
