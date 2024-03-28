''' Stock Chart Display

When the app is launched, the user will immediately be prompted to enter a ticker symbol, a
start and end date. Both the start and end date will be optional, defaulting to one year ago and
today respectively. 

Once the preliminaries are chosen and the data has been downloaded, the user is then presented with a menu of “columns” to analyze. 
The chosen column can be analyzed using raw data OR percent change calculated as (end / beg).

After choosing raw or percent change the user is presented with a table of summary statistics and prompted to either
choose another column or proceed to graphing operations.

Upon proceeding to the graphing portion of the application, the user will first select to type of
graph desired (area, histogram, line), and then the data “column” to graph. 

Once again, they should be prompted to graph raw data or percent change. Note: percent change data probably
doesn't lend itself well to an area chart.
'''
import streamlit as st
import matplotlib.pyplot as plt
from time import time, sleep
import yfinance as yf

values = 0
chart_title = ''

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

def display_plot():
    fig, axes = plt.subplots()
    axes.plot(values)
    axes.set_title(chart_title)
    axes.set_xlabel("Date")
    axes.set_ylabel("Price ($USD)")
    st.pyplot(fig)



def main():
    st.write("## St0ckTracker!")
    st.sidebar.header("Parameters")
    stock = st.sidebar.text_input("Stock Ticker", value = None)
    start_date = st.sidebar.date_input("Start Date", value = None)
    end_date = st.sidebar.date_input("End Date", value = None)
    button = st.sidebar.button("Graph!")

    if start_date and end_date:
        values = yf.Ticker(stock).history(start = start_date, end = end_date, interval = '1d')['Close']
        chart_title = f"{stock} Price History | {start_date} to {end_date}"
    else:
        values = yf.Ticker(stock).history(period = '1y', interval = '1d')['Close']
        chart_title = f"{stock} Price History | Past Year"      # missing way to generate dates for today and 1 year ago
        
    if button:
        display_plot()




if __name__ == "__main__":
    main()
