from binance import Client
import datetime

from typing import List

from currency.local.daily_data_point import DailyDataPoint
from currency.local.coin_data import CoinData


class BinanceService:

    def __init__(self, api_key: str, secret_key: str):
        self.client = Client(api_key=api_key, api_secret=secret_key)

    def get_usdt_tickers(self):
        tickers = self.client.get_all_tickers()

        def usdt_filter(ticker):
            symbol = ticker.get("symbol")
            if "USDT" in symbol[-4:]:
                if "DOWNUSDT" not in symbol and "UPUSDT" not in symbol:
                    return True

            return False

        usdt_tickers = list(filter(usdt_filter, tickers))
        return [x.get("symbol") for x in usdt_tickers]

    def get_data(self, ticker):
        historical = self.get_daily_one_year_historical(ticker=ticker)
        today = self.get_todays_data(ticker=ticker)
        return CoinData(ticker=ticker, today=today, historical=historical)

    def get_daily_one_year_historical(self, ticker) -> List[DailyDataPoint]:
        one_year_ago = datetime.date.today() - datetime.timedelta(days=365)
        one_year_ago_format = one_year_ago.strftime("%d %b, %Y")
        hd = self.client.get_historical_klines(ticker, Client.KLINE_INTERVAL_1DAY, one_year_ago_format)
        return [DailyDataPoint(data=x) for x in hd]

    def get_todays_data(self, ticker):
        return self.client.get_ticker(symbol=ticker)
