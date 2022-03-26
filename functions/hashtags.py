from asyncio.windows_events import NULL
import pandas as pd
import re

def hashtags(df):

  hashtags = []
  hashtags_names = []

  for text in df['content']:
    
    txt_tags = re.findall("#(\w+)", text)

    for tag in txt_tags:
      if tag not in hashtags_names:
        hashtags_names.append(tag)
        newtag = {'hashtag': tag, 'count': 1}
        hashtags.append(newtag)
      else:
        for ht in hashtags:
          if ht['hashtag'] == tag:
            ht['count'] += 1
            break

  top_tags = pd.DataFrame.from_dict(hashtags)

  return top_tags.sort_values(by='count', ascending=False)