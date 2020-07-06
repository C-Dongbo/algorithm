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


    def stoneGame2(self, piles):

        if not piles:
            return 0

        n = len(piles)
        memo = {}
        m = 1
        i = 0

        def dfs(i, m):
            if i == n:
                return 0

            if (i, m) in memo:    
                return memo[(i, m)]

            if i+2*m >= n:
                memo[(i, m)] = sum(piles[i:])
            else:
                total = sum(piles[i:])
                result = 0
                for j in range(1, 2*m+1):
                    result = max(result, total-dfs(i+j, max(j, m)))
                memo[(i,m)] = result
            
            return memo[(i, m)]

        return dfs(i, m)
if __name__ == '__main__':


    ## stone1
    # Input: [5,3,4,5]
    # Output: true
    # Explanation: 
    # Alex starts first, and can only take the first 5 or the last 5.
    # Say he takes the first 5, so that the row becomes [3, 4, 5].
    # If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
    # If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
    # This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


    ## stone2 
    # Input: piles = [2,7,9,4,4]
    # Output: 10
    # Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, 
    # then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. 
    # If Alex takes two piles at the beginning, then Lee can take all three piles left. 
    # In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
    test1 = [5,3,4,5]
    test2 = [2,7,9,4,4]
    solution = Solution()
    print(solution.stoneGame2(test2))