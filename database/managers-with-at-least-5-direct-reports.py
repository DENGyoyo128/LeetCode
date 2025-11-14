import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. 统计每个 managerId 有多少下属
    counts = employee["managerId"].value_counts()

    # 2. 找到拥有至少 5 个直接下属的 managerId
    mgr_ids = counts[counts >= 5].index

    # 3. 在 employee 里找出这些 manager 本人（id 在 mgr_ids 里面）
    result = employee[employee["id"].isin(mgr_ids)]

    # 4. 题目只要 name 这一列
    return result[["name"]]