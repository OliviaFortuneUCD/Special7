import pandas as pd



pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)
gbvideos = pd.read_csv("GBvideos.csv")

cavideos = pd.read_csv("CAvideos.csv")


myartistGB = gbvideos.loc[gbvideos['channel_title'].str.contains("Cola", case=False)]

myartistCA = cavideos.loc[cavideos['channel_title'].str.contains("Cola", case=False)]

left = myartistCA.set_index(['channel_title'])
right = myartistGB.set_index(['channel_title'])

merged_data= pd.merge(left,right,on='video_id')

print(left[['title', 'likes']])
print(right[['title', 'likes']])
print(merged_data[['title_x', 'likes_x','title_y','likes_y']])