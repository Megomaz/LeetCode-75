# Not my solution
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs = sorted(pairs, key = lambda p:p[1], reverse = True) # sort based on nums2 in descending order

        minHeap = []
        n1Sum = 0
        res = 0
        print(pairs)
        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap) # we pop min of n1 since it would affect the Sum
                n1Sum -= n1Pop

            if len(minHeap) == k:
                res = max(res, n1Sum * n2) # since its in ascending order, n2 will always be min

        return res