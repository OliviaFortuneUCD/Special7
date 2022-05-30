import pandas as pd
gbvideos = pd.read_csv("GBvideos.csv")
#print(gbvideos)
cavideos = pd.read_csv("CAvideos.csv")
#print(CAvideos)

myartistGB = gbvideos.loc[gbvideos['channel_title'].str.contains("Taylor", case=False)]
print(myartistGB)
myartistCA = cavideos.loc[cavideos['channel_title'].str.contains("Taylor", case=False)]
print(myartistCA)