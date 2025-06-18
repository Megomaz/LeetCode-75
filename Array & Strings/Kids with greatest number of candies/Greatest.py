class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= high:
                candies[i] = True
            else:
                candies[i] = False
        return candies