class Solution:
    # @param A : tuple of integers
    # @return a strings
    '''
    def largestNumber(self,A):
	for i in range(1,len(A)):
		value = A[i]
		hole = i
		
		while hole>0:
			str1 = (str(A[hole-1])+str(value)) 
			str2 = (str(value)+str(A[hole-1]))
			if str1<str2:
				A[hole]=A[hole-1]
				hole =hole -1
			else:
				break
		A[hole]=value
	result = "".join(str(x) for x in A)
	return result
    '''
    def largestNumber(self,A):
	A=map(str,A)
	A.sort(cmp=self.compare,reverse=True)
	print A
	if A[0]=='0':
		return '0'
	result = "".join(x for x in A)
	return result

    def compare(self,x,y):
	xy = str(x)+str(y)
	yx = str(y)+str(x)
	if xy>yx:
		return 1
	else:
		return -1
if __name__=="__main__":
	obj = Solution()
	A =[89,8] 
	print obj.largestNumber(A)	
