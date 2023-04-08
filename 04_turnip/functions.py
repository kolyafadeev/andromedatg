from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

BEGIN, GAME = 1, 2
GO = "Вперед"


def start(update: Update, context: CallbackContext):
    mark_up = [[GO]] # разметка клавиатуры
    keyboard = ReplyKeyboardMarkup( # клавиатура в тг
        keyboard=mark_up,
        resize_keyboard=True, # сжали размер
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
    heroes = [["дедку"], ["дедка", "репку"]]
    context.user_data["heroes"] = heroes
    update.message.reply_text("""
    Посадил дед репку. Выросла репка большая-пребольшая.
    Стал дед репку из земли тянуть.
    Тянет-потянет - вытянуть не может.
    Кого позвал дедка?""", reply_markup=ReplyKeyboardRemove())
    return GAME

def end(update: Update, context: CallbackContext):
    update.message.reply_text("Значит, ты выбрал конец")
    return ConversationHandler.END

def  get_game(update: Update, context: CallbackContext):
    text = update.message.text
    word = morph.parse(text)[0]
    nomn = word.inflect({"nomn"}).word
    accs = word.inflect({"accs"}).word
    update.message.reply_text(f"{nomn}, {accs}")
    heroes = context.user_data["heroes"] # из рюкзака достаем героев 
    heroes[0].insert(0, nomn) # [бабка, дедку]
    heroes.insert(0, [accs])
    answer = f"Я {nomn}.Буду помогать. "
    for nom, acc in heroes [1:]:
        answer += f"{nom} за {acc}."
    answer += "Тянут - потянут - вытянуть не могу. Кого позовем еще?"
    update.message.reply_text(f'{answer}')
    

