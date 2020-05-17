"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord.
"""
from copy import deepcopy
import time
class AllPath:
    def __init__(self, ladder=None, next=None):
        self.path = ladder
        self.next = next

class Ladder:
    def __init__(self, path=None, lastword=None):
        if path is None:
            path = []
        self.path = path
        self.lastword = lastword
        self.length = len(self.path)


class TransformWord:
    def add_item_to_dictionary(self, dictionary, item):
        dictionary.append(item)

    def transform(self, start_word, end_word):
        # all paths stored here
        allPaths = None
        head = None
        # shortest path stored here
        shortestPath = Ladder(None, None)
        path = [start_word]
        ladder = Ladder(path, start_word)
        shortestPath = self.transform_helper(start_word, end_word, dictionary, ladder, head, allPaths, shortestPath)
        print("Final shortest path = {}".format(shortestPath.path))

    def transform_helper(self, start_word, end_word, dictionary, ladder, head, allPaths, shortestPath):
        if ladder.lastword is end_word:
            print("wohoo we found an end ladder = {}".format(ladder.path))
            if len(shortestPath.path) == 0:
                shortestPath.path = deepcopy(ladder.path)
                shortestPath.lastword = deepcopy(ladder.lastword)
            else:
                print("ladder length = {}, shortestpath length = {}".format(ladder.length, shortestPath.length))
                if len(ladder.path) < len(shortestPath.path):
                    print("ladder = {}, shortestpath={}".format(ladder.path,shortestPath.path))
                    shortestPath.path = deepcopy(ladder.path)
                    shortestPath.lastword = deepcopy(ladder.lastword)
            print("shortestPath={}".format(shortestPath.path))
            return shortestPath

        for item in dictionary:
            #print("item in hand = {}".format(item))
            #print("Ladder={} and lastword ={}".format(ladder.path, ladder.lastword))
            if item not in ladder.path and self.a_letter_diff(item, ladder.lastword):
                #print("item good to add")
                path = deepcopy(ladder.path)
                #print("path right now {}".format(path))
                path.append(item)
                #print("path after adding item {}".format(path))
                shortestPath = self.transform_helper(start_word, end_word, dictionary, Ladder(path, path[-1]), head, allPaths, shortestPath)
                path.pop()
                #print("removing already traversed item, path now {}".format(path))
        return shortestPath

    def a_letter_diff(self, word1, word2):
        #print("comparing {} and {} for a letter difference".format(word1, word2))
        if len(word1) != len(word2):
            #print("word length is not same return false")
            return False
        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1
        return True if diff_count == 1 else False

if __name__ == "__main__":
    print(time.ctime())
    dictionary = []
    transform_object = TransformWord()
    transform_object.add_item_to_dictionary(dictionary, "CAT")
    transform_object.add_item_to_dictionary(dictionary, "SAT")
    transform_object.add_item_to_dictionary(dictionary, "SAR")
    transform_object.add_item_to_dictionary(dictionary, "CAR")
    transform_object.add_item_to_dictionary(dictionary, "CAR")
    transform_object.add_item_to_dictionary(dictionary, "TAR")
    transform_object.add_item_to_dictionary(dictionary, "BUT")
    transform_object.add_item_to_dictionary(dictionary, "TOR")
    transform_object.add_item_to_dictionary(dictionary, "DOG")
    transform_object.add_item_to_dictionary(dictionary, "TOY")
    word1 = "CAT"
    word2 = "TOY"
    print("Dictionary is = {}".format(dictionary))
    print("We need to transform {} into {}".format(word1, word2))
    transform_object.transform(word1, word2)
    print(time.ctime())
