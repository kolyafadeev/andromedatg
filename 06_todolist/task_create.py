from sticker import ADD_STICKER, ENDPOINT_STICKER
from telegram.ext import Filters, CallbackContext, MessageHandler, CommandHandler, ConversationHandler
from telegram import Update
from constats import *

def add_task(update: Update, context: CallbackContext):
    name = update.effective_user.first_name
    update.message.reply_sticker(ADD_STICKER)
    update.message.reply_text(f"Просьба ввести дела, мастер {name} или /no чтобы прекратить операцию добавления")
    return TASK
def handle_task_text(update: Update, context: CallbackContext):
    message = update.message.text # взяли сообщение, где пользователь пишет текст дела
    context.user_data["todo_text"] = message # сохранили это в рюкзак
    update.message.reply_text(message)
    return ConversationHandler.END

def endpoint(update: Update, context: CallbackContext):
    update.message.reply_sticker(ENDPOINT_STICKER)
    update.message.reply_text('Операция прервана')
    return ConversationHandler.END # завершает диалог о добавлении дела
add_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex(f"^{CREATE}$"), add_task)],
    states={
        TASK: [MessageHandler(Filters.text & ~Filters.command, handle_task_text)]
    },
    fallbacks=[CommandHandler("no", endpoint)],
)