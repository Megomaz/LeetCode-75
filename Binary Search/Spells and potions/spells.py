class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = [0] * len(spells)
        size = len(potions)

        for i in range(len(spells)):
            index = 0
            l = 0
            r = size - 1

            while l < r:
                mid = (l + r) // 2

                if potions[mid] * spells[i] < success:
                    l = mid + 1
                else:
                    r = mid
            
            result[i] = size - r if potions[r] * spells[i] >= success else 0

        return result

# Solution using bisect (not mine)
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions so we can binary search them later
        potions.sort()
        m = len(potions)  # Total number of potions
        result = []       # Result list to store the number of successful pairs for each spell
        
        # For each spell, determine how many potions can form a successful pair
        for spell in spells:
            # We want: spell * potion >= success
            # Rearranged: potion >= success / spell
            # Compute the smallest potion value that would satisfy the condition (ceil division)
            min_potion = (success + spell - 1) // spell

            # Use binary search to find the first index where potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)

            # All potions from idx to end are valid (because potions is sorted)
            result.append(m - idx)
        
        # Return the result list containing the number of successful pairs for each spell
        return result

# Example
spells = [10, 20]
potions = [1, 2, 3, 4, 5]
success = 40

Spell = 10
	•	min_potion = ceil(40 / 10) = 4
	•	bisect_left(potions, 4) → index 3 (points to 4)
	•	Valid potions: [4, 5] → count = 2