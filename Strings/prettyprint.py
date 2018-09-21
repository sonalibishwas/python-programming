class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
      length = A*2-1
      result = [[A]*length]*length
      extra = [A]
      for i in range (1,A):
          temp=extra+([A-i]*((A-i)*2-1))
          extra.reverse()
          temp = temp + extra
          extra.reverse()
          result[i]=temp
          result[length-i-1] = result[i]
          extra.append(A-i)
      return result

if __name__ == "__main__":
	obj = Solution()
	A = 5
	print obj.prettyPrint(A)
