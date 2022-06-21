import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9-data-analysis/matplotlib-app-store/apps.csv')
df.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(subset=['App', 'Type', 'Price'], inplace=True)


# BASIC ANALYSIS
df.sort_values('Reviews', ascending=False)
print('Highest rated apps:')
for i in range(1, 6):
  row = df.iloc[i-1]
  print(f'{i}. {row["App"]} ({row["Rating"]} rating)')

df.sort_values('Size_MBs', ascending=False)
print(f'Largest app: {df.iloc[0]["App"]} ({df.iloc[0]["Size_MBs"]} MB)')

