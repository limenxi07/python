import pandas as pd
df = pd.read_csv('9-data-analysis/programming-languages/query_results.csv', header=0, names=['DATE', 'TAG', 'POSTS'])
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