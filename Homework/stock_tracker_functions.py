import os
from time import sleep, time
import sys
import yfinance as yf

# Track list
'''
1. Allow continous tracking of an N list of stocks
2. allow user to choose which list
'''

watchlist = 'AMZN NFLX META GOOG'.split()

def track(watchlist):
    start = time()
    
    while True:
        for stock in watchlist:
            print(f"{stock:<10}{yf.Ticker(stock).history()['Close'][-1]:>.2f}")
            sleep(1)
            if time() - start >= 5:
                prompt = input("Keep Running? [ENTER] to continue, type anything to quit: ")
                start = time()
                if prompt:
                    break

# Choose Watchlist
                
'''
1. 
'''
def read_directory():
    if not os.path.exists('watchlists'):
        print("No watchlist directory, creating")
        os.mkdir("watchlists")
    

    print(os.listdir('watchlists'))

read_directory()