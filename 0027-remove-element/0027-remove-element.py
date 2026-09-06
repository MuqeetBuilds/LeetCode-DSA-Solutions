class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer =0
        for num in nums:
            if num!=val:
                nums[writer]=num
                writer +=1
        return writer
            
        