import pandas as pd
Worldhappy2019 = pd.read_csv("whap2019.csv")
print(Worldhappy2019)
Worldhappy2020 = pd.read_csv("whap2020.csv")
print(Worldhappy2020)

print(Worldhappy2019[['Country (region)', 'SD of Ladder']])
print(Worldhappy2020[['Country name', 'Ladder score']])