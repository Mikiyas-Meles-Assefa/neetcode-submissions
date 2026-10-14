class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        newL = [0] * len(nums)
        total = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros += 1
            else:
                total *= nums[i]
        if zeros>1:
            return newL
        for i in range(len(nums)):
            if zeros == 0:
                newL[i] = total // nums[i]
            elif nums[i] == 0:
                newL[i] = total
        return newL     
        