import yfinance as yf
import pandas as pd
from datetime import datetime

TICKERS = {
    "S&P500": "^GSPC",
    "NASDAQ": "^IXIC",
    "KOSPI": "^KS11",
    "USD_KRW": "KRW=X"
}

def fetch_data():
    results = []

    for name, ticker in TICKERS.items():
        data = yf.download(ticker, period="5d", interval="1d", progress=False)

        if len(data) < 2:
            continue

        today_close = float(data["Close"].iloc[-1])
        yesterday_close = float(data["Close"].iloc[-2])

        change_pct = (today_close - yesterday_close) / yesterday_close * 100

        results.append({
            "Index": name,
            "Close": round(today["Close"], 2),
            "Change(%)": round(change_pct, 2)
        })

    df = pd.DataFrame(results)
    df["Date"] = datetime.now().strftime("%Y-%m-%d")
    return df
