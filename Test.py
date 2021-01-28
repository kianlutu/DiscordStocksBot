import os
import discord
import plotly.graph_objects as go
import pandas as pd
import CandlestickReport
import datetime 


from yahoo_fin import stock_info, options 

ticker = "pltr"

try:
    end = datetime.date.today().strftime("%m/%d/%Y")
    start =  (datetime.date.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y")

    quote = stock_info.get_quote_table(ticker)
    price = stock_info.get_live_price(ticker)
    volume = quote["Volume"]
    data = stock_info.get_data(ticker, end_date = end, start_date = start, index_as_date = True, interval ="1d")
    afterHours = round(float(quote["Ask"].split(' ')[0]),2)

    CandlestickReport.CreateFigure(data,ticker)


    print()
except Exception as e:
    print(e)

print()