class Solution:
    def matrixBlockSum(self, mat, K):
        m = len(mat)
        n = len(mat[0])
        memo = [[0]*n for i in range (m)]
        result = [[0]*n for i in range (m)]
#        memo = mat

        for i in range(m):
            memo[i][0] = mat[i][0]
        
        for i in range(0,m):
            for j in range(1,n):
                memo[i][j] = mat[i][j]+memo[i][j-1]

        for i in range(1,m):
            for j in range(0,n):
                memo[i][j]+=memo[i-1][j]

        for i in range(m):
            for j in range(n):

                left_i = max(0, i-K)
                left_j = max(0, j-K)

                right_i = min(m-1, i+K)
                right_j = min(n-1, j+K)



                result_val = memo[right_i][right_j]

                if left_i > 0:
                    result_val = result_val - memo[left_i - 1][right_j] 
                if left_j > 0: 
                    result_val = result_val - memo[right_i][left_j - 1] 

                result[i][j] = result_val


        return result

if __name__=='__main__':
    test = [[1,2,3],[4,5,6],[7,8,9]] 
    K = 2
    solution = Solution()
    print(solution.matrixBlockSum(test,K))
    