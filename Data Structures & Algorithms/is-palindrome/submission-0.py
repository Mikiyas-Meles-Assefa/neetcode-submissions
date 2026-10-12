class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newL = []
        for c in s:
            if c.isalnum():
                newL.append(c)
        news = "".join(newL)
        print(news, ''.join(list(reversed(news))))
        return ''.join(list(reversed(news))) == news