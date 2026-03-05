from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # index for next non-zero position

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Fill the rest with zeros
        for i in range(j, len(nums)):
            nums[i] = 0
