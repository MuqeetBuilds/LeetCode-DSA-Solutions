class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result= [0]*len(nums)
        left=0
        right=len(nums)-1
        for writer in range(len(nums)-1,-1,-1):
            left_square = nums[left]*nums[left]
            right_square = nums[right]*nums[right]
            if left_square>right_square:
                result[writer]=left_square
                left +=1
            else :
                result[writer]= right_square
                right -=1

        return result 

        
            
        