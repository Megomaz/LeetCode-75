class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtracking(i,curr):
            if len(curr) == len(digits):
                result.append(curr)
                return
                
            for char in (digit_to_letters[digits[i]]):
                backtracking(i + 1, curr + char)
            
        
        if digits:
            backtracking(0,"")

        return result