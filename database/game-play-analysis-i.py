import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result=activity.sort_values(["player_id","event_date"])
    result=result.drop_duplicates(subset=["player_id"])
    result=result.rename(columns={"event_date":"first_login"})
    result=result[["player_id","first_login"]]
    return result