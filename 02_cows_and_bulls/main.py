from telegram.ext import Updater, MessageHandler, Filters
from config import TOKEN
from functions import *

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

game_handler = MessageHandler(Filters.text, game)

dispatcher.add_handler(game_handler)


print("Server start")
updater.start_polling()
updater.idle()