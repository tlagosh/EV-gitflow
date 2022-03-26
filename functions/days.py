
def days(df):
  
  return df.groupby('day')['day'].count().reset_index(name='count').sort_values(by='count', ascending=False)