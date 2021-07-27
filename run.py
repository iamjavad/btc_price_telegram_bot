#!/usr/bin/python3

from telegram.ext import * 
import requests
import json
import logging
import datetime

updater = Updater(token='', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
		level=logging.INFO)

def start(updater, context):
	context.bot.send_message(chat_id=updater.effective_chat.id, text="""Hi\nwelcom to BITCOIN PRICE bot \ntype or click on /price\ni will send you BTC price\nsource code: https://github.com/iamjavad/btc_price_telegram_bot.""")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def price(updater, context):
	url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
	resp = requests.get(url)
	j = json.loads(resp.text)
	#print(json.dumps(j, indent=4))
	price = resp.json()["data"]["amount"]
	price = str(price)
	
	x = str(datetime.datetime.now())[0:16]
	
	context.bot.send_message(chat_id=updater.effective_chat.id, text="BITCOINE PRICE: " + price + " USD 💲" + ' \n DATE: ' + x)
price_handler = CommandHandler('price', price)
dispatcher.add_handler(price_handler)

updater.start_polling()
