
def retweeted(df):
    """
    df.sort_values(by=['retweeted'], ascending=False)
    """
    return df.sort_values(by=['retweetCount'], ascending=False, inplace=False)