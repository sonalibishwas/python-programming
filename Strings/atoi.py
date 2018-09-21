import re
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
	maxint = 2147483647
	minint = -2147483647
	result = 0
	i = A.split()[0]
	res=re.sub('[^0-9 \+ \-].*','',i)
	if not res=='':
		if res.isdigit() or ((res[0]== '+' or res[0]=='-') and res[-1].isdigit()):
			result = int(res)
	result = maxint if result > maxint else result
	result = minint if result <minint else result
	return result

if __name__ == "__main__":
	obj = Solution()
	A= "-9 99"
	print obj.atoi(A)
