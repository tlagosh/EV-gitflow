
def users(df):

  return df.groupby(['user'])['id'].count().reset_index(user='Count').sort_values(['Count'], ascending=False)