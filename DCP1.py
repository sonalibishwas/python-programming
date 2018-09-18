"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
def check(A,k):
	d = dict()
	for i in range(0,len(A)):
		comp = abs(A[i]-k)
		if A[i] in d.keys():
			return A[i],A[d[A[i]]]
		else:
			d[comp]=i
	return None,None
if __name__ == "__main__":
	A=[10,15,3,7]
	k = 17
	num1,num2 = check(A,k)
	print num1, num2
