from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writer=0
        for reader in range(len(nums)):
            if nums[reader]!=0:
                nums[reader],nums[writer]=nums[writer],nums[reader]
                writer +=1
                