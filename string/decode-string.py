class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        cur = []
        st = []  # 栈里放 (之前的字符串list, k)

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)       # 处理多位数
            elif ch == '[':
                st.append((cur, num))          # 入栈保存现场
                cur, num = [], 0               # 开启新一层
            elif ch == ']':
                prev, k = st.pop()             # 出栈恢复现场
                cur = prev + cur * k           # 当前解码重复并拼回
            else:
                cur.append(ch)                 # 普通字母
        return "".join(cur)
        