from copy import deepcopy
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    '''
    def setZeroes(self, A):
	i = 0
	B = deepcopy(A)
	import pdb
	pdb.set_trace()
	for i in range(0,len(A)):
		for j in range(0,len(A[0])):	
			if A[i][j]==0:
				#mark all rows
				B[i]=[0] * len(A[0])
				# mark all columns
				for k in range(0,len(A)):
					B[k][j]=0
				
		
	return B
    '''
    def setZeroes(self,A):
	markrows =[]
	markcols =[]
	for i in range(0,len(A)):
		for j in range(0,len(A[0])):
			if A[i][j]==0:
				markrows.append(i)
				markcols.append(j)
	markrows = list(set(markrows))
	markcols = list(set(markcols))
	for i in range(0,len(A)):
		if i in markrows:
			A[i] = [0]*len(A[0])
			continue
		for j in markcols:
			A[i][j]=0
	return A
if __name__ == "__main__":
	obj = Solution()
	A=[[1,0,1],[1,1,1],[1,1,1]]
	print obj.setZeroes(A)
