class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        newL = [1] * len(nums)
        total = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros += 1
            total *= nums[i]
        
        for i in range(len(nums)):
            if nums[i] != 0:
                newL[i] = total // nums[i]
            else:
                if zeros == 1:
                    total2 = 1
                    for j in range(len(nums)):
                        if nums[j]!=0:
                            total2 *= nums[j]
                    newL[i] = total2
                else:
                    return [0]*len(nums)
        return newL     
        