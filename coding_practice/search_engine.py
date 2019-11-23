import collections
from typing import List

"""
Algorithm used: Trie: Pronounced 'Try'
Trie is a tree like data structure wherein the nodes of the tree store the entire alphabet & strings/words can be reTRIEved by traversing down a brach of the tree.

Link: https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014

Hash tables use arrays combined with linked lists, whereas tries use arrays combined with pointers/references.

Complexity: O(m*n) where m = length of longest key, n = total number of keys in the tire

"""


class Trie:
    def __init__(self):
        self.hot_rank = 0
        self.data = None
        self.children = {}
        self.isword = False


class Solution:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.keyword = ""

        for index, sentence in enumerate(sentences):
            self.add_record(sentence, times[index])

    def add_record(self, sentence, hot_rank):
        node = self.root

        for c in sentence:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        # for the last node we update the initialized values to store the data and hot_rank

        node.isword = True
        node.hot_rank -= hot_rank
        node.data = sentence

    def dfs(self, node):
        result = []
        if node:
            if node.isword:
                result.append((node.data, node.hot_rank))
            for child in node.children:
                result.extend(self.dfs(node.children[child]))
        return result

    def search_record(self, sentence):
        node = self.root

        for c in sentence:
            if c not in node.children:
                return []
            node = node.children[c]
        return self.dfs(node)

    def input(self, c: str) -> List[str]:
        result = []
        if c != "#":
            self.keyword += c.lower()
            result = self.search_record(self.keyword)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""

        sort = sorted(result, key=lambda x: x)
        ret = [item[0] for item in sort]
        # print(sort)
        return ret[:3]


sentences = [
    "i love you",
    "island",
    "iroman",
    "i love leetcode",
    "omlette",
    "meatballs",
    "deceptive",
]
times = [5, 3, 2, 2, 3, 2, 1]
obj = Solution(sentences, times)

characters = ["i", " ", "a", "#"]
for c in characters:
    print(obj.input(c))

