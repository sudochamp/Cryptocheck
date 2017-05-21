import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
import apis
import random

TOKEN = "ENTER TOKEN HERE"
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Time for BTC")

def list(bot, update):
    chat_id = update.message.chat_id
    btcPrice = apis.btcapi()
    ethPrice = apis.ethapi()
    zecPrice = apis.zecapi()
    bot.send_message(chat_id=chat_id, text="BTCUSD: {0}\n"
                                  "ETHUSD: {1}\n"
                                  "ZECUSD: {2}\n".format(btcPrice, ethPrice, zecPrice))

def ta(bot, update):
    chat_id = update.message.chat_id
    random_number = random.randint(0, 10)
    if random_number <= 5:
        bot.send_message(chat_id=chat_id, text="Buy")
    if random_number >= 5:
        update.send_message(chat_id=chat_id, text="Sell")

start_handler = CommandHandler('start', start)
coin_handler = CommandHandler('list', list)
ta_handler = CommandHandler('ta', ta)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(coin_handler)
dispatcher.add_handler(ta_handler)

updater.start_polling()
