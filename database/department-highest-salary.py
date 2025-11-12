import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 1) 列重命名，便于最终输出
    emp = employee.rename(columns={'name': 'Employee'})
    dept = department.rename(columns={'id': 'departmentId', 'name': 'Department'})

    # 2) 关联部门名
    df = emp.merge(dept[['departmentId', 'Department']], on='departmentId', how='left')

    # 3) 计算各部门最高薪并筛选
    max_sal = df.groupby('departmentId')['salary'].transform('max')
    out = df.loc[df['salary'] == max_sal, ['Department', 'Employee', 'salary']]

    # 4) 列名
    out = out.rename(columns={'salary': 'Salary'})
    return out