#!/usr/bin/env python
# coding: utf-8

# In[1]:


## import librararies

import pandas as pd
import numpy as np


# In[2]:


## load all the data files

master = pd.read_csv('Master.csv')
sp500 = pd.read_csv('SP500.csv')
us10Y = pd.read_csv('US10Y.csv')
crude = pd.read_csv('Crude.csv')
gold = pd.read_csv('gold.csv')
corn = pd.read_csv('Corn.csv')
us1Y = pd.read_csv('US1Y.csv')
sentiment = pd.read_csv('sentiment.csv')
trend_bitcoin = pd.read_csv('GoogleTrend_Bitcoin2.csv')
trend_cryptocurrency = pd.read_csv('GoogleTrend_Cryptocurrency.csv')
indicators = pd.read_csv('indicators.csv')
bitcoin = pd.read_csv('bitcoin_prices_new.csv')
crypto = pd.read_csv('added_data.csv')


# In[3]:


## change the column heading to match that of the master dataframe - "Dates"

master = master.rename(columns={"date": "Dates"})
sentiment = sentiment.rename(columns={"date": "Dates"})
trend_bitcoin = trend_bitcoin.rename(columns={"Week": "Dates"})
trend_cryptocurrency = trend_cryptocurrency.rename(columns={"Week": "Dates"})
indicators = indicators.rename(columns={"Date": "Dates"})
bitcoin["Dates"] = pd.to_datetime(bitcoin["Dates"])
crypto = crypto.rename(columns={"Date": "Dates"})


# In[4]:


## changes the date formate across all files - "YYYY-MM-DD"

master["Dates"] = pd.to_datetime(master["Dates"])
sp500["Dates"] = pd.to_datetime(sp500["Dates"])
us10Y["Dates"] = pd.to_datetime(us10Y["Dates"])
crude["Dates"] = pd.to_datetime(crude["Dates"])
gold["Dates"] = pd.to_datetime(gold["Dates"])
corn["Dates"] = pd.to_datetime(corn["Dates"])
us1Y["Dates"] = pd.to_datetime(us1Y["Dates"])
sentiment["Dates"] = pd.to_datetime(sentiment["Dates"])
trend_cryptocurrency["Dates"] = pd.to_datetime(trend_cryptocurrency["Dates"])
trend_bitcoin["Dates"] = pd.to_datetime(trend_bitcoin["Dates"])
indicators["Dates"] = pd.to_datetime(sentiment["Dates"])
crypto["Dates"] = pd.to_datetime(crypto["Dates"])


# In[5]:


## Merge the master dataframe with the other dataframes containing all the data

master = pd.merge(master, sp500[["Dates", "S&P 500 (^SPX) - Index Value"]], on="Dates", how="left")
master = pd.merge(master, us10Y[["Dates", "US Treasure 10Y Maturity"]], on="Dates", how="left")
master = pd.merge(master, crude[["Dates", "Crude Oil - Light (NYMEX) Historical Pricing"]], on="Dates", how="left")
master = pd.merge(master, gold[["Dates", "Gold (COMEX:^GC) - Day Close Price"]], on="Dates", how="left")
master = pd.merge(master, corn[["Dates", "Corn Price Per Bushel"]], on="Dates", how="left")
master = pd.merge(master, us1Y[["Dates", "US Treasure 1Y Maturity"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "twitter_total_posts"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "positive_tweets"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "negative_tweets"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "neutral_tweets"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "tweet_sentiment"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "news_text_count"]], on="Dates", how="left")
master = pd.merge(master, sentiment[["Dates", "news_sentiment"]], on="Dates", how="left")
master = pd.merge(master, trend_cryptocurrency[["Dates", "Crypto Global Ranking"]], on="Dates", how="left")
master = pd.merge(master, indicators[["Dates", "DJI"]], on="Dates", how="left")
master = pd.merge(master, indicators[["Dates", "NASDAQ"]], on="Dates", how="left")
master = pd.merge(master, indicators[["Dates", "VIX"]], on="Dates", how="left")
master = pd.merge(master, bitcoin[["Dates", "Open"]], on="Dates", how="left")
master = pd.merge(master, bitcoin[["Dates", "Close"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "DOGE"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "COPPER"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "BTC_VOLUME"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "ETH"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "LTC"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "SJD"]], on="Dates", how="left")
master = pd.merge(master, crypto[["Dates", "EUR"]], on="Dates", how="left")


# In[6]:


master.head(2)


# In[7]:


## For all NaN values, we will use the interpolated values

master['S&P 500 (^SPX) - Index Value'].interpolate(inplace=True)
master['US Treasure 10Y Maturity'].interpolate(inplace=True)
master['Crude Oil - Light (NYMEX) Historical Pricing'].interpolate(inplace=True)
master['Gold (COMEX:^GC) - Day Close Price'].interpolate(inplace=True)
master['Corn Price Per Bushel'].interpolate(inplace=True)
master['US Treasure 1Y Maturity'].interpolate(inplace=True)
master['twitter_total_posts'].interpolate(inplace=True)
master['positive_tweets'].interpolate(inplace=True)
master['neutral_tweets'].interpolate(inplace=True)
master['negative_tweets'].interpolate(inplace=True)
master['tweet_sentiment'].interpolate(inplace=True)
master['news_text_count'].interpolate(inplace=True)
master['news_sentiment'].interpolate(inplace=True)
master['Crypto Global Ranking'].interpolate(inplace=True)
master['DJI'].interpolate(inplace=True)
master['NASDAQ'].interpolate(inplace=True)
master['VIX'].interpolate(inplace=True)
master['Open'].interpolate(inplace=True)
master['DOGE'].interpolate(inplace=True)
master['COPPER'].interpolate(inplace=True)
master['BTC_VOLUME'].interpolate(inplace=True)
master['ETH'].interpolate(inplace=True)
master['LTC'].interpolate(inplace=True)
master['SJD'].interpolate(inplace=True)
master['EUR'].interpolate(inplace=True)


# In[8]:


## remove dumplicates from the dataframe (from the Dates column)

master = master.drop_duplicates(subset=["Dates"], keep="first")


# In[9]:


master.info()


# Theres a total of 543 data days and a total of 25 variables

# In[10]:


master.to_csv("Capstone_Data_5.csv", index=False)

