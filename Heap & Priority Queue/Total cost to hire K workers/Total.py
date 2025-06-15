class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i,j = 0, len(costs) - 1
        heapLeft = []
        heapRight = []
        total = 0

        for p in range(k):
            while len(heapLeft) < candidates and i <= j:
                heapq.heappush(heapLeft,costs[i])
                i += 1
            while len(heapRight) < candidates and j >= i:
                heapq.heappush(heapRight,costs[j])
                j -= 1
            
            if heapLeft and heapRight:
                if heapLeft[0] <= heapRight[0]:
                    total += heapq.heappop(heapLeft)
                else:
                    total += heapq.heappop(heapRight)
            elif heapLeft:
                total += heapq.heappop(heapLeft)
            elif heapRight:
                total += heapq.heappop(heapRight)

        return total
        