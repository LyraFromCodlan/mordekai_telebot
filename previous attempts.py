# bot = telebot.TeleBot("2088166250:AAEXeKCTXPermVngV2n_naKbmQzBvnZilO0")
# @bot.message_handler(content_types=["text"])


# def get_text_messages(message):
#     if message.text=='Hello there':
#         bot.send_message(message.chat.id, 'General Kenobi')
#     elif message.text=='whatsup':
#         bot.send_message(message.chat.id,'Wazaaaaa')
#     else:
#         bot.send_message(message.chat.id, message.text)
#         # bot.send_message(message.from_user.id, message.text) # 'message.from_user.id' suppose to work like 'chat.id' - just different path

# bot.infinity_polling()

# @bot.message_handler(commands='repeat')

# def reply(message):
#     bot.send_message(message.chat.id,'Are are you stuuupid?', message.text)

# @bot.message_handler(content_types='voice')

# def DEF(message):
#     bot.send_message(message.chat.id,'Write something or get the fuck out!')
#     bot.send_message(message.chat.id, 'I am def, you stuuupid!')

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

# bot.infinity_polling()

# @bot.message_handler(content_types='text')

# def report(message):
#     if message.text=='check':
#         bot.reply_to(message, 'Your expression is')
#     else:
#         bot.reply_to(message,'Incorrect')



