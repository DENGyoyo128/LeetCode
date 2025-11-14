class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 1. 统计新鲜橘子数量，并把所有腐烂橘子入队
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # 没有新鲜橘子，0 分钟
        if fresh == 0:
            return 0

        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. 多源 BFS
        while q:
            size = len(q)
            infected = False  # 这一分钟有没有新鲜被感染

            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    # 越界或不是新鲜橘子就跳过
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] != 1:
                        continue

                    # 新鲜橘子变腐烂
                    grid[nx][ny] = 2
                    fresh -= 1
                    infected = True
                    q.append((nx, ny))

            # 这一轮有新鲜橘子被感染，分钟数 +1
            if infected:
                minutes += 1

        # 3. 检查是否还有新鲜橘子
        return minutes if fresh == 0 else -1