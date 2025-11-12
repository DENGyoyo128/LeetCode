import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    out = scores.copy()
    out["rank"] = out["score"].rank(method="dense", ascending=False).astype(int)
    return out[["score", "rank"]].sort_values("score", ascending=False)