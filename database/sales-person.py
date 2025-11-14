import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
     # 找出公司名为 "RED" 的 com_id
    red_com_ids = company.loc[company["name"] == "RED", "com_id"]

    # 找出所有给 RED 下过单的 sales_id
    red_sales_ids = orders.loc[orders["com_id"].isin(red_com_ids), "sales_id"].unique()

    # 从销售人员里剔除这些人
    return sales_person[~sales_person["sales_id"].isin(red_sales_ids)][["name"]]