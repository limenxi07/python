import pandas as pd
import matplotlib.pyplot as plt

# colours analysis
df = pd.read_csv('9-data-analysis/pandas-lego-sets/data/colors.csv')
df = df.dropna()
print(f"COLOURS ANALYSIS\nNumber of unique LEGO colours: {df.nunique()['name']}")
print(f"Number of transparent LEGO colours: {df['is_trans'].value_counts()['t']}")


# sets analysis
df = pd.read_csv('9-data-analysis/pandas-lego-sets/data/sets.csv')
df = df.dropna()
df = df.sort_values('year')
release_year = df.iloc[0]['year']
print(f"\nSETS ANALYSIS\nThe first LEGO sets were released in {release_year}. The first set was called the {df.iloc[0]['name']}.")
print(f"In their first year of operation, the LEGO company sold {df['year'].value_counts()[release_year]} different products.")
df = df.sort_values('num_parts', ascending=False)
print("The top 5 LEGO sets with the most number of parts:")
for i in range(1, 6):
  row = df.iloc[i-1]
  print(f"{i}. {row['name']} ({row['year']}) - {row['num_parts']} parts")