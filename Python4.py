import pandas as pd
gbvideos = pd.read_csv("GBvideos.csv")

cavideos = pd.read_csv("CAvideos.csv")


myartistGB = gbvideos.loc[gbvideos['channel_title'].str.contains("Taylor", case=False)]

myartistCA = cavideos.loc[cavideos['channel_title'].str.contains("Taylor", case=False)]

left = myartistCA.set_index(['channel_title'])
right = myartistGB.set_index(['channel_title'])

merged_data= pd.merge(left,right,on='video_id')
print(left.columns, right.columns)
print(merged_data.columns)