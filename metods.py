import config
import random
import telebot
import requests
import time
from bs4 import BeautifulSoup
class Prsr:
    def get_html(url):
        try:
            r = requests.get(url)
        except:
            get_html(url)
        return r.text

    def get_data(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            h1 = soup.text
        except:
            get_data(html)
        return h1
class money:
    def get_money(y):
        try:
            a = Prsr
            url = "http://www.nbrb.by/API/ExRates/Rates/"+str(y)
            data1 = a.get_html(url)
            dct1 = {}
            dct1 = eval(data1)
        except:
            get_money(y)
        return str(dct1["Cur_OfficialRate"])
    def history():
        try:
            a = Prsr
            url = "http://www.nbrb.by/API/ExRates/Rates/145?onDate=2017-7-6"
            data1 = a.get_html(url)
            dct1 = {}
            dct1 = eval(data1)
        except:
            history()
        return str(dct1["Cur_OfficialRate"])
    def rand():
        return(str(random.randint(1,10)))