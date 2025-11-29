class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(index: int, path: str):
            # index 表示当前处理到第几位 digit
            if index == len(digits):
                # 所有位置都选完了，path 是一个完整的组合
                res.append(path)
                return

            cur_digit = digits[index]
            for ch in phone[cur_digit]:
                # 选当前 digit 对应的一个字母，进入下一位
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return res