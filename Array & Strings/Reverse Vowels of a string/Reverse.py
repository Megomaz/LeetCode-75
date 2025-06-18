class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        arr = []
        result = []

        for i in range(len(s)):
            if s[i] in vowels:
                arr.append(i)
            result.append(s[i])

        l,r = 0, len(arr) - 1

        while l <= r:
            result[arr[l]],result[arr[r]]  = result[arr[r]], result[arr[l]]
            l += 1
            r -= 1

        return "".join(result)