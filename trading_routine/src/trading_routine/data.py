"""Market data fetching via Alpaca."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

import pandas as pd
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame


def fetch_daily_bars(symbols: list[str], years: int = 3) -> dict[str, pd.DataFrame]:
    client = StockHistoricalDataClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_API_SECRET"],
    )
    req = StockBarsRequest(
        symbol_or_symbols=symbols,
        timeframe=TimeFrame.Day,
        start=datetime.now(timezone.utc) - timedelta(days=365 * years),
        adjustment="all",
    )
    df = client.get_stock_bars(req).df
    return {
        s: df.xs(s, level="symbol")[["open", "high", "low", "close", "volume"]].dropna()
        for s in symbols
    }
