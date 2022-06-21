import pandas as pd
import plotly.express as px

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


# DATA VISUALISATION - PLOTLY
rt = df.Content_Rating.value_counts()
f1 = px.pie(labels=rt.index, values=rt.values, title='Content Rating', names=rt.index, hole=0.6)
f1.update_traces(textposition='inside', textinfo='percent', textfont_size=15)
f1.show()