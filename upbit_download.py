import pyupbit as pu
import pandas as pd
import os


def download_data(year :int=10):
    directory_ = os.getcwd()
    folder_name_ = 'upbit'
    path_ = os.path.join(directory_, folder_name_)
    
    bool_exists_ = os.path.exists(path_)
    
    if bool_exists_ == False:
        os.mkdir(path)
    elif bool_exists_ == True:
        pass
    
    tickers_ = pu.get_tickers('KRW')
    print('Ticker loading complete')
    
    for ticker in tickers_:
        ohlcv_ = pu.get_ohlcv(ticker=ticker, interval='day', count=365 * year)
        file_name = str(ticker.split('-')[1]) +  '.csv'
        save_path =  os.path.join(path_, file_name)
        ohlcv_.to_csv(save_path)
        print(f'{ticker} loading complete!')

    print('All download complete!')

if __name__ == "__main__":
    download_data()