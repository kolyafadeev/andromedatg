from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TOKEN
from telegram import Update


def start(update: Update, context: CallbackContext):#колбэк - функция
    #update- обновление чата, в котором находится свежее собщение
    #context - весь чат, мы будем использовать в качестве рюкзака
    name = update.message.from_user.full_name
    update.message.reply_text(f"Летсго бро {name}")
    update.message.reply_text("""
                                Я разумный интеллект, вот что я могу:
                                /start - справка 
                                /bye - прощание
                                /zitata - великие слова великих людей
                                """)

def bye (update: Update, context: CallbackContext):
    name = update.message.from_user.full_name
    update.message.reply_text(f"НЕ УХАДИ, позялуйста... {name}")

def zitata (update: Update, context: CallbackContext):
    name = update.message.from_user.full_name
    update.message.reply_text(f"Чтобы идти к цели, нужно встать с постели {name}")

print("Сервер запущен")
updater = Updater(TOKEN)
dispatcher = updater.dispatcher


start_handler = CommandHandler("start", start)
bye_handler = CommandHandler ("bye", bye)
zitata_handler = CommandHandler ("zitata", zitata)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(bye_handler)
dispatcher.add_handler(zitata_handler)

updater.start_polling()
updater.idle()