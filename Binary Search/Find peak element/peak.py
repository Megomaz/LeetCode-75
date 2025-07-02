class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums) - 1
        l,r = 0, length

        while l <= r:
            mid = l + ((r-l)//2)
            prev = nums[mid-1] if mid - 1 >= 0 else -float('inf')
            after = nums[mid+1] if mid + 1 <= length else -float('inf')

            if nums[mid] > prev and nums[mid] > after:
                return mid
            elif after > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l
            
