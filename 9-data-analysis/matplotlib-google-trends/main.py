from atexit import register
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mds
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df_tesla = pd.read_csv('9-data-analysis/matplotlib-google-trends/TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('9-data-analysis/matplotlib-google-trends/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('9-data-analysis/matplotlib-google-trends/Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('9-data-analysis/matplotlib-google-trends/UE Benefits Search vs UE Rate 2004-19.csv')

df_btc_price.dropna(inplace=True)
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price = df_btc_price.resample('M', on='DATE').last() # converts daily data into monthly data (using the price at month-end)


# DATA VISUALISATION
plt.figure(1, figsize=(14, 8), dpi=120)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('TSLA stock price', color='red', fontsize=14)
ax2.set_ylabel('Search trend', color='blue', fontsize=14)
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
ax1.set_ylim([0, 600])
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, 'r')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, 'b')

years = mds.YearLocator()
months = mds.MonthLocator()
years_format = mds.DateFormatter('%Y')
plt.xticks(fontsize=14, rotation=45)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_format)

plt.show()