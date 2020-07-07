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

    def countNegatives2(self, grid):
        global_cnt = 0

        def rec(sorted_list, low, high, cnt):
            
            if low > high:
                return cnt

            mid = int((low+high)/2)

            if sorted_list[mid] < 0:
                print(sorted_list)
                cnt += high - mid + 1
                cnt = rec(sorted_list, low, mid-1, cnt)

            else:
                cnt = rec(sorted_list, mid+1, high, cnt)
            return cnt
        global_cnt = 0
        for sorted_list in grid:
            global_cnt = rec(sorted_list, 0, len(sorted_list)-1, global_cnt)

        return global_cnt

if __name__ =='__main__':
    test = [[4,3,2,-1]]
    solution = Solution()
    print(solution.countNegatives2(test))
        