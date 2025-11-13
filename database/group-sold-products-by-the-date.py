import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    #去重，确保同一天同产品只算一次
    tmp = activities.drop_duplicates(['sell_date', 'product'])

    # 按天拿到“排序后的产品列表”
    grp = tmp.groupby('sell_date')['product']
    products_list = grp.apply(lambda s: sorted(s.tolist()))

    # 分别算出三列
    dates = products_list.index
    num_sold = products_list.apply(len)
    products = products_list.apply(lambda lst: ','.join(lst))

    # 新建 DataFrame，把值填进去
    out = pd.DataFrame({
        'sell_date': dates,
        'num_sold': num_sold.values,
        'products': products.values
    }).reset_index(drop=True)


    return out