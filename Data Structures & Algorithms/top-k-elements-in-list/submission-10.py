class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        freq = []
        for k1,v in count.items():
            freq.append([v, k1])
        
        freq.sort(reverse = True)
        res = []
        print(k)
        for i in range(k):
            res.append(freq[i][1])
        
        return res