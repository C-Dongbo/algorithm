
class BackTracking:
    def findNQueen(self, row, n):
        count = 0
        def dfs(column, row):

            def isPossible(column, row):
                for i in range(row):
                    if column[i] == column[row]:
                        return False
                    if abs(i - row) == abs(column[i]- column[row]):
                        return False
                return True

            if row == n:
                count += 1
            else:
                for i in range(n):
                    column[row+1]=i
                    if isPossible(column, row+1):
                        dfs(column, row+1)
                    else:
                        column[row+1] = 0
            column[row] = 0
        
        for i in range(n):
            column = []
            column.append(i)


            dfs(column, row)
        return count      



if __name__ =='__main__':
    n = 5
    count = 0
