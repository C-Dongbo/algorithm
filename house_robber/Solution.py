class Solution:
    def rob(self, nums):
        pre_step, curr_step = 0 , 0

        for num in nums:
            pre_step, curr_step = curr_step , max(curr_step, pre_step + num)
        return curr_step

if __name__=='__main__':
    solution = Solution()
    test = [1,2,3,4]

    print(solution.rob(test))
