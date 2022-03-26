import pandas as pd

def users(df):

  return df.groupby('username')['username'].count().reset_index(name='count').sort_values(by='count', ascending=False)