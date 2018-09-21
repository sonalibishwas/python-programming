import pdb
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
	print "size of A = ", A[0]
	print "size of B = ", B[0]
	i = 1
	step = 0
	while i < A[0]:
#		pdb.set_trace()
		x = i
		y = i + 1
		print "point 1 = ",A[x],B[x]
		print "point 2 = ",A[y],B[y]
		if abs(A[y]-A[x])<=1:
		 if abs(B[y]-B[x])<=1:
			step +=1
			i +=1
		 else:
		 	A[x]+=(A[y]-A[x])
		 	B[x]+=1 if B[y]>B[x] else -1 
		 	step +=1
		else:
		 if abs(B[y]-B[x])<=1:
		 	step+=1
		 	A[x]+=1 if A[y]>A[x] else -1
		 	B[x]=B[x]+(B[y]-B[x])
		 else:
		 	step +=1
		 	A[x]+=1 if A[y]>A[x] else -1
		 	B[x]+=1 if B[y]>B[x] else -1
		if step >300:
			break
	print "steps = %s" %step
if __name__ == "__main__":
	A = [20,-5, 7, -12, 4, -6, 2, -5, -12, -6, 3, 11, 10, -8, 11, -13, -8, 5, -12, 4, 4]
	B = [20,-6, 6, -8, -13, -2, -9, -10, -10, -7, -14, 9, -8, -4, 8, 13, -11, 13, 5, 9, 11]
#	A = [2,-11,-12]
#	B =[2,-6,-8]
	cover = Solution()
	cover.coverPoints(A,B)

