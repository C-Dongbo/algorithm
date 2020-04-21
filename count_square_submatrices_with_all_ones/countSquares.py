class Solution:
    def countSquares(self, matrix):

#       initialize        

        row = len(matrix)
        column = len(matrix[0])
        memo = [[0]*column for i in range (row)]
            
        result = 0
        
        for i in range(0, row):
            memo[i][0] = matrix[i][0]
            if matrix[i][0] == 1:
                result += 1
                
        for i in range(1, column):
            memo[0][i] = matrix[0][i] 
            if matrix[0][i] == 1:
                result += 1
                
        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j] == 1:
                    memo[i][j] = 1 + min(memo[i-1][j-1], memo[i-1][j], memo[i][j-1])
                    result += memo[i][j]
                    
        return result


        # result = 0
        # for row in matrix:
        #     result += sum(row)

        # return result




if __name__=='__main__':
    solution = Solution()
    test = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]
    print(solution.countSquares(test))