class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        right_prefix = 0
        left_prefix = 0

        for i in range(len(nums)):
            right_prefix = total - nums[i] - left_prefix

            if left_prefix == right_prefix:
                return i

            left_prefix += nums[i]

        return -1