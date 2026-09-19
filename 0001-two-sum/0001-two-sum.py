class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem={}
        for index in range(len(nums)):
            current_number = nums[index]
            n_target =target - current_number
            if n_target in mem:
                return [mem[n_target],index]
            mem[current_number]=index