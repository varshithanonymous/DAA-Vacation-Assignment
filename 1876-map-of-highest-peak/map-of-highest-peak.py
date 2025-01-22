from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]  # Initialize heights with -1
        queue = deque()

        # Initialize the queue with all water cells and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        # Directions for north, east, south, west
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS to assign heights
        while queue:
            x, y = queue.popleft()
            current_height = height[x][y]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = current_height + 1
                    queue.append((nx, ny))

        return height
