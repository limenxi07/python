from tkinter import Y
import pandas as pd
import plotly.express as px

df = pd.read_csv('9-data-analysis/matplotlib-app-store/apps.csv')
df.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(subset=['App', 'Type', 'Price'], inplace=True)

df.Installs = df.Installs.astype(str).str.replace(',', '')
df.Installs = pd.to_numeric(df.Installs)
df.Price = df.Price.astype(str).str.replace('$', '')
df.Price = pd.to_numeric(df.Price)
df = df[df.Price < 250]


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

ct = df.groupby('Category').agg({"Installs": pd.Series.sum, "App": pd.Series.count})
ct.sort_values('Installs', ascending=False, inplace=True)
f2 = px.scatter(ct, x='App', y='Installs', title='Category concentration', size='App', hover_name=ct.index, color='Installs')
f2.update_layout(xaxis_title='Number of apps (lower indicates more concentrated)', yaxis_title='Installs', yaxis=dict(type='log'))

gn = df.Genres.str.split(';', expand=True).stack().value_counts().head(15)
f3 = px.bar(x=gn.index, y=gn.values, title='Top genres', hover_name=gn.index, color=gn.values, color_continuous_scale='Agsunset')
f3.update_layout(xaxis_title='Genre', yaxis_title='Number of apps', coloraxis_showscale=False)

fr = df.groupby(['Category', 'Type'], as_index=False).agg({"App": pd.Series.count})
f4 = px.bar(fr, x='Category', y='App', title='Free vs paid apps by category', color='Type', barmode='group')
f4.update_layout(xaxis_title='Category', yaxis_title='Number of apps', xaxis={'categoryorder': 'total descending'}, yaxis=dict(type='log'))

mn = df[df['Type'] == 'Paid']
f5 = px.box(mn, x='Category', y='Price', title='Price per category')
f5.update_layout(xaxis_title='Category', yaxis_title='Paid app price', xaxis={'categoryorder': 'total descending'}, yaxis=dict(type='log'))

f1.show()
f2.show()
f3.show()
f4.show()
f5.show()