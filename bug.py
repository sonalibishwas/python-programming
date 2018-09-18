class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
	import pdb
	pdb.set_trace()
        for i in xrange(len(a)):
            ret.append(a[(i + b)%len(a)])
        return ret

if __name__ == "__main__":
	obj = Solution()
	a = [1,2,3,4]
	b = 1
	result =obj.rotateArray(a,b)
	print result

