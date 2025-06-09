class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        total = 0

        for i in range(len(gain)):
            total += gain[i]
            highest = max(highest,total)
        
        return highest 