from random import choice, shuffle
from telebot import TeleBot, types
с
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "пр")

@bot.message_handler(content_types=['text'])
def echo(message):
    choise_player = message.text.lower()
    if choise_player in game_inventory:
        choise_bot = random.choice(game_inventory)
        if choise_player == 'камень':
            if choise_bot == 'бумага':
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "проиграл лоз")
            elif choise_bot == 'ножницы'
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "молодца")
            else:
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "ничья")
    elif choise_player == 'бумага'
    if choise_bot == 'ножницы'
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "проиграл лоз")
            elif choise_bot == 'камень'
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "молодца")
            else:
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "ничья")
    elif choise_player == 'ножницы'
    if choise_bot == 'камень'
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "проиграл лоз")
            elif choise_bot == 'бумага'
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "молодца")
            else:
                bot.send_message(message.chat.id, choise_bot)
                bot.send_message(message.chat.id, "ничья")
          else: 
bot.send_message(message.chat.id, "я не понял")
bot.polling()