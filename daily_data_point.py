from datetime import datetime

#   [
#     1499040000000,      // Open time
#     "0.01634790",       // Open
#     "0.80000000",       // High
#     "0.01575800",       // Low
#     "0.01577100",       // Close
#     "148976.11427815",  // Volume
#     1499644799999,      // Close time
#     "2434.19055334",    // Quote asset volume
#     308,                // Number of trades
#     "1756.87402397",    // Taker buy base asset volume
#     "28.46694368",      // Taker buy quote asset volume
#     "17928899.62484339" // Ignore
#   ]

class DailyDataPoint:

    def __init__(self, data):
        self.open_time = datetime.utcfromtimestamp(data[0] / 1000)
        self.close_time = datetime.utcfromtimestamp(data[6] / 1000)
        self.price_open = float(data[1])
        self.price_high = float(data[2])
        self.price_low = float(data[3])
        self.price_close = float(data[4])
        self.volume = float(data[5])
        self.quote_asset_volume = float(data[7])
        self.num_of_trades = int(data[8])
        self.taker_buy_base_asset_vol = float(data[9])
        self.taker_buy_quote_asset_vol = float(data[10])

    def __str__(self) -> str:
        return "OTime " + str(self.open_time) + " CTime " + str(self.close_time) + " Open px: " + str(
            self.price_open) + " Closing px: " + str(
            self.price_close) + " Volume: " + str(self.volume)
