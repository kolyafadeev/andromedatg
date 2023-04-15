import csv, random
from telegram.ext import CallbackContext, ConversationHandler
from telegram import (Update, ReplyKeyboardMarkup, ReplyKeyboardRemove)


GO = "LETS GO"
GAME = 1
QUESTIONS_ON_ROUND = 4



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
    questions = read_csv()
    random.shuffle(questions)

    questions = questions[:QUESTIONS_ON_ROUND]
    context.user_data["вопросы"] = questions
    context.user_data['right_ansver'] = GO
    return GAME


def game(update: Update, context: CallbackContext):
    questions = context.user_data["вопросы"]
    answers = questions.pop()
    question_text = answers.pop(0)
    right_ansver = answers[0]
    random.shuffle(answers)
    mark_up = [answers[:2], answers[2:]]
    keyboard = ReplyKeyboardMarkup(  
        keyboard=mark_up,
        resize_keyboard=True,  
        one_time_keyboard=True,
        )

    update.message.reply_text(question_text, reply_markup=keyboard)




def end(update: Update, context: CallbackContext):
    update.message.reply_text("Значит, ты выбрал конец")
    return ConversationHandler.END
