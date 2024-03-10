import ohlcv_csv_load as load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import graph_hangle as gh


df_load_ = load.load()
tickers_ = [x for x in df_load_.keys()]

def compare(first :str='BTC', second :str='ETH', year :int=10):
    
    df_1 = pd.read_csv(os.path.join(os.getcwd(), 'upbit', f'{first}.csv'))
    df_2 = pd.read_csv(os.path.join(os.getcwd(), 'upbit', f'{second}.csv'))
    df_1.rename(columns={df_1.columns[0] : 'Date'}, inplace=True)
    df_1.set_index(df_1.columns[0], inplace=True)
    df_2.rename(columns={df_2.columns[0] : 'Date'}, inplace=True)
    df_2.set_index(df_2.columns[0], inplace=True)

    index_1 = df_1.index[0]
    index_2 = df_2.index[0]

    if index_1 > index_2:
        df_2 = df_2.loc[index_1:]
    elif index_1 < index_2:
        df_1 = df_1.loc[index_2:]
    elif index_1 == index_2:
        pass

    date_start = df_1.index[0].split(' ')[0]
    
    scaler = MinMaxScaler()
    df_1 = pd.DataFrame(scaler.fit_transform(df_1), columns=df_1.columns)
    df_2 = pd.DataFrame(scaler.fit_transform(df_2), columns=df_2.columns)
    df_1['date'] = pd.date_range(start=date_start, periods=len(df_1), freq='D')
    df_2['date'] = pd.date_range(start=date_start, periods=len(df_2), freq='D')

    plt.figure(figsize=(10, 6))
    plt.plot(df_1.date, df_1.close, label=first, color='red')
    plt.plot(df_2.date, df_2.close, label=second, color='blue')
    
    plt.xlabel('date (Year)')
    plt.ylabel('Scaled Values (Percent)')
    plt.legend()
    plt.title(f'{first} vs {second}')
    plt.show()