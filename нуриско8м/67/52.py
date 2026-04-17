import telebot
from telebot import types
import json

TOKEN = "8263281836:AAGbcqTWmY8zE10chQbS-qBSaCStGfaladw"
bot = telebot.TeleBot(TOKEN)

def load_questions():
    with open('bertyuiop.json', 'r', encoding='utf-8') as f:
        return json.load(f)

questions = load_questions()
user_states = {}

def send_question(chat_id):
    state = user_states.get(chat_id)
    index = state['index']

    if index >= len(questions):
        score = state['score']
        bot.send_message(
            chat_id,
            f"Викторина окончена!\nВаш результат: {score} из {len(questions)}",
            reply_markup=types.ReplyKeyboardRemove()
        )
        return

    q_data = questions[index]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [types.KeyboardButton(opt) for opt in q_data['options']]
    markup.add(*buttons)
    markup.add(types.KeyboardButton("Пропустить вопрос"))

    bot.send_message(chat_id, q_data['question'], reply_markup=markup)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_states[chat_id] = {'index': 0, 'score': 0}
    bot.send_message(chat_id, "Привет! Давай начнем викторину.")
    send_question(chat_id)

@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    chat_id = message.chat.id
    
    if chat_id not in user_states:
        bot.send_message(chat_id, "Нажми /start, чтобы начать игру.")
        return

    state = user_states[chat_id]
    index = state['index']

    if index >= len(questions):
        return

    correct_answer = questions[index]['answer']

    if message.text == "Пропустить вопрос":
        state['index'] += 1
        send_question(chat_id)
        return

    if message.text == correct_answer:
        state['score'] += 1
        bot.send_message(chat_id, "Верно")
    else:
        bot.send_message(chat_id, f"Неверно. Правильный ответ: {correct_answer}")

    state['index'] += 1
    send_question(chat_id)

bot.polling(none_stop=True)