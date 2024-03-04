from time import sleep
import yfinance as yf




def main():
    for second in range(10):
        print(f"{yf.Ticker('AAPL').history()['Close'][-1]:.2f}")
        sleep(1)

if __name__ == "__main__":
    main()