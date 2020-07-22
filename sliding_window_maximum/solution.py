import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        
        n = len(nums)
        queue = collections.deque()
        result_list = []

        for idx, num in enumerate(nums):

            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(idx)

            while queue and queue[0] <= idx - k:
                queue.popleft()

            if idx >= k - 1:
                result_list.append(nums[queue[0]])

        return result_list

if __name__ == '__main__':
    solution = Solution()

    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))