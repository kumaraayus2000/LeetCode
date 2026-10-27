class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        # Initially make every cell an obstacle
        grid = [["#"] * n for _ in range(m)]

        # Step 1:
        # Make the entire top row free
        for col in range(n):
            grid[0][col] = "."

        # Step 2:
        # Make the entire rightmost column free
        for row in range(m):
            grid[row][n - 1] = "."

        # Convert each row from list of chars to string
        result = []

        for row in grid:
            result.append("".join(row))

        return result