import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # 1) 过滤 author_id == viewer_id 的记录（自己看自己）
    self_view = views[views['author_id'] == views['viewer_id']]
    # 2) 只保留作者的 id 列，并去重
    result = self_view[['author_id']].drop_duplicates()
    # 3) 按照题目风格把列名改为 'id'
    result = result.rename(columns={'author_id': 'id'}).sort_values('id')
    return result