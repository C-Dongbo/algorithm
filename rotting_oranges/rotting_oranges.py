from collections import deque

class Solution:
  def orangesRotting(self, grid):
    row_size, col_size = len(grid), len(grid[0])

    d = 0
    queue = deque()
    for r, row in enumerate(grid):
      for c, val in enumerate(row):
        if val == 2:
          queue.append((r, c, d))

    def get_neighbors(r, c):
      for neighbor_r, neighbor_c in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
        if 0 <= neighbor_r < row_size and 0 <= neighbor_c < col_size:
          yield neighbor_r, neighbor_c

    while queue:
      row, column, d = queue.popleft()
      for neighbor_r, neighbor_c in get_neighbors(row, column):
        if grid[neighbor_r][neighbor_c] == 1:
          grid[neighbor_r][neighbor_c] = 2
          queue.append((neighbor_r, neighbor_c, d + 1))

    for row in grid:
      if 1 in row:
        return -1

    return d

if __name__ == '__main__':
  test = [[2,1,1],[1,1,0],[0,1,1]]
  solution = Solution()
  print(solution.orangesRotting(test))
