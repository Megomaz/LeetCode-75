lass Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = [j for j in range(1,10)]

        def dfs(i,length,curr,total):
            if length > k or total > n or i > len(nums):
                return

            if total == n and length >= k:
                result.append(curr[:])
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j+1, length + 1,curr, total + nums[j])

                curr.pop()       

        dfs(0,0,[],0)
        return result
            