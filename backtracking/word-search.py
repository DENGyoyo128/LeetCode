class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # 频数剪枝 + 反转优化
        cnt_board = Counter(ch for row in board for ch in row)
        cnt_word = Counter(word)
        for ch, c in cnt_word.items():
            if cnt_board[ch] < c:
                return False
        if cnt_board[word[0]] > cnt_board[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, k: int) -> bool:
            # k 表示将匹配 word[k]
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False

            # 原地标记避免重复使用
            tmp = board[r][c]
            board[r][c] = '#'

            # 四方向探索
            found = (
                dfs(r+1, c, k+1) or
                dfs(r-1, c, k+1) or
                dfs(r, c+1, k+1) or
                dfs(r, c-1, k+1)
            )

            # 还原现场
            board[r][c] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False