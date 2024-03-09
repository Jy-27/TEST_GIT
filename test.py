import pyupbit as pu

tickers_ = pu.get_tickers('KRW')
ohlcv_ = pu.get_ohlcv(tickers_[0], interval = 'day', count = 365*10)

print(ohlcv)
