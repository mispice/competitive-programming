class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indice_list = []
        for i in range(len(nums)):
            sindex = i
            for a in range(i+1,len(nums)):
                if nums[sindex]>nums[a]:
                    sindex = a
            nums[i],nums[sindex] = nums[sindex],nums[i]
        for i in range(len(nums)):
            if target == nums[i]:
                indice_list.append(i)
        return indice_list
