from time import sleep, time
import stock_tracker_functions as st
import sys
import yfinance as yf
import os
   
def display_menu():
    print("""
    1. Track Watchlist
    2. Add Watchlist (WIP)
    3. Edit Watchlist (WIP)
    4. Delete Watchlist (WIP)
    5. Exit
    """)

def track(watchlist):
    start = time()
    while True:
        try:
            for symbol in watchlist:
                print(f"{symbol:8}{yf.Ticker(symbol).history()['Close'][-1]:.2f}")
                sleep(1)
        except:
            print("not found")
        if time() - start >= 15:
            prompt = input("Enter to continue, any key to quit: ")
            start = time()
            if prompt:
                break


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


def choose_list():
      lists = read_directory()
      choice = int(input("Pick a watchlist, type the number: "))
      watchlist = lists[choice-1]
      
      f = open(f'watchlists/{watchlist}', "r")
      watchlist_data = f.read().split()
      f.close()
      return watchlist_data


def add_list():
    print("add a new list!")
    pass


def edit_list():
    print("edit a list!")
    pass


def del_list():
    print("delete a list!")
    pass


actions = {'2': add_list, '3': edit_list, '4': del_list}

def main():
    print("Welcome to St0ckTracker!")
    while True:
        display_menu()
        choice = input("Enter a menu number: ")
        if choice == '1':
            watchlist = choose_list()
            track(watchlist)
        elif choice in '234':
            actions[choice]()
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Enter a valid menu number!")


if __name__ == "__main__":
    main()