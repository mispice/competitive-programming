class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l_counter = 0
        counter = []
        for i in range(len(nums)):
            for a in range(len(nums)):
                if(i==a):
                    continue
                elif nums[i]>nums[a]:
                    l_counter+=1
            counter.append(l_counter)
            l_counter = 0
        return counter
