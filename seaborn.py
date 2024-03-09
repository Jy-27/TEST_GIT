import seaborn as sns
import graph_hangle as gh
import pyupbit as pu
import pandas as pd


def data(ticker :str='KRW-BTC'):
    df_ = pu.get_ohlcv(ticker = 'KRW-BTC', interval='day', count=3_650)
    sns.set(font='AppleGothic',
            rc={'axes.unicode_minus':False,
                'figure.figsize':(15,5)},
            style='white')
    ax = sns.lineplot(data = df_,
                      x = df_.index,
                      y = 'close')
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    ax.legend(['Close'])
    ax.set_title(ticker)
    plt.show()

tickers = pu.get_tickers('KRW')

for ticker in tickers:
    data(ticker)