import config
import random
import telebot
import requests
import time
from bs4 import BeautifulSoup
bot = telebot.TeleBot(config.token)

class Prsr:
    def get_html(url):
        r = requests.get(url)
        return r.text

    def get_data(html):
        soup = BeautifulSoup(html, 'lxml')
        h1 = soup.text
        return h1
class money:
    def get_money(y):
        a = Prsr
        url = "http://www.nbrb.by/API/ExRates/Rates/"+str(y)
        data1 = a.get_html(url)
        dct1 = {}
        dct1 = eval(data1)
        return str(dct1["Cur_OfficialRate"])
    def history():
        a = Prsr
        url = "http://www.nbrb.by/API/ExRates/Rates/145?onDate=2017-7-6"
        data1 = a.get_html(url)
        dct1 = {}
        dct1 = eval(data1)
        return str(dct1["Cur_OfficialRate"])
    def rand():
        return(str(random.randint(1,10)))


@bot.message_handler(content_types=["text"])

def mirrormessage(message):
    def his():
        bot.send_message(message.chat.id, 'Введите дату в формате 2016-7-5')
        date=message.text
        res = money.history(date)
        bot.send_message(message.chat.id, res+' BLR за 1$')

    a = Prsr
    if message.text == '/dol':
        res = money.get_money(145)
        bot.send_message(message.chat.id, res+' BLR за 1$')
    elif message.text == '/help':
        help_list = '''
        /dol - узнать курс доллара на сегодняшний день
/eur - узнать курс евро на сегодняшний день
/pln - узнать курс злотого на сегодняшний день
/dkk - узнать курс датских крон на сегодняшний день
/rub - узнать курс российских рублей на сегодняшний день
/czk - узнать курс чешских крон на сегодняшний день
/jpy - узнать курс японских йен на сегодняшний день
/cny - узнать курс китайских юаней на сегодняшний день
/uah - узнать курс украинских гривен на сегодняшний день
/historydol - узнать курс доллара  на 2017-7-6
/rand - выводит рандомное число от 0 до 10
        '''
        bot.send_message(message.chat.id, help_list)
    elif message.text == '/eur':
        res = money.get_money(292)
        bot.send_message(message.chat.id, res + ' BLR за 1€')
    elif message.text == '/pln':
        res = money.get_money(293)
        bot.send_message(message.chat.id, res + ' BLR за 10zł')
    elif message.text == '/dkk':
        res = money.get_money(291)
        bot.send_message(message.chat.id, res + ' BLR за 10kr')
    elif message.text == '/rub':
        res = money.get_money(298)
        bot.send_message(message.chat.id, res + ' BLR за 100₽')
    elif message.text == '/czk':
        res = money.get_money(305)
        bot.send_message(message.chat.id, res + ' BLR за 100Kč')

    elif message.text == '/jpy':
        res = money.get_money(295)
        bot.send_message(message.chat.id, res + ' BLR за 100¥')
    elif message.text == '/cny':
        res = money.get_money(304)
        bot.send_message(message.chat.id, res + ' BLR за 10¥')
    elif message.text == '/uah':
        res = money.get_money(290)
        bot.send_message(message.chat.id, res + ' BLR за 100₴')
    elif message.text == '/historydol':
        res = money.history()
        bot.send_message(message.chat.id, res + ' BLR за 1$  2017-7-6')
    elif message.text == '/rand':
        res = money.rand()
        bot.send_message(message.chat.id, res + '- ваше число')

    else:
        bot.send_message(message.chat.id,'Введите /help для получения информации')
if __name__ =='__main__':
    bot.polling(none_stop=True)