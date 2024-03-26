import time
import pyupbit as pu
import pandas as pd

class StopLoss:
    """손절가를 지정한다. High값의 기준으로 (-)LossPercent가격을 손절가로 지정한다."""
    def __init__(self, High :float = 0, LossPercent :float = 0.05) -> None:
        self.High = High
        self.LossPercent = LossPercent
    def HighUpdate(self, Price :float) -> None:
        if self.High < Price:
            self.High = Price
    def LossPercentUpdate(self, Percent :float) -> None:
        self.LossPercent = Percent
    def StopLoss(self) -> float:
        Price_ = self.High - (self.High * self.LossPercent)
        Price_ = pu.get_tick_size(Price_)
        return Price_

class Ticker():
    def __init__(self):
        self.info = pu.get_tickers(fiat='KRW', is_details=True)
        self.Safty = [ticker['market'] for ticker in self.info if ticker['market_warning'] == 'NONE']
        self.Danger = [ticker['market'] for ticker in self.info if ticker['market_warning'] != 'NONE']
    def Filter(self, Satus :str='Safty', Value :str="75%"):
        if Satus == 'Safty':
            """거래종료 예정없는 티켓 리스트"""
            price_ = pu.get_current_price(self.Safty, verbose=True)
        elif Satus == 'Danger':
            """거래종료 예정이 있는 티켓 리스트"""
            price_ = pu.get_current_price(self.Danger, verbose=True)
        df_ = pd.DataFrame(price_)
        describe_ = df_.describe()
        try:
            value_ = describe_.loc[Value]['acc_trade_price_24h']
            result = list(df_.loc[df_.acc_trade_price_24h >= value_]['market'])
            return result
        except KeyError:
            print('empty data')
            return None 

"""
class를 활용해서 웹소켓 데이터를 누적하고
판다스 데이터로 전환 후 일정 시간(예 : 1시간)이 지난 데이터는
Remove처리한다.

1시간의 데이터를 기준으로 작성

class를 활용하여 OHLCV 데이터를 수집하고
describe()를 사용한다.

최빈값 찾은 후 

"""


# if __name__ == "__main__":
#     tickers_ = Tickers()
#     print(Tickers.safety())
