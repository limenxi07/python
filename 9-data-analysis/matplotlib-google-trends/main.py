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


# DATA VISUALISATION - TESLA
plt.figure(1, figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
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


# DATA VISUALISATION - BITCOIN
plt.figure(2, figsize=(14, 8), dpi=120)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
ax3 = plt.gca()
ax4 = ax3.twinx()
ax3.set_xlabel('Year', fontsize=14)
ax3.set_ylabel('BTC price', color='orange', fontsize=14)
ax4.set_ylabel('Search trend', color='skyblue', fontsize=14)
ax3.set_xlim([df_btc_price.index.min(), df_btc_price.index.max()])
ax3.set_ylim([0, 15000])
ax3.plot(df_btc_price.index, df_btc_price.CLOSE, 'orange', linestyle='--')
ax4.plot(df_btc_price.index, df_btc_search.BTC_NEWS_SEARCH, 'skyblue', marker='o')

plt.xticks(fontsize=14, rotation=45)
ax3.xaxis.set_major_locator(years)
ax3.xaxis.set_minor_locator(months)
ax3.xaxis.set_major_formatter(years_format)


# DATA VISUALISATION - UNEMPLOYMENT
plt.figure(3, figsize=(14, 8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
ax5 = plt.gca()
ax6 = ax5.twinx()
ax5.grid(color='grey', linestyle='--')
ax5.set_xlabel('Year', fontsize=14)
ax5.set_ylabel('FRED U/E rate', color='purple', fontsize=14)
ax6.set_ylabel('Search trend', color='skyblue', fontsize=14)
ax5.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
ax5.set_ylim([3, 10.5])
ax5.plot(df_unemployment.MONTH, df_unemployment.UNRATE, 'purple', linestyle='--')
ax6.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, 'skyblue')

plt.xticks(fontsize=14, rotation=45)
ax5.xaxis.set_major_locator(years)
ax5.xaxis.set_minor_locator(months)
ax5.xaxis.set_major_formatter(years_format)

plt.show()