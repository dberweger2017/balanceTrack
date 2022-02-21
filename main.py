import pandas as pd
import yfinance as yf
import csv
from datetime import datetime,date
import csv
import requests
import time

prices = []
#requests.get(f'https://api.telegram.org/bot5176536572:AAHEHyZlxo118z_hbuBS73pQdYG8K2CSa98/sendMessage?chat_id=-775777947&text={text}')

df = pd.read_csv("portfolio.csv")

for i in range(len(df.iloc[0])):
    ticker = df[str(i)][0]
    if ticker == "Cash":
        pass
    else:
        prices += [yf.Ticker(ticker).history(period="1d")["Close"][0]]


currentBalance = int(df[str(0)][1])

for i in range(len(prices)):
    currentBalance += int(df[str(i+1)][1])*prices[i]

days = (date.today()-date(2022, 1, 31)).days
date = datetime.today().strftime('%d-%m-%y')

text = (f'{days}. {date}, Portfolio Balance: {round(currentBalance)} Fr.')
requests.get(f'https://api.telegram.org/bot5176536572:AAHEHyZlxo118z_hbuBS73pQdYG8K2CSa98/sendMessage?chat_id=-775777947&text={text}')
