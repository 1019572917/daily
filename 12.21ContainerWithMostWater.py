class Solution:
    def maxArea(self, height):
        length = len(height)
        answer = 0
        for i in range(length):
            for j in range(i+1,length):
                width = j - i
                height1 = min(height[i],height[j])
                s = width * height1
                if s >= answer:
                    answer = s
        return answer
