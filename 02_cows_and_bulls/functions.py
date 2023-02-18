from telegram import Update 
from telegram.ext import CallbackContext
import random

def game (update:Update, context: CallbackContext):
    message = update.message.text #сообщение, которое бот принял
    print(context.user_data)
    if "secret_number" not in context.user_data:
        secret_number = random.randint(1000, 9999) #компьютер загадал
        context.user_data["secret_number"] = secret_number # сохранилт в рюкзачок
    secret_number = context.user_data["secret_number"]
    print(context.user_data)
    
    if not message.isdigit():
        update.message.reply_text(f"Компьютер загадал 4-х значное число. Вам нужно отгадать число")
        return None
    elif not len(message) == 4:
        update.message.reply_text(f"enter a four digit number")
        return None
    secret_number = str(secret_number)

    cows = 0 
    bulls = 0
    for index, digit in enumerate(secret_number):
        if digit in message:
            if message[index] == digit:
                bulls += 1
            else:
                cows += 1
    update.message.reply_text(f"В вашем числе {cows} коров, {bulls} быков")
    if bulls == 4:
        update.message.reply_text('УРА, ПОБЕДА ГОВЯДИНЫ')
        del context.user_data["secret_number"]
