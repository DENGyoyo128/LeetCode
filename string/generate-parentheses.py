class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #哇，好久不见
        res = []
        def dfs(cur: str, left: int, right: int):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if left < n:
                dfs(cur + "(", left + 1, right)
            if right < left:
                dfs(cur + ")", left, right + 1)
        dfs("", 0, 0)
        return res