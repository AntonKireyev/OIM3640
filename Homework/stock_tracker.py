from time import sleep
import stock_tracker_functions as st
import sys
import yfinance as yf
   
def display_menu():
    print("""
    1. Track Watchlist
    2. Add Watchlist
    3. Edit Watchlist
    4. Delete Watchlist
    5. Exit
    """)

def track(watchlist):
    '''for second in range(10):
    print(f"{yf.Ticker('AAPL').history()['Close'][-1]:.2f}")
    sleep(1)'''



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
    print("Welcome to StackTracker!")
    while True:
        watchlist = 'AMZN NFLX FB GOOG'.split()
        display_menu()
        choice = input("Enter a menu number: ")
        if choice == '1':
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