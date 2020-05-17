
class MergeSort:
    def merge_sort(self, A):
        if len(A) > 1:
            # find the midpoint
            mid = len(A) // 2
            # get left half
            left_arr = A[:mid]
            print("left_array"+str(left_arr))
            # get right half
            right_arr = A[mid:]
            print("right_array"+str(right_arr))
            # call merge_sort on left half
            self.merge_sort(left_arr)
            # call merge sort on right half
            self.merge_sort(right_arr)
            # merge

            i = 0
            j = 0
            k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    A[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    A[k] = right_arr[j]
                    j += 1
                    k += 1
            while i < len(left_arr):
                A[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                A[k] = right_arr[j]
                j += 1
                k += 1

if __name__ == "__main__":
    merge_obj = MergeSort()
    A = [23 ,5 ,1 ,3 ,6 ,9]
    print(A)
    merge_obj.merge_sort(A)
    print("Sorted")
    print(A)
