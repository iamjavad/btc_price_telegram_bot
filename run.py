#!/usr/bin/python3


from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext  import MessageHandler, Filters
import logging

updater = Updater(token='', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
		level=logging.INFO)

def start(updater, context):
	context.bot.send_message(chat_id=updater.effective_chat.id, text="")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)