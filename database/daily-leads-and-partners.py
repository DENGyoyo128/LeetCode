import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result1=daily_sales.groupby(["date_id","make_name"])["lead_id"].nunique()
    result2=daily_sales.groupby(["date_id","make_name"])["partner_id"].nunique()
    # 用 concat 按列拼起来，索引是 MultiIndex (date_id, make_name)
    result = pd.concat([result1,result2], axis=1)
    # 重命名列名
    result.columns = ["unique_leads", "unique_partners"]

    # 把索引还原成普通列
    result = result.reset_index()
    return result
