class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast < 0:
                while True:
                    if stack and stack[-1] > 0 and stack[-1] < abs(ast):
                        stack.pop()
                    elif stack and stack[-1] > 0 and stack[-1] > abs(ast):
                        break
                    elif stack and stack[-1] > 0 and stack[-1] == abs(ast):
                        stack.pop()
                        break
                    else:
                        stack.append(ast)
                        break
            else:
                stack.append(ast)
            
        return stack

        # append in postivive, if negat check if stack -1 is <= abs(ast) -> if it is pop and dont append, if it crashes dont append but dont pop 

# Cleaner solution (not mine)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack