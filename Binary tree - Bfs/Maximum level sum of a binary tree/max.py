# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxx = float('-inf')
        lvl = 1

        q = deque([(root,1)])

        while q:
            size = len(q)
            total = 0

            for _ in range(size):
                node, level = q.popleft()

                total += node.val

                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

            if total > maxx:
                maxx = total
                lvl = level

        return lvl 