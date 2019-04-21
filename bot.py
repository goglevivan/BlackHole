import config

import telebot
import requests
import metods

bot = telebot.TeleBot(config.token)

try:
    url_my_404 ='www.ivgo180419.com'
    print(requests.get(url_my_404))
except:
    print("Error")



@bot.message_handler(content_types=["text"])

def mirrormessage(message):
    def his():
        bot.send_message(message.chat.id, 'Введите дату в формате 2016-7-5')
        date=message.text
        res = metods.money.history(date)
        bot.send_message(message.chat.id, res+' BLR за 1$')

    a = metods.Prsr
    if message.text == '/dol':
        res = metods.money.get_money(145)
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
        res = metods.money.get_money(292)
        bot.send_message(message.chat.id, res + ' BLR за 1€')
    elif message.text == '/pln':
        res = metods.money.get_money(293)
        bot.send_message(message.chat.id, res + ' BLR за 10zł')
    elif message.text == '/dkk':
        res = metods.money.get_money(291)
        bot.send_message(message.chat.id, res + ' BLR за 10kr')
    elif message.text == '/rub':
        res = metods.money.get_money(298)
        bot.send_message(message.chat.id, res + ' BLR за 100₽')
    elif message.text == '/czk':
        res = metods.money.get_money(305)
        bot.send_message(message.chat.id, res + ' BLR за 100Kč')

    elif message.text == '/jpy':
        res = metods.money.get_money(295)
        bot.send_message(message.chat.id, res + ' BLR за 100¥')
    elif message.text == '/cny':
        res = metods.money.get_money(304)
        bot.send_message(message.chat.id, res + ' BLR за 10¥')
    elif message.text == '/uah':
        res = metods.money.get_money(290)
        bot.send_message(message.chat.id, res + ' BLR за 100₴')
    elif message.text == '/historydol':
        res = metods.money.history()
        bot.send_message(message.chat.id, res + ' BLR за 1$  2017-7-6')
    elif message.text == '/rand':
        res = metods.money.rand()
        bot.send_message(message.chat.id, res + '- ваше число')

    else:
        bot.send_message(message.chat.id,'Введите /help для получения информации')
if __name__ =='__main__':
    bot.polling(none_stop=True)