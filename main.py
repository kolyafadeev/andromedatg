from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from config import TOKEN # чтобы связать твоего бота с кодом
from telegram import Update


def start(update: Update, context: CallbackContext):#колбэк - функция
    #update- обновление чата, в котором находится свежее собщение
    #context - весь чат, мы будем использовать в качестве рюкзака
    name = update.message.from_user.full_name
    update.message.reply_animation("https://thumbs.gfycat.com/AntiqueLinedBrocketdeer-max-1mb.gif")
    update.message.reply_text(f"Летсго бро {name}")
    update.message.reply_text("""
                                Я разумный интеллект, вот что я могу:
                                /start - справка 
                                /bye - прощание
                                /zitata - великие слова великих людей
                                /contact - мой контактик)))
                                /plus - калькулятор 
                                """)

def bye (update: Update, context: CallbackContext):
    name = update.message.from_user.full_name
    update.message.reply_text(f"НЕ УХАДИ, позялуйста... {name}")

def zitata (update: Update, context: CallbackContext):
    name = update.message.from_user.full_name
    update.message.reply_text(f"Чтобы идти к цели, нужно встать с постели {name}")

def send_contact (update: Update, context: CallbackContext):
    update.message.reply_contact("79393017475", "Колясик")

def get_numbers(update: Update, context: CallbackContext):
    numbers = context.args
    if len(numbers) != 2:
        update.message.reply_text ("Введи 2 числа дурень, через /plus !")
        return None
    try:
        num1 = int(numbers [0])
        num2 = int(numbers [1])
        return num1, num2
    except ValueError:
        update.message.reply_text("не не чувак, это не цифры")
        return None 
    

def plus(update: Update, context: CallbackContext):
    nums = get_numbers(update, context)
    if nums is not None:
        num1, num2 = nums 
        context.bot.send_message (update.effective_chat.id, "{num1} + {num2} = {num1 + num2}")

def revolution(update: Update, context: CallbackContext):
    expression = update.message.text
    try:
        update.message.reply_text(f'{expression} = {eval(expression)}')
    except:
        update.message.reply_text('Ого')

print("Сервер запущен")
updater = Updater(TOKEN)
dispatcher = updater.dispatcher


start_handler = CommandHandler("start", start)
bye_handler = CommandHandler ("bye", bye)
zitata_handler = CommandHandler ("zitata", zitata)
contact_handler = CommandHandler ("contact", send_contact)
plus_handler = CommandHandler ("plus", plus)
eval_handler = MessageHandler (Filters.text, revolution)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(bye_handler)
dispatcher.add_handler(zitata_handler)
dispatcher.add_handler(contact_handler)
dispatcher.add_handler(plus_handler)
dispatcher.add_handler(eval_handler)

updater.start_polling()
updater.idle()