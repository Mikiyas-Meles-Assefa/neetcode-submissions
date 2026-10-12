class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter

        d = Counter(nums)

        res = []
        for i in range(k):
            highest = 0
            highestnum = 0
            for i, k in d.items():
                if k>highest:
                    highestnum = i
                    highest = k
            res.append(highestnum)
            del d[highestnum]

        return res