'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self,A):
	#working code
	i = 0
	j = len(A)-1
	max = float('-inf')
	while i<j:
		area = (j-i)*min(A[i],A[j])
		if area>max:
			max = area
		if A[i]>A[j]:
			j-=1
		if A[i]<=A[j]:
			i+=1
	return max
    def notworkingmaxArea(self, A):
	#eg A=[1,5,4,3]
	max_area = 0
	j = len(A)-1
	for i in range(0,len(A)-1):
			distance = abs(j-i)
			height = min(A[i],A[j])
			area = distance*height
			if area >max_area:
				max_area=area
#				print "max_area=%s"%max_area
#				print A[i],A[j]
	return max_area

if __name__ == "__main__":
	obj=Solution()
	A = [3,4,6,7,1,2]
	print obj.maxArea(A)
