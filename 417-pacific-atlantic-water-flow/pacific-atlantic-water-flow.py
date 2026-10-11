class Solution:

    def dfs(self, heights, x, y, visited):

        rows = len(heights)
        cols = len(heights[0])

        # Boundary check
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return

        # Already visited
        if (x, y) in visited:
            return

        visited.add((x, y))

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]

        for dx, dy in directions:

            new_x = x + dx
            new_y = y + dy

            # Boundary check
            if (
                new_x < 0 or
                new_y < 0 or
                new_x >= rows or
                new_y >= cols
            ):
                continue

            # Already visited
            if (new_x, new_y) in visited:
                continue

            # Reverse water flow:
            # move only to same or higher height
            if heights[new_x][new_y] < heights[x][y]:
                continue

            self.dfs(
                heights,
                new_x,
                new_y,
                visited
            )


    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        # Safety check
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        # Pacific = TOP + LEFT
        for col in range(cols):
            self.dfs(heights, 0, col, pacific)

        for row in range(rows):
            self.dfs(heights, row, 0, pacific)

        # Atlantic = BOTTOM + RIGHT
        for col in range(cols):
            self.dfs(heights, rows - 1, col, atlantic)

        for row in range(rows):
            self.dfs(heights, row, cols - 1, atlantic)

        result = []

        # Must be reachable from BOTH oceans
        for x in range(rows):
            for y in range(cols):

                if (x, y) in pacific and (x, y) in atlantic:
                    result.append([x, y])

        return result