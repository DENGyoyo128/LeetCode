import pandas as pd

# def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
#     if employees['employee_id'] %2=1 and employees['name'][:1]!='M':
#         employees['bonus']=employees['salary']
#     else:
#         employees['bonus']=0
#     return employees


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # 条件：ID 为奇数 且 姓名不以 'M' 开头
    mask = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))

    out = employees[['employee_id']].copy()
    out['bonus'] = np.where(mask, employees['salary'], 0).astype(int)

    return out.sort_values('employee_id')