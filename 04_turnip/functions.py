from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove


BEGIN, GAME = 1, 2
GO = "Вперед"


def start(update: Update, context: CallbackContext):
    mark_up = [[GO]]
    keyboard = ReplyKeyboardMarkup(
        keyboard=mark_up,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=f"Если хочешь начать игру, нажми {GO}"
    )

    update.message.reply_text(
        f"""
        Ты любишь придумывать сказки? Я очень люблю.
        Ты знаешь сказку как посадил дед репку?
        А кто помогал деду репку тянуть? Чтобы начать, нажми на кнопку {GO}!""",
        reply_markup=keyboard)
    return BEGIN


def get_begin(update: Update, context: CallbackContext):
    update.message.reply_text("""Посадил дед репку. Выросла репка большая-пребольшая.
                              Стал дед репку из земли тянуть. Тянет-потянет - вытянутьне может.
                              Кого позвал дедок?""",
    reply_markup = ReplyKeyboardRemove())
    return GAME


def end(update: Update, context: CallbackContext):
    update.message.reply_text("Значит, ты выбрал конец")
    return ConversationHandler.END
