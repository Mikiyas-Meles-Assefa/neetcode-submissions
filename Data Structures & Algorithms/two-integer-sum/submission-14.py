class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict = {}

        for i in range(len(nums)):
            if target - nums[i] in newdict:
                x = newdict[target-nums[i]]
                y = i
                return [x,y]
            newdict[nums[i]] = i + newdict.get(nums[i], 0)

