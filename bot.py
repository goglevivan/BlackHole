import config

import telebot
import requests
import metods
import sqlite3
bot = telebot.TeleBot(config.token)





@bot.message_handler(content_types=["text"])

def mirrormessage(message):
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute( 'CREATE TABLE if not EXISTS message(id INTEGER PRIMARY  KEY AUTOINCREMENT,msg TEXT);')
    zn = message.text
    c.executescript('insert into message("msg") values("'+message.text+'");')
    c.close()
    conn.close()
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
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
/five - что писали боту пять сообщений назад 
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

    elif message.text == '/five':
        c.execute('select id from message order by id desc limit 1;')
        num = c.fetchall()
        print(num)
        num = num[0]
        print (num)
        num =num[0]
        num = int(num)

        if num < 5:
            bot.send_message(message.chat.id, 'ничего')
        else:
            num = num - 5
            num = str(num)
            c.execute('select msg from message where id='+num+';')
            res = c.fetchall()
            bot.send_message(message.chat.id, res )


    else:
        bot.send_message(message.chat.id,'Введите /help для получения информации')
    c.close()
    conn.close()
if __name__ =='__main__':
    bot.polling(none_stop=True)