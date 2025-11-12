import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 先按 id 升序，确保每个 email 保留最小 id
    person.sort_values('id', inplace=True)
    # 再按 email 去重，保留第一次出现（也就是最小 id 那行）
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)