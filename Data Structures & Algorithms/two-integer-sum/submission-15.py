class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsset = set()
        for i in range(len(nums)):
            if (target-nums[i]) in numsset:
                x = nums[i]
                a = i
                break
            numsset.add(nums[i])
            
        x = nums.index(target-nums[a])
        return [x,a]