import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#retrieve data from csv
ael = pd.read_csv('./data/AEL.N0000/trades.csv')
print(ael.head())
#print(ael.describe())

ael['Trade Date'] = pd.to_datetime(ael['Trade Date'])
#ael = ael.set_index(['Trade Date'])

#extract one year data
ael_lastyear = ael.loc[(ael['Trade Date'] > '2020-06-01') & (ael['Trade Date'] <= '2021-06-01')]

print(ael_lastyear.head())
print(ael_lastyear.tail())
print(ael_lastyear.describe())


#Calculating the log returns and Value of Rs 100 invested
ael_lastyear['logClose'] = np.log(ael_lastyear['Close (Rs.)'])
ael_lastyear['log_return'] = ael_lastyear['logClose'].diff(-1)
annual_logreturn = ael_lastyear['log_return'].sum()

print(ael_lastyear.describe())
print('Annual Log Return')
print(annual_logreturn)

print('Value of Rs 100 invested:')
print(np.exp(annual_logreturn)*100)

#percentage change return
ael_lastyear_daily_returns = ael_lastyear['Close (Rs.)'].pct_change(-1)
annual_return = np.prod(ael_lastyear_daily_returns+1)-1

print('Annual return')
print(annual_return)

#Risk Adjusted Return (Sharp Ratio)
std = ael_lastyear_daily_returns.std();
Sharp_Ratio = ael_lastyear_daily_returns.mean()/std * np.sqrt(252)
print('Sharp Ratio')
print(Sharp_Ratio)

#Max Draw down
# We are going to use a trailing 252 trading day window
window = 252
temp = ael_lastyear['Close (Rs.)']
temp = temp.iloc[::-1]
Roll_Max = temp.rolling(window, min_periods=1).max()
Daily_Drawdown = temp/Roll_Max - 1.0
Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()
print('Max Daily Drawdown')
print(Max_Daily_Drawdown.min())

#JB - jarque bera
print('jarque bera')
print(stats.jarque_bera(ael_lastyear_daily_returns))
print('skew')
print(ael_lastyear_daily_returns.skew())
print('Kurtosis')
print(ael_lastyear_daily_returns.kurtosis())

#Semi Deviation
print('Semi Deviation')
print(ael_lastyear_daily_returns[ael_lastyear_daily_returns<0].std(ddof=0))

#Liqudity for 10000 stocks and average daile volume for 1 month)
ael_lastmonth = ael.loc[(ael['Trade Date'] > '2021-05-01') & (ael['Trade Date'] <= '2021-06-01')]
average_share_volume = ael_lastmonth['Share Volume'].mean()
alpha = 0.1
order_size = 10000
liqudity_horizon = order_size/(average_share_volume*alpha)
print('Liquidity for 10000 shares')
print(liqudity_horizon)

#VaR
#std
#mean = ael_lastyear_daily_returns.mean();
VaR_95 = ael_lastyear_daily_returns.quantile(0.05)
print('Var 95')
print(VaR_95)

#CVaR
CVaR_95 = ael_lastyear_daily_returns[ael_lastyear_daily_returns <= VaR_95].mean()
print('CVaR 95')
print(CVaR_95)
#print(average_turnover)