class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
	if x == 0 or x == 1 or n == 1:
		return x%d
	if x == -1:
		return (-1+n)%d
	if x == 0:
		return 1%d
	result = self.calculate_power(x,n)%d
	return result

    def calculate_power(self,x,n):
	if n == 0: 
		return 1
	elif (n%2)==0:
		return (self.calculate_power(x,n/2)*self.calculate_power(x,n/2))
	else:
		return (x*self.calculate_power(x,n/2*self.calculate_power(x,n/2)))

if __name__ == "__main__":
	obj = Solution()
	print obj.pow(2,3,3)
	
