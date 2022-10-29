class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        counter = length - 1
        maxArea = 0
        i = 0
        for j in range(length):
            minimum = min(height[i],height[counter])
            mult = minimum * (counter-i)
            if mult > maxArea:
                maxArea = mult
            if height[i] >= height[counter]:
                counter-=1
            elif height[i] < height[counter]:
                i+=1
        return maxArea
