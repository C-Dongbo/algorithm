from functools import lru_cache

class Solution:
    def stoneGame(self, piles):

        n = len(piles)

        @lru_cache(None)
        def dp(i, j):
            
            if i > j: return 0
            part = (j - i - n) % 2
            if part == 1:
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))
        
        if dp(0, n-1) > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    test = [5,3,4,5]
    solution = Solution()
    print(solution.stoneGame(test))