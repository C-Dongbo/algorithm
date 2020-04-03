

class Solution:

    def minCostClimbingStairs(self, cost):
        one_step, two_step = 0 , 0
        for v in cost:
            one_step, two_step = v + min(one_step,two_step), one_step
        return min(one_step,two_step)


if __name__=='__main__':
    test = [10,15,20]
    test2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    print(solution.minCostClimbingStairs(test2))