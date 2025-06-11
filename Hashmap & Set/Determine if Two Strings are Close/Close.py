class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        hashmap1 = {}
        hashmap2 = {}

        if set(word1) != set(word2):
            return False

        for letter in word1:
            hashmap1[letter] = hashmap1.get(letter,0) + 1

        for letter in word2:
            hashmap2[letter] = hashmap2.get(letter,0) + 1
        
        
        return sorted(list(hashmap1.values())) == sorted(list(hashmap2.values()))
            