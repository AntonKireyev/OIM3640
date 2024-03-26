'''
Use streamlit to create a simple app that plots a stocks closing price 
Use the the Yahoo Finance API (yfinance) to collect data (or API of your choice)
The app should have a textbox to enter stock symbol (perhaps the sidebar may work well for this)
Also include date boxes for a start date and end date (default should be to plot the last year of data)
Display a button that when clicked graphs the chosen stock closing prices for the specified date range 
Above the chart display a title with the stock symbol or company name and data range being charted
'''

import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf

st.write("## Stock Price History")

st.sidebar.header("Parameters")
stock = st.sidebar.text_input("Stock Ticker", value = None)
start_date = st.sidebar.date_input("Start Date", value = None)
end_date = st.sidebar.date_input("End Date", value = None)
button = st.sidebar.button("Graph!")

# missing way to rotate dates on x axis to prevent overflow
def display_plot():
    fig, axes = plt.subplots()
    axes.plot(values)
    axes.set_title(chart_title)
    axes.set_xlabel("Date")
    axes.set_ylabel("Price ($USD)")
    st.pyplot(fig)

if start_date and end_date:
    values = yf.Ticker(stock).history(start = start_date, end = end_date, interval = '1d')['Close']
    chart_title = f"{stock} Price History | {start_date} to {end_date}"
else:
    values = yf.Ticker(stock).history(period = '1y', interval = '1d')['Close']
    chart_title = f"{stock} Price History | Past Year"      # missing way to generate dates for today and 1 year ago

if button:
    display_plot()

