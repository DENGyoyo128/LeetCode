import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values('salary').drop_duplicates()
    second=employee.iloc[1:2]
    out=second[['salary']].rename(columns={'salary':'SecondHighestSalary'})
    if out.empty:
        out = pd.DataFrame({'SecondHighestSalary': [None]})
    return out[['SecondHighestSalary']]
    # s = employee['salary'].drop_duplicates().nlargest(2)
    # val = s.iloc[-1] if len(s) == 2 else None  # 不足两种工资 -> None(显示为 NaN)
    # return pd.DataFrame({'SecondHighestSalary': [val]})

    