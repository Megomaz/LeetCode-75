class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string

                stack.pop() # removes '[' bracket

                value = ""
                while stack and stack[-1].isdigit():
                    value = stack.pop() + value
                stack.append(int(value) * string)

        return "".join(stack)
