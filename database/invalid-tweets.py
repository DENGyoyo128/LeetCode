import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # tweets["str_length"]=len(tweets["content"].str())
    tweets["str_length"]=tweets["content"].str.len()
    select=(tweets["str_length"]>15)
    result=tweets.loc[select,["tweet_id"]]
    return result