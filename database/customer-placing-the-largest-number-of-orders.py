import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cnt=orders.groupby("customer_number",as_index=False)["order_number"].nunique()
    mx = cnt["order_number"].max()

    # 3) 保留并列最大者，取最小 customer_number，按题目只返回一行一列
    winner = cnt.loc[cnt["order_number"] == mx, "customer_number"].min()
    return pd.DataFrame({"customer_number": [winner]})