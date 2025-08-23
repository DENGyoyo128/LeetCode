class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n, m = len(s), len(p)
        # if n < m:
        #     return ans
        
        cnt_p = Counter(p)
        cnt_window = Counter(s[:m])

        if cnt_window == cnt_p:
            ans.append(0)

        for i in range(m, n):
            cnt_window[s[i]] += 1         # 加入新字符
            cnt_window[s[i-m]] -= 1       # 移出最左字符
            if cnt_window[s[i-m]] == 0:   # 清理0项，避免无效key
                del cnt_window[s[i-m]]

            if cnt_window == cnt_p:
                ans.append(i - m + 1)

        return ans