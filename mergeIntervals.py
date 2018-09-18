# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param A, a list of Intervals
    # @return a list of Interval
    def merge(self, A):
	import pdb
	pdb.set_trace()
	A = sorted(A)
	s = A[0][0]
	e = A[0][1]
	result = []
	for i in range(1, len(A)):
		f = A[i][0]
		l = A[i][1]
		if f>s and f<=e and l>=e:
			e = l
		elif f<=s and l<=e:
			s = f
		elif f>e:
			result.append((s,e))
			s = f
			e = l
	result.append((s,e))
	return result
    def mergeIntervals(self,A):
	import pdb
	pdb.set_trace()
	if len(A)<=1:
		return A
	result =[]
	A= sorted(A)
	for i in range(0,len(A)-1):
		if A[
if __name__ == "__main__":
	A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
	obj = Solution()
	print obj.merge(A)
	
		
