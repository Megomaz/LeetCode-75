class SmallestInfiniteSet:

    def __init__(self):
        self.infinitySet = set()
        self.heap = []
        heapq.heapify(self.heap)

        for i in range(1,1001):
            self.infinitySet.add(i)

    def popSmallest(self) -> int:
        for i in range(1,1001):
            if i in self.infinitySet:
                self.infinitySet.remove(i)
                heapq.heappush(self.heap,i)
                return i

    def addBack(self, num: int) -> None:
        if num not in self.infinitySet:
            self.infinitySet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)



# Optimal solution (not mine)
class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.s = set()

    def popSmallest(self):
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        else:
            self.cur += 1
            return self.cur - 1

    def addBack(self, num):
        if self.cur > num:
            self.s.add(num) 