import telebot
import apis
import logging
import random
import requests
import time
import sys

# Logger for Debug
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Token for API
TOKEN = "68779605:AAGAww5D1ZkWHCRDRwL23SZ-4RGiqv8XaUk"
tb = telebot.TeleBot(TOKEN)


# Handles Recieved Messages
@tb.message_handler(commands=['start', 'help'])
def send_welcome(message):
    tb.reply_to(message, "Wassup Doc?")


@tb.message_handler(commands=['btc'])
def send_btcprice(message):
    chat_id = message.chat.id
    currentPrice, highestPrice, lowestPrice = apis.btcapi_bitstamp()
    tb.send_message(chat_id, text="Bitstamp: {0}\n"
                                  "High: {1}\n"
                                  "Low: {2}\n".format(currentPrice, highestPrice, lowestPrice))


@tb.message_handler(commands=['eth'])
def send_ethprice(message):
    chat_id = message.chat.id
    tb.send_message(chat_id, text="Ethereum: " + str(apis.etheruem_price()))


@tb.message_handler(commands=['ta'])
def send_tradingadvice(message):
    chat_id = message.chat.id
    random_number = random.randint(0, 10)
    if random_number <= 5:
        tb.send_message(chat_id, text="Buy")
    if random_number >= 5:
        tb.send_message(chat_id, text="Sell")

@tb.message_handler(commands="sad")
def send_NOOOOO(message):
    chat_id = message.chat.id
    audio = open('audio/no.mp3', 'rb')
    tb.send_audio(chat_id, audio)

while True:
    try:
        tb.polling(none_stop=True)
    except requests.exceptions.ConnectionError as e:
        print >> sys.stderr, str(e)
        time.sleep(15)

# Polls telegram servers for new messages
tb.polling()
