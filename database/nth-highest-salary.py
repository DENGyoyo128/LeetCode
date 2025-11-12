import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 取不同工资，按降序
    s = employee['salary'].drop_duplicates().sort_values(ascending=False)
    val = s.iloc[N-1] if len(s) >= N and N>0 else np.nan  # 不足 n 个则返回 NaN (等价于 SQL 的 NULL)
    return pd.DataFrame({f'getNthHighestSalary({N})': [val]})

    # s = employee['salary'].drop_duplicates().nlargest(n)
    # val = s.iloc[-1] if len(s) == n else np.nan
    # return pd.DataFrame({'NthHighestSalary': [val]})





