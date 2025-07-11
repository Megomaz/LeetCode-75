class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        #prefix
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        #postfix
        for i in range(len(nums) -2 ,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = postfix[i] * prefix[i]

        return nums