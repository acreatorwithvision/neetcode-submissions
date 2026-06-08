class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_zero=0

        for i in range(len(nums)):
            if nums[i]:
                nums[insert_zero],nums[i]=nums[i],nums[insert_zero]
                insert_zero=insert_zero+1
        