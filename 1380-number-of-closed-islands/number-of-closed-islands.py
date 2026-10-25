class Solution:

    def dfs(self, grid, x, y, vis):

        rows = len(grid)
        cols = len(grid[0])

        # If we go outside the grid,
        # this island touched the boundary,
        # so it is NOT closed.
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return False

        # Water does not affect whether island is closed.
        if grid[x][y] == 1:
            return True

        # Already visited land.
        if vis[x][y]:
            return True

        # Mark current land cell visited.
        vis[x][y] = True

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]

        is_closed = True

        for dx, dy in directions:

            new_x = x + dx
            new_y = y + dy

            # If ANY direction reaches outside,
            # entire island is not closed.
            if not self.dfs(grid, new_x, new_y, vis):
                is_closed = False

        return is_closed


    def closedIsland(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        vis = [[False] * cols for _ in range(rows)]

        count = 0

        for i in range(rows):
            for j in range(cols):

                # Start DFS only from
                # unvisited LAND cells.
                if grid[i][j] == 0 and not vis[i][j]:

                    # If DFS confirms this island
                    # never reaches boundary,
                    # then it is a closed island.
                    if self.dfs(grid, i, j, vis):
                        count += 1

        return count