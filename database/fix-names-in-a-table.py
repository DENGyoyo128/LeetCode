import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    s=users["name"]
    fixed = s.str[:1].str.upper() + s.str[1:].str.lower()
    out = users.copy()
    out["name"] = fixed
    return out[["user_id", "name"]].sort_values("user_id")