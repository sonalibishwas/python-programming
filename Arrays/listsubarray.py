class Solution:
    # @param A : list of integers
    # @return a list of integers
    def find_max(self,list,sum):
	max=0
	max_index = 0
	for i in range(0,len(sum)):
		if sum[i] > max:
			max = sum[i]
			max_index = i
		if sum[i] == max :
			if (len(list[i])>len(list[max_index])):
				max_index = i
			if (len(list[i])==len(list[max_index])):
				if list[i][0] < list[max_index][0]:
					max_index = i
	return max_index	

    def maxset(self, A):
	B = []
	temp =[]
	sum = 0
	sub_sum=[]
	max_sum = float("-INF")
	for i in range(0,len(A)):
		if A[i]>-1:
			temp.append(A[i])
			sum = sum + A[i]
			continue
		
		if temp:
			B.append(temp)
			temp = []
			sub_sum.append(sum)
			sum =0
	if temp:
                        B.append(temp)
                        temp = []
                        sub_sum.append(sum)
                        sum =0
	#print B
	#print sub_sum
	if not B:
		return B
	max_index = self.find_max(B,sub_sum)
	return B[max_index]

if __name__ == "__main__":
	obj = Solution()
	A = [-1]
	result = obj.maxset(A)
	print result
