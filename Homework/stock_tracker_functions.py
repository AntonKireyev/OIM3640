import os
from time import sleep, time
import sys
import yfinance as yf

"""
FUNCTIONS NEEDED:
    1. Track Watchlist
    2. Add Watchlist (WIP)
    3. Edit Watchlist (WIP)
    4. Delete Watchlist (WIP)
    5. Exit

"""

# read_directory function, will need to use it to view a directory.

def read_directory(): 
      if not os.path.exists('watchlists'):            # test for existence of folder
            print("No watchlist directory, creating")
            os.mkdir("watchlists")
      else:
            watchlists = os.listdir('watchlists')                        # returns list with names of files
            if not watchlists:
                  print("No saved list")
            else:
                  for count, watchlist in enumerate(watchlists, 1):                    # Print numbered list of files.
                        watchlist = watchlist[:-4]
                        print(f'{count}.  {watchlist}')
                  return watchlists
            

# Track list
'''
1. Allow continous tracking of an N list of stocks
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
2. allow user to choose which list
'''
def choose_list():
      lists = read_directory()
      choice = int(input("Pick a watchlist, type the number: "))
      watchlist = lists[choice-1]
      
      f = open(f'watchlists/{watchlist}', "r")
      watchlist_data = f.read().split()
      f.close()
      return watchlist_data



# Add Watchlist

'''
1.
'''

def add_watchlist():
     pass   # TODO


# Edit Watchlists

def edit_watchlist():
     lists = read_directory()
     pass   # TODO


# Delete Watchlists

def del_watchlist():
     pass   # TODO
