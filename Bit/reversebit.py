#Reverse bits of an 32 bit unsigned integer
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
	bin_num = bin(A)
	rev_bin_num = bin_num[-1:1:-1]
	rev_bin_num = rev_bin_num + (32-len(rev_bin_num))*'0'
	rev_num = int(rev_bin_num,2)
	return rev_num
if __name__ == "__main__":
	A = 3
	obj=Solution()
	print obj.reverse(A)
