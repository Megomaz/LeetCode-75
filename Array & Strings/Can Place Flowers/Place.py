class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0:
                if 0 <= i - 1 and i + 1 <= len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i - 1 < 0 and  i + 1 <= len(flowerbed) - 1 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i + 1 >= len(flowerbed) and i - 1 >= 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            i += 1

        return n == 0

# Cleaner solution (not mine)
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    count, prev = 0, 0

    for cur in flowerbed:
        if cur == 1:
            if prev == 1: # violation!
                count -= 1
            prev = 1
        else:
            if prev == 1: # can't plant
                prev = 0 
            else:
                count += 1
                prev = 1 # the cur plot gets taken
        
    return count >= n
