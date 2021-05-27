import os
import pandas as pd
from local.binance_service import BinanceService

if __name__ == '__main__':
    bs = BinanceService(api_key=os.environ.get('BINANCE_API_KEY'), secret_key=os.environ.get('BINANCE_SECRET_KEY'))

    usdt_tickers = bs.get_usdt_tickers()
    bitcoin = bs.get_data("BTCUSDT")
    currencies = [bitcoin]

    for ticker in usdt_tickers:
        if ticker != "BTCUSDT":
            currency = bs.get_data(ticker)
            if currency.price != 0:
                currencies.append(currency)

    currency_data = pd.DataFrame([vars(c) for c in currencies])
    currency_data.to_csv("currency_data.csv")