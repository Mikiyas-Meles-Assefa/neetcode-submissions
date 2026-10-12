class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if nums == []:
            return 0
        newL = [[]]*len(nums)
        newL[0] = [nums[0]]
        j = 0
        for i in range(1, len(nums)):
            prev = nums[i-1]
            cur = nums[i]
            if prev + 1 == cur:
                newL[j].append(cur)
            else:
                j+=1
                newL[j] = [cur]
        longest = []
        longestsize = 0
        size = [0]*len(newL)
        for i in range(len(newL)):
            size[i] = len(newL[i])
        longestsize =max(size)


        return longestsize