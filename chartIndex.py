import ccxt
import requests
import datetime
import FinanceDataReader as fdr
from pytrends.request import TrendReq #https://pypi.org/project/pytrends/
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pandas_datareader import data as pdr
from datetime import datetime

keyword = 'ethereum' #body = '''{"startDate":"2021-07-01", "endDate":"2021-08-05","timeUnit":"date","keywordGroups":[{"groupName":"cryptocurrency","keywords":["ethereum","bitcoin"]}]}'''

period = 'today 1-m'

trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword], timeframe=period)


trend_df = trend_obj.interest_over_time()
print(trend_df.head())

# def df_1(S0, K, r, sigma, T, q):
#        return (np.log(S0 / K) + (r - q + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))

# def df_2(S0, K, r, sigma, T, q):
#        return (np.log(S0 / K) + (r - q - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))

plt.style.use('ggplot')
plt.figure(figsize=(14,5))
trend_df['ethereum'].plot()
plt.title("ethereum", size=15)
plt.legend(labels=['ethereum'], loc='upper left')

df = fdr.DataReader('BTC/KRW', '2021-07-05', '2021-08-05')
df_1 = fdr.DataReader('ETH/KRW', '2021-07-05', '2021-08-05')
df_2 = fdr.DataReader('XRP/KRW', '2021-07-05', '2021-08-05')


config = {'title':'ETH',
          'width': 830,
          'height': 300,
          'volume': True,
}

fdr.chart.config(config=config)
fdr.chart.plot(df)