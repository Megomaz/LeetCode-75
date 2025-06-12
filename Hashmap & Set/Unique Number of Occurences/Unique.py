class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        checker = set()
        hashmap = defaultdict(int)

        for num in arr:
            hashmap[num] += 1

        for num in hashmap.values():
            if num in checker:
                return False
            checker.add(num)

        return True