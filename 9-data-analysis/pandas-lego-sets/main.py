import pandas as pd
import matplotlib.pyplot as plt

# colours analysis
cl = pd.read_csv('9-data-analysis/pandas-lego-sets/data/colors.csv')
cl = cl.dropna()
print(f"COLOURS ANALYSIS\nNumber of unique LEGO colours: {cl.nunique()['name']}")
print(f"Number of transparent LEGO colours: {cl['is_trans'].value_counts()['t']}")


# sets analysis
df = pd.read_csv('9-data-analysis/pandas-lego-sets/data/sets.csv')
st = df.dropna()
st = st.sort_values('year')
release_year = st.iloc[0]['year']
print(f"\nSETS ANALYSIS\nThe first LEGO sets were released in {release_year}. The first set was called the {st.iloc[0]['name']}.")
print(f"In their first year of operation, the LEGO company sold {st['year'].value_counts()[release_year]} different products.")
st = st.sort_values('num_parts', ascending=False)
print("The top 5 LEGO sets with the most number of parts:")
for i in range(1, 6):
  row = st.iloc[i-1]
  print(f"{i}. {row['name']} ({row['year']}) - {row['num_parts']} parts")


# sets over time analysis
stt = st.groupby('year').count()
sets = pd.Series(index=stt.index, data=stt['name'])
plt.figure(0)
ax1 = plt.gca()
ax1.plot(sets.index[:-2], sets[:-2], 'g')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of sets', color='green')

themes = df.groupby('year').agg({'theme_id': pd.Series.nunique})
themes.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
ax2 = ax1.twinx()
ax2.plot(themes.index[:-2], themes['nr_themes'][:-2], 'b')
ax2.set_ylabel('Number of themes', color='blue')

fig2, ax3 = plt.subplots()
parts = df.groupby('year').agg({'num_parts': pd.Series.mean})
parts.rename(columns={'num_parts': 'avg_num_parts'}, inplace=True)
plt.figure(1)
plt.scatter(parts.index[:-2], parts.avg_num_parts[:-2])

plt.show()