class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            smallest_index = i
            for a in range(i+1,len(nums)):
                if nums[smallest_index]>nums[a]:
                    smallest_index = a
            nums[i],nums[smallest_index] = nums[smallest_index],nums[i]
