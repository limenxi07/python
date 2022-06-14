import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('9-data-analysis/pandas-programming-languages/query_results.csv', header=0, names=['DATE', 'TAG', 'POSTS'])
df = df.dropna()
df.DATE = pd.to_datetime(df.DATE)

# greatest number of posts
grouped = df.groupby('TAG').sum()
grouped = grouped.sort_values('POSTS', ascending=False)
print("Number of posts under different programming languages since the creation of Stack Overflow:")
for i in range(1, len(grouped.index)):
  print(f"{i}. {grouped.index[i]} ({grouped['POSTS'][i]} posts)")


# number of months of posts
months = df.groupby('TAG').count()
months = months.sort_values('POSTS', ascending=False)
print("\nNumber of months of posts under different programming languages since the creation of Stack Overflow:")
for i in range(1, len(months.index)):
  print(f"{i}. {months.index[i]} ({months['POSTS'][i]} months)")


# data manipulation by language
languages = df.pivot(index='DATE', columns='TAG', values='POSTS')
languages = languages.fillna(0)
languages = languages.rolling(window=5).mean()
print("Popularity of the top 2 programming language over time")
plt.xlabel('Date')
plt.ylabel('Number of posts')
plt.ylim(0, 35000)
for column in languages.columns:
  plt.plot(languages.index, languages[column], label=languages[column].name)
plt.legend(fontsize=8)
plt.show()