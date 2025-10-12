from typing import List

class Solution:       
    def moveZeroes(self, nums: List[int]) -> None:
        position = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[position] = nums[index]
                position+=1

        for index in range(position, len(nums)):
            nums[index] = 0
    
    def swap(self, nums, first_index, next_index):
        temp = nums[first_index]
        nums[first_index] = nums[next_index]
        nums[next_index] = temp
    
    def moveZeroOptimized(self, nums: List[int]) -> None:
        position = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                if position != index:
                    self.swap(nums, position, index)
                position+=1

