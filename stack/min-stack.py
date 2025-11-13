class MinStack:

    def __init__(self):
        self.st = []       # 主栈：存元素
        self.min_st = []   # 最小栈：存到当前为止的最小值

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val <= self.min_st[-1]:
            self.min_st.append(val)
        else:
            # 也可只在更小或相等时压入；这里为了 O(1) getMin，也可以重复顶
            self.min_st.append(self.min_st[-1])

    def pop(self) -> None:
        self.st.pop()
        self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()