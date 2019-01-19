# -*- coding: utf-8 -*-

import requests
import json
from time import strptime
from dateutil.relativedelta import relativedelta

def StockPrice_Crawler(StockCode, date):
    try:
        url = 'http://www.tse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+str(date)+'&stockNo='+StockCode
        return json.loads(requests.get(url).text)['data']
    except:
        pass

def change_date(date):
    return (date / 100 + 89) * 100 + 1 if date / 100 % 100 == 12 else (date / 100 + 1) * 100 + 1
