class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        newd = {}
        for i in range(len(strs)):
            newd[str(sorted(list(strs[i])))] = [strs[i]] + newd.get(str(sorted(list(strs[i]))), [])
        
        l = []
        for s in newd:
            l.append(newd[s])

        return l