class Solution:
    def compress(self, chars: List[str]) -> int:
        r = 0
        s = ""

        while r < len(chars):
            count = 0
            l = r
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
                count += 1

            if count == 1:
                s += chars[l]
            elif count >= 2 and count <= 9:
                s += chars[l]
                s += str(count)
            elif count >= 10:
                digits = [str(int(d)) for d in str(count)]
                s += chars[l]
                for d in digits:
                    s += d

        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)


#Optimal Solution (not mine)
class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans