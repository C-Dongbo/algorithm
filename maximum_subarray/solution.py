import sys

class Solution:
    def maxSubArray(self, nums):
        max_val = -sys.maxsize
        window = 0
        for num in nums:
            window = max(window+num, num)
            max_val = max(max_val,window)
        return max_val
        

if __name__=='__main__':

    test = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(test))