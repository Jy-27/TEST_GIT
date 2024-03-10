import seaborn as sns
import graph_hangle as gh
import pyupbit as pu
import pandas as pd
import matplotlib.pyplot as plt

def compare(ticker_1 :str='KRW-BTC', ticker_2 :str='KRW-ETH', year :int=10):
    df_1 = pu.get_ohlcv(ticker=ticker_1, interval='day', count=365*year)
    df_2 = pu.get_ohlcv(ticker=ticker_2, interval='day', count=365*year)

    index_1 = df_1.index[0]
    index_2 = df_2.index[0]

    if index_1 > index_2:
        df_2 = df_2.loc[index_1:]
    elif index_1 < index_2:
        df_1 = df_1.loc[index_2:]
    elif index_1 == index_2:
        pass
        
    scaler = MinMaxScaler()
    df_1 = pd.DataFrame(scaler.fit_transform(df_1), columns=df_1.columns)
    df_2 = pd.DataFrame(scaler.fit_transform(df_2), columns=df_2.columns)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_1.index, df_1.close, label=ticker_1, color='red')
    plt.plot(df_2.index, df_2.close, label=ticker_2, color='blue')
    
    plt.xlabel('date')
    plt.ylabel('Scaled Values')
    plt.legend()
    plt.title(f'{ticker_1} vs {ticker_2}')
    plt.show()