class FlattenList:
    def flatten_list(self, A):
        result = []
        for i in A:
            if isinstance(i, list):
                result = result + self.flatten_list(i)
            else:
                result.append(i)
        return result


if __name__ == "__main__":
    A = [1,[2,3]]
    print(A)
    object = FlattenList()
    result = object.flatten_list(A)
    print(result)