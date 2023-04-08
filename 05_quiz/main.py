from config import TOKEN
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from functions import *

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        GAME: [MessageHandler(Filters.text & ~Filters.command, game)]
    },
    fallbacks=[CommandHandler("end", end)]
)

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(conv_handler)

print("Сервер - loading - go")
updater.start_polling()
updater.idle()