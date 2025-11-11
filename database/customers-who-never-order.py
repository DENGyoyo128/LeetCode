import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 1) 只保留 orders 里用得上的列
    orders_min = orders[['customerId']]

    # 2) 和 customers 做左连接，带上 indicator
    merged = customers.merge(orders_min,left_on='id',right_on='customerId',how='left',indicator=True)

    # 3) 只保留“左表独有”的（表示没下过单）
    never_df = merged.loc[merged['_merge'] == 'left_only', ['name']]

    # 4) 重命名列为 "Customers"
    never_df = never_df.rename(columns={'name': 'Customers'})
    return never_df