class Solution:
    def countBits(self, num: int):

        if num == 0:
            return [0]  
    
        dp = [0]*(num+1)
        dp[0] = 0
        dp[1] = 1
        
        j = 1
        for i in range(2, num+1):
            if i%2 == 0:
                dp[i] = dp[i-j]
            else:
                dp[i] = 1+dp[i-j-1]
                j+=1
                

        return dp




if __name__=='__main__':
    test = 7
    solution = Solution()
    print(solution.countBits(test))