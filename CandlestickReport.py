import plotly.graph_objects as go
import pandas as pd


def CreateFigure(df, ticker):
    print('Figure')
    try:
        date = pd.to_datetime(df.index)
        fig = go.Figure(data=[go.Candlestick(x=pd.to_datetime(df.index),
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
        
        fig.update_layout(xaxis_rangeslider_visible=False,title=ticker.upper(),template="plotly_dark")

        fig.update_yaxes(side="right",tickprefix="$")
     


        fig.write_image('test.png',format='png')
    except Exception as e:
        print(e)


