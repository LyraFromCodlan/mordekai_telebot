import telebot
import private_file
from telebot import types

bot=telebot.TeleBot(private_file.API_name)

@bot.message_handler(commands='register')

def MakeMarkup(message):

    markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)

    button_1=types.KeyboardButton('Yes')
    button_2=types.KeyboardButton('No')

    markup.row(button_1,button_2)

    keyboard=types.ReplyKeyboardRemove()


    bot.send_message(message.chat.id, 'Your answer was :'+message.text,reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: True)

# def handle_call(call):

#     keyboard=types.ReplyKeyboardRemove()

#     if call.text=='Yes':
#         bot.send_message(call.message.chat.id, 'Your correct answer was :'+call.data,)
#     elif call.text=='No':
#         bot.send_message(call.message.chat.id, 'Your incorrect answer was :'+call.data)
#     else:
#         # bot.send_message(call.message.chat.id, 'Your stupid answer was :'+call.data,reply_markup=keyboard)
#         bot.send_message(call.message.chat.id, 'Your stupid answer was :'+call.data)

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     buttonA = types.InlineKeyboardButton('A', callback_data='a')
#     buttonB = types.InlineKeyboardButton('B', callback_data='b')
#     buttonC = types.InlineKeyboardButton('C', callback_data='c')

#     markup.row(buttonA, buttonB)
#     markup.row(buttonC)

#     keyboard=types.ReplyKeyboardRemove()

#     bot.send_message(message.chat.id, 'It works!', reply_markup=keyboard)


bot.infinity_polling()

