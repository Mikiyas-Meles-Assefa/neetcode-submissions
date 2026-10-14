class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        newd = {}
        for i in range(len(strs)):
            t = [0]*26
            for j in range(len(strs[i])):
                t[ord(strs[i][j])-ord('a')] += 1
            t = tuple(t)
            newd[t] = [strs[i]] + newd.get(t, [])
        
        l = []
        for s in newd:
            l.append(newd[s])

        return l