from typing import List

import pytest
from mock import patch
from binance import Client
from currency.local.binance_service import BinanceService
from currency.local.daily_data_point import DailyDataPoint

@patch.object(Client, 'get_all_tickers')
def test_get_usdt_tickers(mock_get_all_tickers, tickers):
    mock_get_all_tickers.return_value = tickers
    bs = BinanceService(api_key="foo", secret_key="bar")
    tickers = bs.get_usdt_tickers()
    assert (len(tickers) == 2)
    assert (tickers[0] == 'BTCUSDT')
    assert (tickers[1] == 'ETHUSDT')


@patch.object(Client, 'get_ticker')
def test_get_todays_data(mock_get_ticker, todays_data):
    mock_get_ticker.return_value = todays_data
    bs = BinanceService(api_key="foo", secret_key="bar")
    today = bs.get_todays_data("FOOBAR")
    assert (today.get("priceChange") == "-94.99999800")
    assert (today.get("priceChangePercent") == "-95.960")


@patch.object(Client, 'get_historical_klines')
def test_get_daily_one_year_historical(mock_get_historical_klines, historical_klines_1yr):
    mock_get_historical_klines.return_value = historical_klines_1yr
    bs = BinanceService(api_key="foo", secret_key="bar")
    historical = bs.get_daily_one_year_historical("FOOBAR")
    assert (type(historical[0]) == DailyDataPoint)
    assert(len(historical) == 2)
    assert(historical[0].price_open == 0.01634790)
    assert(historical[1].price_open == 0.12345678)


@pytest.fixture
def historical_klines_1yr():
    return [
        [
            1499040000000,  # Open time
            "0.01634790",  # Open
            "0.80000000",  # High
            "0.01575800",  # Low
            "0.01577100",  # Close
            "148976.11427815",  # Volume
            1499644799999,  # Close time
            "2434.19055334",  # Quote asset volume
            308,  # Number of trades
            "1756.87402397",  # Taker buy base asset volume
            "28.46694368",  # Taker buy quote asset volume
            "17928899.62484339"  # Ignore
        ],
        [
            1499040000000,  # Open time
            "0.12345678",  # Open
            "0.23456789",  # High
            "0.12345670",  # Low
            "0.23456780",  # Close
            "100000.123",  # Volume
            1499644799999,  # Close time
            "1234.1234",  # Quote asset volume
            500,  # Number of trades
            "3456.34567",  # Taker buy base asset volume
            "67.234567",  # Taker buy quote asset volume
            "17928899.62484339"  # Ignore
        ],
    ]


@pytest.fixture
def tickers():
    return [
        {
            "symbol": "BTCUSDT",
            "price": "4.000000"
        },
        {
            "symbol": "ETHUSDT",
            "price": "4.000000"
        },
        {
            "symbol": "BTCBNB",
            "price": "4.000000"
        },
        {
            "symbol": "ETHUPUSDT",
            "price": "4.000000"
        },
        {
            "symbol": "BTCDOWNUSDT",
            "price": "4.000000"
        }
    ]


@pytest.fixture
def todays_data():
    return {
        "priceChange": "-94.99999800",
        "priceChangePercent": "-95.960",
        "weightedAvgPrice": "0.29628482",
        "prevClosePrice": "0.10002000",
        "lastPrice": "4.00000200",
        "bidPrice": "4.00000000",
        "askPrice": "4.00000200",
        "openPrice": "99.00000000",
        "highPrice": "100.00000000",
        "lowPrice": "0.10000000",
        "volume": "8913.30000000",
        "openTime": 1499783499040,
        "closeTime": 1499869899040,
        "fristId": 28385,  # First tradeId
        "lastId": 28460,  # Last tradeId
        "count": 76  # Trade count
    }
