class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}

        for m,n in enumerate(nums):
            diff=target-n
            if diff in freq:
                return [freq[diff],m]

            freq[n]=m