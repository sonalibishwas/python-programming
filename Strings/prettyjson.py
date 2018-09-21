class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
	output = []
	space = 0
	value = ''
	for i in range(0,len(A)):
		if A[i] == '{' or A[i] == '[':
			if not value == '':
				output.append('\t'*space+value)
			output.append('\t'*space+A[i])	
			space +=1
			value=''
		elif A[i] == '}' or A[i] == ']':
			if not value == '':
				output.append('\t'*space+value)
			space -=1
			if i+1 == len(A) or not A[i+1]==',':
				output.append('\t'*space+A[i])
				value=''
			else:
				value = A[i]
			
		elif A[i] == ',':
			value = value+A[i]
			output.append('\t'*space+value)
			value=''
		else:
			value=value+A[i]
	return output
if __name__ == "__main__":
	obj = Solution()
	A = """{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"""
	print obj.prettyJSON(A)
