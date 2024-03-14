from nsepy import get_history
from datetime import date

data = get_history(symbol="NIFTY", start=date(2015,1,1), end=date(2015,1,31))
print(data[["Close"]].plot())