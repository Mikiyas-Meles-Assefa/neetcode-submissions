class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d = Counter(nums)
        freq = []
        for k1,v in d.items():
            freq.append([v, k1])
        
        freq.sort(reverse = True)
        res = []
        print(k)
        for i in range(k):
            res.append(freq[i][1])
        
        return res