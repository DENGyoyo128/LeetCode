class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        return True if not stack else False


        # if len(s) % 2 == 1:
        # return False  # 奇数长度不可能有效

        # pairs = {')': '(', ']': '[', '}': '{'}
        # stack = []

        # for ch in s:
        #     if ch in "([{":
        #         stack.append(ch)
        #     else:
        #         if not stack or stack[-1] != pairs.get(ch):
        #             return False
        #         stack.pop()

        # return not stack