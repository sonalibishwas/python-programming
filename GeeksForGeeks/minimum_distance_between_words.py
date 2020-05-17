

class FindMininumDistance:
    def find_minimum_distance(self, hash_map, word1, word2):
        if word1 not in hash_map.keys() or word2 not in hash_map.keys():
            return -1
        word1_indices = hash_map[word1]
        word2_indices = hash_map[word2]
        i = 0
        j = 0
        min_distance = float('inf')
        while i < len(word1_indices):
            diff = abs(word1_indices[i] - word2_indices[j])
            if diff < min_distance:
                min_distance = diff
                if j < len(word2_indices) - 1:
                    j += 1
                else:
                    i += 1
            if diff > min_distance:
                i += 1
        return min_distance

    def construct_map(self, input_string):
        print(input)
        hash_map = {}
        words = input.split()
        for index, word in enumerate(words):
            if word in hash_map.keys():
                hash_map[word].append(index)
            else:
                hash_map[word] = [index]
        print(hash_map)
        return hash_map


if __name__ == "__main__":
    input = "Amazon is the best company to work for. The amazon is a beautiful forest"
    min_distance = FindMininumDistance()
    hash_map = min_distance.construct_map(input)
    result = min_distance.find_minimum_distance(hash_map, "Amazon", "the")
    print(result)
