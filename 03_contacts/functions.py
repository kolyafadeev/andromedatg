from telegram import Update 
from telegram.ext import CallbackContext, ConversationHandler

NAME, LAST_NAME, HOBBY, PHONE  = range(4)



def start (update:Update, context: CallbackContext):
    update.message.reply_text("Диалог начинается")
    update.message.reply_text("Введите свое имя")
    return NAME
    
    
def get_name(update:Update, context: CallbackContext):
    name = update.message.text
    context.user_data["name"] = name.title()
    update.message.reply_text(f"Твое имя - {name}")
    update.message.reply_text(F'Ваша фамилия, сэр')
    return LAST_NAME

def last_get_name(update:Update, context: CallbackContext):
    last_name = update.message.text
    first_name = context.user_data["name"]
    update.message.reply_text(f"Ты - {first_name}, Ваша фамилия - {last_name}")
    update.message.reply_text(f"Ваше hobby ?")
    return HOBBY

def get_hobby (update:Update, context: CallbackContext):
    hobby = update.message.text
    update.message.reply_text(f"Ваше хобби - {hobby}")
    update.message.reply_text(f"А телефончик не дадите?")
    return PHONE

def get_phone (update:Update, context: CallbackContext):
    phone = update.message.text
    if not phone.isdigit(): # если не число
        update.message.reply_text(f"Введите число позялуйста, а не слово")
        return None
    update.message.reply_text(f"Ваш телефончик у меня хихихи - {phone}")
    return ConversationHandler.END


def end (update:Update, context: CallbackContext):
    update.message.reply_text("Значит, ты выбрал конец")
    return ConversationHandler.END