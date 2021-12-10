import telebot
import private_file
from telebot import types

bot=telebot.TeleBot(private_file.API_name)

@bot.message_handler(commands='reply')

def MakeReplyMarkup(message):
#popup keyboard appears in the left corner of the texting menu
    markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)

    button_1=types.KeyboardButton('Yes')
    button_2=types.KeyboardButton('No')

    markup.row(button_1,button_2)

    bot.send_message(message.chat.id, 'Your answer was :'+message.text,reply_markup=markup)
 

@bot.message_handler(commands='inline')
# inline keyboard appears under the message
def MakeInlineMarkup(message):
    new_markup=types.InlineKeyboardMarkup()

    button_1=types.InlineKeyboardButton(text='New Yes', callback_data='1')
    button_2=types.InlineKeyboardButton(text='NEW No',callback_data='2')
    button_3=types.InlineKeyboardButton(text='HELP! I NEED SOMEBODY',callback_data='2')

    new_markup.add(button_1, button_2, button_3)
    # bot.send_message(message.chat.id, 'Delete markup',reply_markup=types.ReplyKeyboardRemove())

    bot.send_message(message.chat.id, 'Your answer was : Empty',reply_markup=new_markup)

# @bot.callback_query_handler(func=lambda call: True)

# def handle_query(call):
#     bot.send_message(call.message.chat.id, 'Your stupid answer was :'+call.data)

#Handler that passes that updates markup and waits for your response

@bot.message_handler(commands='film')
def ChoseFilm(message):
    def NewMarkup(film_lis):
        new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for el in film_lis:
            new_markup.add(types.KeyboardButton(text=el))
        return new_markup

    film_list=['Atlantis','Young Justice','Regular Show']
    keyboard=NewMarkup(film_lis=film_list)

    # keyboard1=types.ReplyKeyboardMarkup()
    # button_1=types.KeyboardButton('Atlantis')
    # button_2=types.KeyboardButton('The Mask')
    # button_3=types.KeyboardButton('Courage the Cowardly Dog')
    # keyboard1.add(button_1, button_2, button_3)

    bot.send_message(message.chat.id,'Choose movie you want to see: ', reply_markup=keyboard)

    bot.register_next_step_handler(message,ViewMovie)

def ViewMovie(message):
    # film_list=['Atlantis','Young Justice','Regular Show']

    # while message.text not in film_list:  #сделать через  try требование корректного ввода
    #     bot.send_message(message.chat.id, text="Enter movie's name")

    bot.send_message(message.chat.id,text=('Here it is) %s is your movie' % message.text), reply_markup=types.ReplyKeyboardRemove())


bot.infinity_polling()