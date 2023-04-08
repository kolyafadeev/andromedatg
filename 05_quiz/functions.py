import csv
from telegram.ext import CallbackContext, ConversationHandler
from telegram import (Update, ReplyKeyboardMarkup, ReplyKeyboardRemove)


GO = "LETS GO"
GAME = 1


def read_csv():
    with open("05_quiz\вопросы.csv", "r", encoding="utf-8") as file:
        quest = list(csv.reader(file, delimiter="|"))
        return quest


def write_csv():
    with open("05_quiz\вопросы.csv", "a", encoding="utf-8") as file:
        worker = csv.writer(file, delimiter="|",
                            lineterminator="\n")
        worker.writerow(["Как называется упорядоченное движение заряженных частиц",
                         "Электрический ток", "Реакция", "Растворение", "Напряжение"])


def start(update: Update, context: CallbackContext):
    mark_up = [[GO]]  # разметка клавиатуры
    keyboard = ReplyKeyboardMarkup(  # клавиатура в тг
        keyboard=mark_up,
        resize_keyboard=True,  # сжали размер
        one_time_keyboard=True,
        input_field_placeholder=f"Нажми на кнопку '{GO}', поиграем?"
    )
    update.message.reply_text(
        "Добро пожаловать в викторину😃")
    update.message.reply_text(
        f"Чтобы начать, нажми на '{GO}'", reply_markup=keyboard)
    return GAME


def game(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Игра началась ОХОХОХОО"
    )


def end(update: Update, context: CallbackContext):
    update.message.reply_text("Значит, ты выбрал конец")
    return ConversationHandler.END
