import pandas as pd
import matplotlib.pyplot as plt

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
