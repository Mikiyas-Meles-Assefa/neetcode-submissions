class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use default dict to use append (which wont take o(n) time in cases all strings in the list are anagrams to concatenate as a normal dict would)
        newd = defaultdict(list)
        for i in range(len(strs)):
            t = [0]*26
            for j in range(len(strs[i])):
                t[ord(strs[i][j])-ord('a')] += 1
            t = tuple(t)
            newd[t].append(strs[i])
        
        l = []
        for s in newd:
            l.append(newd[s])

        return l