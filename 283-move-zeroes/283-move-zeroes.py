class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == 0:
        #             temp = nums[i]
        #             nums[i] = nums[j]
        #             nums[j] = temp
        
        a = []
        
        for i in range(len(nums)):
            if nums[i] != 0:
                a.append(nums[i])
                
        for i in range(len(a), len(nums)):
            a.append(0)
            
        nums[:] = a
        