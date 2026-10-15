class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        longestyet = 0
        i = 0
        start = 0
        while i < len(s):
            c = s[i]
            if i == 6: print("hi", c, start, i)
            if i==0:
                prev = {}
                prev[c] = i
                length += 1
                i+=1
            elif c not in prev:
                length += 1
                prev[c] = i
                if i == 6: print("ofc", i)
                i+=1
                
            else:
                if i == 6: print("ofc", i)

                if prev[c] >= start:
                    start = prev[c] + 1
                    length = i - start + 1
                    prev[c] = i
                else:
                    length+=1
                    prev[c] = i
                i+=1
            if length > longestyet:
                longestyet = length
        print(s[start:start+length])
        return longestyet