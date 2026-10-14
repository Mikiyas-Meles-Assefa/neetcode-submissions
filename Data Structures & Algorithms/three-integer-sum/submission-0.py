class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        newD = defaultdict(list)
        res = set()
        for i in range(len(nums)):
            newD[nums[i]].append(i)
        
        i, j = 0, 1
        while i < len(nums): 
            while j<len(nums):
                cursum = nums[i] + nums[j]
                if -cursum in newD:
                    for k in newD[-cursum]:
                        if k != i and k!= j:
                            h = len(res)
                            res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                            if len(res) > h:
                                print(i,j,k)
                            break
                j+=1
                if j == i:
                    j+=1
            j = 0
            i+=1
        return list(res)