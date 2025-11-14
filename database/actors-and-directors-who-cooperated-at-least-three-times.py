import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    pair=actor_director.groupby(["actor_id","director_id"],as_index=False).nunique()
    pair=pair.loc[pair["timestamp"]>=3,["actor_id","director_id"]]
    return pair