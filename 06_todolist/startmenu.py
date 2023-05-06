from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from sticker import *
from constats import *
from file_work import init


def start(update: Update, context: CallbackContext):
    init(update, context)
    mark_up = [[GO]]  # разметка клавиатуры
    keyboard = ReplyKeyboardMarkup(  # клавиатура в тг
        keyboard=mark_up,
        resize_keyboard=True,  # сжали размер
        one_time_keyboard=True,
        input_field_placeholder=f"Нажми на кнопку '{GO}', чтобы начать"
    )
    name = update.effective_user.first_name
    update.message.reply_sticker(START_STICKER)
    update.message.reply_text(f"Приветствую тебя, {name}")
    update.message.reply_text(f"В этом боте ты можешь \n-создать задачу\n-изменить задачу\n-посмотреть имеющиеся\n-удалить задаучу\n-отметить задачу выполненной",
                              reply_markup=keyboard)
    return MENU


def main_menu(update: Update, context: CallbackContext):
    menu = [[READ], [CREATE, DONE], [UPDATE, DELETE]]
    keyboard = ReplyKeyboardMarkup(
        keyboard=menu,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    name = update.effective_chat.full_name
    update.message.reply_sticker(MAIN_MENU_STICKER)
    update.message.reply_text(f"Выберите, что хотите сделать, мастер {name}?", reply_markup=keyboard)
    return MENU_ITEMS