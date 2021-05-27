from typing import List

from local.daily_data_point import DailyDataPoint


class CoinData:

    def __init__(self, ticker, today, historical: List[DailyDataPoint], btc_history=None):
        self.ticker = ticker
        self.price = float(today.get("lastPrice"))
        # TODO: check length of data to see if historicals are possible
        self.chg_on_day = float(today.get("priceChangePercent"))

        self.chg_on_week = ((float(today.get("lastPrice")) - historical[-7].price_close) / historical[-7].price_close) * 100 if len(historical) > 7 else 0
        self.chg_on_month = ((float(today.get("lastPrice")) - historical[-30].price_close) / historical[-30].price_close) * 100 if len(historical) > 30 else 0
        self.chg_on_year = ((float(today.get("lastPrice")) - historical[0].price_close) / historical[0].price_close) * 100 if len(historical) >= 364 else 0

        self.chg_on_day_vs_btc = self.chg_on_day - btc_history.chg_on_day if btc_history else 0
        self.chg_on_week_vs_btc = self.chg_on_week - btc_history.chg_on_week if btc_history else 0
        self.chg_on_month_vs_btc = self.chg_on_month - btc_history.chg_on_month if btc_history else 0
        self.chg_on_year_vs_btc = self.chg_on_year - btc_history.chg_on_year if btc_history else 0
        volumes = [x.volume for x in historical]
        self.hdv7d_adv_week = max(volumes[:7]) / (sum(volumes[:7]) / 7) if len(volumes) > 7 else 0
        self.hdv7d_adv_month = max(volumes[:7]) / (sum(volumes[:30]) / 30) if len(volumes) > 30 else 0
        self.hdv7d_adv_year = max(volumes[:7]) / (sum(volumes) / len(volumes)) if len(volumes) >= 364 else 0
        self.hdv1m_adv_month = max(volumes[:30]) / (sum(volumes[:30]) / 30) if len(volumes) > 30 else 0
        self.hdv1m_adv_year = max(volumes[:30]) / (sum(volumes) / len(volumes)) if len(volumes) >= 364 else 0

    def __str__(self):
        return "CoinData(" \
               "ticker="+self.ticker + ", "\
               "price="+str(self.price) + ", "\
               "volume="+str(self.volume) +\
               ")"

    def __iter__(self):
        return iter([self.ticker, self.price, self.chg_on_day, self.chg_on_week, self.chg_on_month,
                     self.chg_on_year, self.chg_on_day_vs_btc, self.chg_on_week_vs_btc, self.chg_on_month_vs_btc,
                     self.chg_on_year_vs_btc, self.volume, self.hdv7d_adv_week, self.hdv7d_adv_month,
                     self.hdv7d_adv_year, self.hdv1m_adv_month, self.hdv1m_adv_year])
