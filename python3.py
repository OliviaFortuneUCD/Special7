import pandas as pd
gbvideos = pd.read_csv("GBvideos.csv")

cavideos = pd.read_csv("CAvideos.csv")


myartistGB = gbvideos.loc[gbvideos['channel_title'].str.contains("Taylor", case=False)]

myartistCA = cavideos.loc[cavideos['channel_title'].str.contains("Taylor", case=False)]

left = myartistCA.set_index(['title', 'trending_date'])
right = myartistGB.set_index(['title', 'trending_date'])
merged_data= pd.merge(left,right,on='video_id')
print(merged_data)