class BiggestNumber:
    def find_max(self, A):
        return max(A)

    def form_biggest_number(self, A):
        answer = ''
        B = self.padding(A)
        B.sort(reverse=True)
        for b in B:
            answer = answer + b[1]
        return answer


    def padding(self, A):
        max_num = self.find_max(A)
        B = []
        for i in range(len(A)):
            temp = str(A[i]) * max_num
            B.append((temp[:max_num], str(A[i])))
        return B

if __name__ == "__main__":
    A = [9,33,555,77]
    biggest_obj = BiggestNumber()
    answer = biggest_obj.form_biggest_number(A)
    print (answer)