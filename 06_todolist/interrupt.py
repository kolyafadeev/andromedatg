from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from sticker import *
from constats import *

def end(update: Update, context: CallbackContext):
    update.message.reply_photo(open("images\goodbye.jpg", 'br'))
    return ConversationHandler.END

def wrong_message(update: Update, context: CallbackContext):
    update.message.reply_sticker(WRONG_STICKER)
    update.message.reply_text("Ой! Такой команды нет")