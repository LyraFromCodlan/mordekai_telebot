# bot = telebot.TeleBot("2088166250:AAEXeKCTXPermVngV2n_naKbmQzBvnZilO0")
# @bot.message_handler(content_types=["text"])

#program 1 simple echo bot

# def get_text_messages(message):
#     if message.text=='Hello there':
#         bot.send_message(message.chat.id, 'General Kenobi')
#     elif message.text=='whatsup':
#         bot.send_message(message.chat.id,'Wazaaaaa')
#     else:
#         bot.send_message(message.chat.id, message.text)
#         # bot.send_message(message.from_user.id, message.text) # 'message.from_user.id' suppose to work like 'chat.id' - just different path

# bot.infinity_polling()

#handler 1 for th repeat command

# @bot.message_handler(commands='repeat')

# def reply(message):
#     bot.send_message(message.chat.id,'Are are you stuuupid?', message.text)

#handler 2 answers to voice messages

# @bot.message_handler(content_types='voice')

# def DEF(message):
#     bot.send_message(message.chat.id,'Write something or get the fuck out!')
#     bot.send_message(message.chat.id, 'I am def, you stuuupid!')

#handler 3 - register bot

# @bot.message_handler(content_types=["text"])

# def start(message):
#     if message.text=='/register':
#         bot.send_message(message.chat.id,'Enter your name: ')
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.chat.id,'Try enter /register')

# def get_name(message):
#     global name;
#     name=message.text
#     bot.send_message(message.chat.id,"Enter your surname: ")
#     bot.register_next_step_handler(message,get_surname)

# def get_surname(message):
#     global surname;
#     surname=message.text
#     bot.send_message(message.chat.id,"Enter your age: ")
#     bot.register_next_step_handler(message,get_age)
# def get_age(message):
#     global age;
#     age=message.text
#     bot.send_message(message.chat.id,"Lets check if everything is right")
#     bot.send_message(message.chat.id,'Hello,'+surname+' '+name+'! Your age is '+age)
#     bot.register_next_step_handler(message,get_result)

# def get_result(message):
#     bot.send_message(message.chat.id,'Hello,',surname,name,'! Your age is',age)

#handler 4 for any text message

# @bot.message_handler(content_types='text')

# def report(message):
#     if message.text=='check':
#         bot.reply_to(message, 'Your expression is')
#     else:
#         bot.reply_to(message,'Incorrect')

# # bot starter through PopUpKeyboard

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

#handler 5 movie delivery through the command

#handler for 'film' command

# @bot.message_handler(commands='film')
# def ChoseFilm(message):

#     film_list=['Atlantis','Young Justice','Regular Show']
#     keyboard=extf.NewMarkupName(name_lis=film_list)

#     bot.send_message(message.chat.id,'Choose movie you want to see: ', reply_markup=keyboard)

#     bot.register_next_step_handler(message,ViewMovie)

# def ViewMovie(message):

#     bot.send_message(message.chat.id,text=('Here it is) %s is your movie' % message.text), reply_markup=types.ReplyKeyboardRemove())
#     start_markup=extf.NewMarkupCommand(['start'])
#     bot.send_message(message.chat.id,'If you want to start over again press buttons',reply_markup=start_markup)