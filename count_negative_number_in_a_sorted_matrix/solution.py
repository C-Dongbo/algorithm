class Solution:
    def countNegatives(self, grid):
        cnt = 0

        for sorted_list in grid:
            low = 0
            high = len(sorted_list) - 1
            print(sorted_list)
            while low <= high:
                mid = int((low+high)/2)

                if sorted_list[mid] < 0:
                    cnt += high - mid + 1
                    high = mid - 1
                else:
                    low = mid + 1
        return cnt


if __name__ =='__main__':
    test = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    solution = Solution()
    print(solution.countNegatives(test))
        