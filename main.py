import telebot 
import private_file

bot=telebot.TeleBot(private_file.API_name)

@bot.message_handler(content_types=["text"])

def start(message):
    if message.text=='/register':
        bot.send_message(message.chat.id,'Enter your name: ')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.chat.id,'Try enter /register')

def get_name(message):
    global name;
    name=message.text
    bot.send_message(message.chat.id,"Enter your surname: ")
    bot.register_next_step_handler(message,get_surname)

def get_surname(message):
    global surname;
    surname=message.text
    bot.send_message(message.chat.id,"Enter your age: ")
    bot.register_next_step_handler(message,get_age)
def get_age(message):
    global age;
    age=message.text
    bot.send_message(message.chat.id,"Lets check if everything is right")
    bot.send_message(message.chat.id,'Hello,'+surname+' '+name+'! Your age is'+age)
#      get_result(message)

# def get_result(message):
#     bot.send_message(message.chat.id,'Hello,',surname,name,'! Your age is',age)

bot.infinity_polling()


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