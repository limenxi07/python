import pandas as pd
df = pd.read_csv('9-data-analysis/college-major-salary/salaries_by_college_major.csv')
df = df.dropna()
pd.options.display.float_format = '{:,.2f}'.format

# highest/lowest earning degrees
max_mid = df['Mid-Career Median Salary'].idxmax()
print(f"College major with the highest mid-career salary: {df['Undergraduate Major'][max_mid]} (${df['Mid-Career Median Salary'][max_mid]})")

min_start = df['Starting Median Salary'].idxmin()
print(f"College major with the lowest starting salary: {df['Undergraduate Major'][min_start]} (${df['Starting Median Salary'][min_start]})")

min_mid = df['Mid-Career Median Salary'].idxmin()
print(f"College major with the lowest mid-career salary: {df['Undergraduate Major'][min_mid]} (${df['Mid-Career Median Salary'][min_mid]})")


# degrees with high potential
df.insert(1, 'Spread', df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary'])
sorted = df.sort_values('Spread')
print("\nTop 5 majors with the highest values in the 90th percentile:")
for i in range(1, 6):
  print(f"{i}. {sorted['Undergraduate Major'][i]} (${sorted['Mid-Career 90th Percentile Salary'][i]})")

sorted = df.sort_values('Spread', ascending=False)
print("\nTop 5 majors with the largest difference between high and low earners after graduation:")
for i in range(1, 6):
  print(f"{i}. {sorted['Undergraduate Major'][i]} (${sorted['Starting Median Salary'][i]})")


# average salary by group
avg = df.groupby('Group').mean()
avg = avg.sort_values('Spread', ascending=False)
print('\nCategory of degrees with the highest average salary:\n', avg)