import pandas as pd
Worldhappy2019 = pd.read_csv("whap2019.csv")
print(Worldhappy2019)
Worldhappy2020 = pd.read_csv("whap2020.csv")
print(Worldhappy2020)



merged_data= pd.merge(Worldhappy2019,Worldhappy2020,on='Country')

print(merged_data.columns)