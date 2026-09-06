class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k =1
        for reader in range(1,len(nums)):
            if nums[reader] != nums[reader-1]:
                nums[k] = nums[reader]
                k +=1
        return k