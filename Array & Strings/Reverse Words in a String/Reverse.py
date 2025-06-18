class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        curr = ""

        for i in range(len(s)):
            if s[i] == " " and curr != "":
                result.append(curr)
                curr = ""
                continue
            elif s[i] == " ":
                continue
            curr += s[i]

        if curr != "":
            result.append(curr)

        final = result[::-1]
        return " ".join(final)
             
            