import telebot
import private_file
from telebot import types


#functions for telebots handler
def NewMarkupName(film_lis):                                            #names keyboard_generator
    new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for el in film_lis:
        new_markup.add(types.KeyboardButton(text=el))
    return new_markup

def NewMarkupCommand(com_lis):                                          #command keyboard generator
    new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for el in com_lis:
        new_markup.add(types.KeyboardButton(text='/'+el))
    return new_markup


bot=telebot.TeleBot(private_file.API_name)                              #telebot generation

@bot.message_handler(commands='start')

# #old variant

# def start_bot(message):
#     options_keyboard=NewMarkupName(['Series','Comics','Movies'])
#     bot.send_message(message.chat.id,'Welcome to Mordecai telegrambot. Today I will help you to entertain yourself. What would you like to watch?', reply_markup=options_keyboard)
#     bot.register_next_step_handler(message,options_handler)

# def options_handler(message):

#     if message.text=='Movies':
#         pass
#     if message.text=='Series':
#         bot.register_next_step_handler(message,ChoseFilm)
#     elif message.text=='Comics':
#         pass
#     else:
#         bot.send_message(message.chat.id,'Dear Sir or Madam, You must have pressed something wrong. Please, chose your answer from the button menu')
#         bot.register_next_step_handler(message,options_handler)

#start bot and handle first level requests

def start_bot(message):
    options_keyboard=types.InlineKeyboardMarkup(row_width=3,keyboard=[   #keyboard for chosing types of entertaintment
        [
            types.InlineKeyboardButton(text='Movies',callback_data='mov'),
            types.InlineKeyboardButton(text='Series',callback_data='ser'),
            types.InlineKeyboardButton(text='Comics',callback_data='com')
        ]
    ]
    )
    welcome_text='Welcome to Mordecai telegrambot. Today I will help you to entertain yourself. What would you like to watch?'

    bot.send_message(chat_id=message.chat.id,text=welcome_text, reply_markup=options_keyboard)


#callback handler for movies
@bot.callback_query_handler(func=lambda call: call.data=='mov')

def handle_mov(call):
    movies_lis=[]
    movie_keyboard=NewMarkupName(movies_lis)
    bot.send_message(call.message.chat.id, 'We have variety of movies. Chose one from the button menu below: ',reply_markup=movie_keyboard)
    print('call message id: ', call.message.message_id)
    bot.register_next_step_handler(call.message,ChoseFilm)

def ChoseFilm(message):

    film_list=['Atlantis','Young Justice','Regular Show']
    keyboard=NewMarkupName(film_lis=film_list)

    bot.send_message(message.chat.id,'Choose movie you want to see: ', reply_markup=keyboard)

    bot.register_next_step_handler(message,ViewMovie)

def ViewMovie(message):

    bot.send_message(message.chat.id,text=('Here it is) %s is your movie' % message.text), reply_markup=types.ReplyKeyboardRemove())
    start_markup=NewMarkupCommand(['start'])
    bot.send_message(message.chat.id,'If you want to start over again press buttons',reply_markup=start_markup)

#callback handler for series
@bot.callback_query_handler(func=lambda call: call.data=='ser')

def handle_ser(call):
    series_lis=[]
    series_keyboard=NewMarkupName(series_lis)
    bot.send_message(call.message.chat.id, 'We have variety of series. Chose one from the button menu below: ',reply_markup=series_keyboard)

#callback handler for comics
@bot.callback_query_handler(func=lambda call: call.data=='com')

def handle_com(call):
    com_lis=[]
    com_keyboard=NewMarkupName(com_lis)
    bot.send_message(call.message.chat.id, 'We have variety of movies. Chose one from the button menu below: ',reply_markup=com_keyboard)

 
#check for testing

@bot.message_handler(commands='check')
# inline keyboard appears under the message
def MakeInlineMarkup(message):
    new_markup=types.InlineKeyboardMarkup()

    button_1=types.InlineKeyboardButton(text='New Yes', callback_data='1')
    button_2=types.InlineKeyboardButton(text='NEW No',callback_data='2')
    button_3=types.InlineKeyboardButton(text='HELP! I NEED SOMEBODY',callback_data='3')
    button_4=types.InlineKeyboardButton(text='start',callback_data='start')

    new_markup.add(button_1, button_2, button_3, button_4)

    bot.send_message(message.chat.id,'Wait a sec', reply_markup=new_markup)

    new_new_markup=types.InlineKeyboardMarkup()
    new_new_markup.add(types.InlineKeyboardButton('text 1',callback_data='1.1'))

    bot.edit_message_reply_markup(chat_id=message.chat.id,message_id=message.message_id+1,reply_markup=new_new_markup)

@bot.callback_query_handler(func=lambda call: call.data=='1')

def handle_query_1(call):
    bot.send_message(call.message.chat.id, 'Congratulations. We are number '+call.data)

@bot.callback_query_handler(func=lambda call: call.data=='2' or call.data=='3')

def handle_query(call):
    bot.send_message(call.message.chat.id, 'Your stupid answer was :'+call.data)


@bot.callback_query_handler(func=lambda call: call.data=='start')

def handle_query(call):
    message=types.Message(call)
    start_bot(message)
    bot.send_message(call.message.chat.id, 'Your stupid answer was :'+call.data)
#Handler that passes that updates markup and waits for your response

@bot.message_handler(commands='film')
def ChoseFilm(message):

    film_list=['Atlantis','Young Justice','Regular Show']
    keyboard=NewMarkupName(film_lis=film_list)

    bot.send_message(message.chat.id,'Choose movie you want to see: ', reply_markup=keyboard)

    bot.register_next_step_handler(message,ViewMovie)

def ViewMovie(message):

    bot.send_message(message.chat.id,text=('Here it is) %s is your movie' % message.text), reply_markup=types.ReplyKeyboardRemove())
    start_markup=NewMarkupCommand(['start'])
    bot.send_message(message.chat.id,'If you want to start over again press buttons',reply_markup=start_markup)


bot.infinity_polling()