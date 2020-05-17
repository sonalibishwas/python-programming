# bubble sort algorithm


class BubbleSort:
    def bubble_sort(self, A):
        n = len(A)
        print(A)
        for i in range(n, 0, -1):
            for j in range(n - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
        print("Sorted")
        print(A)


if __name__ == "__main__":
    bubble_obj = BubbleSort()
    A = [6, 4, 2, 1, 3, 9, 33, 11, 199]
    bubble_obj.bubble_sort(A)
