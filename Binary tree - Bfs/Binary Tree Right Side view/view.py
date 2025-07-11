# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(root, 0)])
        result = []
        check = set()

        while q:
            node, level = q.popleft()

            if level not in check:
                check.add(level)
                result.append(node.val)

            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))
        return result