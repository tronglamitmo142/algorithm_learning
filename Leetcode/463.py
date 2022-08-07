class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        self.perimeter = 0
        visited = [[False for j in range(col)] for i in range(row)]
        def isValid(x, y):
            return 0 <= x < row and 0 <= y < col 
        def DFS(x, y, grid):
            visited[x][y] = True
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if isValid(xx, yy) and grid[xx][yy] != 0: 
                    if not visited[xx][yy]:
                        DFS(xx, yy, grid)
                else:
                    self.perimeter += 1 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == False:
                    DFS(i, j, grid)
        return self.perimeter

a = Solution()
a.islandPerimeter

