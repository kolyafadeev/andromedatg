from config import TOKEN
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from startmenu import *
from interrupt import *
from task_create import add_handler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        MENU: [MessageHandler(Filters.text & ~Filters.command, main_menu)],
        MENU_ITEMS:[
            add_handler,
            MessageHandler(Filters.text & ~Filters.command, wrong_message)
        ]
    },
    fallbacks=[CommandHandler("end", end)]
)

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(conv_handler)

print("Сервер - loading - go")
updater.start_polling()
updater.idle()