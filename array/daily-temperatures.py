class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []  # 存下标，保证 T[st] 递减

        for i, t in enumerate(temperatures):
            # 当前温度更高，解决掉之前更低的日子
            while st and temperatures[st[-1]] < t:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans