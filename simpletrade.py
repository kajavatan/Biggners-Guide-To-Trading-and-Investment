import pandas as pd
import matplotlib.pyplot as plt
#get_ipython().magic('matplotlib inline')

ael = pd.read_csv('./data/AEL.N0000/trades.csv')

ael['Trade Date'] = pd.to_datetime(ael['Trade Date'])
#ael = ael.set_index(['Trade Date'])

ael_lastyear = ael.loc[(ael['Trade Date'] > '2020-04-01') & (ael['Trade Date'] <= '2021-06-01')]
print(ael_lastyear.head())
ael_lastyear = ael_lastyear.iloc[::-1]
print(ael_lastyear.head())

ael_lastyear['MA10'] = ael_lastyear['Close (Rs.)'].rolling(10).mean()
ael_lastyear['MA50'] = ael_lastyear['Close (Rs.)'].rolling(50).mean()
ael_lastyear = ael_lastyear.dropna()
ael_lastyear.head()

ael_lastyear['Shares'] = [1 if ael_lastyear.loc[ei, 'MA10']>ael_lastyear.loc[ei, 'MA50'] else 0 for ei in ael_lastyear.index]

ael_lastyear['Close1'] = ael_lastyear['Close (Rs.)'].shift(-1)
ael_lastyear['Profit'] = [ael_lastyear.loc[ei, 'Close1'] - ael_lastyear.loc[ei, 'Close (Rs.)'] if ael_lastyear.loc[ei, 'Shares']==1 else 0 for ei in ael_lastyear.index]
#ael_lastyear['Profit'].plot()
compression_opts = dict(method='zip',archive_name='out.csv')
ael_lastyear.to_csv('out.zip', index=False,compression=compression_opts)
#ael_lastyear = ael_lastyear.iloc[::-1]
ael_lastyear['Close (Rs.)'].plot()
ael_lastyear['MA10'].plot(color="blue")
ael_lastyear['MA50'].plot(color="green")
plt.gca().invert_xaxis()
plt.axhline(y=0, color='red')
plt.show(block=True)