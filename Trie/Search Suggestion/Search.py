class TrieNode:
    def __init__(self):
        self.children = {}
        self.array = []

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

            if len(cur.array) < 3:
                cur.array.append(word)  

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = PrefixTree()
        output = [[] for _ in (searchWord)]

        for word in products:
            prefix.insert(word)

        curr = prefix.root

        for index, char in enumerate(searchWord):
            if char not in curr.children:
                break
            curr = curr.children[char]
            output[index] = curr.array

        return output