class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        dir = 0
        T =0 
        B = len(A)-1
        L = 0
        R = len(A[0])-1
        result = []
        import pdb
	pdb.set_trace()
	while (T<=B and L<=R):
            if dir == 0:
                for i in range(L,R+1):
                    result.append(A[T][i])
                dir+=1
                T+=1
            elif dir == 1:
                for i in range(T,B+1):
                    result.append(A[i][R])
                dir+=1
                R-=1
            elif dir == 2:
                for i in range(R,L-1,-1):
                    result.append(A[B][i])
                dir+=1
                B-=1
            elif dir == 3:
                for i in range(B,T-1,-1):
                    result.append(A[i][L])
                dir =0
                L+=1
        return result
if __name__ == "__main__":
	obj = Solution()
	A = [[1,2,3],[1,2,3]]
	result = obj.spiralOrder(A)
	print result
