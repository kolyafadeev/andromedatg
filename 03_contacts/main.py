from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
from config import TOKEN
from functions import *

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

contact_handler = ConversationHandler(
    entry_points = [CommandHandler("start", start)],
    states={
        NAME: [MessageHandler(Filters.text & ~Filters.command, get_name )],
        LAST_NAME: [MessageHandler(Filters.text & ~Filters.command, last_get_name)],
        HOBBY: [MessageHandler(Filters.text & ~Filters.command, get_hobby)]
    },
    fallbacks = [CommandHandler("end", end)]
)

dispatcher.add_handler(contact_handler)

print("Server start")
updater.start_polling()
updater.idle()