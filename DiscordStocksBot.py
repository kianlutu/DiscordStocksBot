import os
import discord
import pyjokes 
import CandlestickReport 
import Emoji
import datetime

from discord.ext import commands
from yahoo_fin import stock_info as si
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='cv', help="Displays the ticker's candlestick chart and set the number of days it goes back in time with the parameter from yahoo finance.")
async def cv(ctx, ticker, days):
    try:
        end =  datetime.date.today().strftime("%m/%d/%Y")
        start = (datetime.date.today() - datetime.timedelta(days=int(days))).strftime("%m/%d/%Y")

        data = si.get_data(ticker,start_date=start,end_date=end,index_as_date=True)
        CandlestickReport.CreateFigure(data,ticker)
        await ctx.channel.send(file=discord.File('test.png'))
    except Exception as e:
        msg = 'Ticker not found'
        print(msg)
        await ctx.channel.send(msg)

@bot.command(name='ca', help="Displays the ticker's full candlestick chart history from yahoo finance.")
async def ca(ctx, ticker):
    try:
 
        data = si.get_data(ticker,index_as_date=True)
        CandlestickReport.CreateFigure(data,ticker)
        await ctx.channel.send(file=discord.File('test.png'))
    except Exception as e:
        msg = 'Ticker not found'
        print(msg)
        await ctx.channel.send(msg)



@bot.command(name='ah', help="Gets the ticker's after hours price from yahoo finance")
async def ah(ctx, ticker):
    try:
        quote = si.get_quote_table(ticker)

        livePrice = round(quote["Quote Price"],2)

        afterHours = round(float(quote["Ask"].split(' ')[0]),2)

        avgVolume = round(quote["Avg. Volume"])

        avgVolumeByM = round(avgVolume / 1000000,2)

        afterHoursChange = round(afterHours - livePrice,2)
        afterHoursChangePercent = round(afterHoursChange / afterHours * 100,2)

        emoji = Emoji.get_trend(afterHoursChange)

        msg = f'**{emoji}{ticker.upper()}** Yahoo After Hours: ${afterHours} ({afterHoursChange}) {afterHoursChangePercent}%, Avg. Volume: {avgVolumeByM}M '
        
        print(msg)
        await ctx.channel.send(msg)

    except:
        msg = 'Ticker not found'
        print(msg)
        await ctx.channel.send(msg)


@bot.command(name='p', help="Gets the ticker's current price and volume from yahoo finance.")
async def p(ctx, ticker):
    try:
        quote = si.get_quote_table(ticker)
        
        volume = round(quote["Volume"])

        volumeByM = round(volume / 1000000,2)

        livePrice = round(quote["Quote Price"],2)
        closePrice = round(quote["Previous Close"],2)
        
        liveChange = round(livePrice - closePrice,2)
        liveChangePercent = round(liveChange / closePrice * 100,2)

        emoji = Emoji.get_trend(liveChange)
        
        msg = f'**{emoji}{ticker.upper()}** Yahoo Live Price: ${livePrice} ({liveChange}) {liveChangePercent}%, Volume: {volumeByM}M'
        
        print(msg)
        await ctx.channel.send(msg)

    except:
        msg = 'Ticker not found'
        print(msg)
        await ctx.channel.send(msg)


@bot.command(name='j', help="Tells a random joke.")
async def j(ctx):
    joke = pyjokes.get_joke(language='en', category='all')
    print(joke)
    await ctx.channel.send(joke)


bot.run(TOKEN)