from nsepython import equity_history

symbol = "TCS"
series = "EQ"
start_date = "14-03-2024"
end_date ="14-03-2024"
print(equity_history(symbol,series,start_date,end_date))