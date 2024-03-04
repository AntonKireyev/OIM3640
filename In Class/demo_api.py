import yfinance as yf
 
#aapl = yf.Ticker("AAPL").history()
aapl = yf.Ticker("AAPL").history()['Close'][-1]

print(aapl)

