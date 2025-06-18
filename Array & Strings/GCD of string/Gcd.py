class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l, r = 0,0
        size = len(str1)
        size2 = len(str2)
        curr = ""
        result = ""

        while r < len(str2) and l < len(str1):
            if str1[l] == str2[r]:
                curr += str2[r]
                if (size // len(curr)) * curr == str1 and (size2 // len(curr)) * curr == str2 :
                    result = curr
            else:
                break
            l += 1
            r += 1

        return result

# Better Solution (not mine)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]