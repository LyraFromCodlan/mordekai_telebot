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
    bot.send_message(message.chat.id, "this is before calling function GetAge")
    bot.send_message(message.chat.id,"Enter your age: ")
    bot.register_next_step_handler(message,get_age)
    bot.send_message(message.chat.id, "this is after calling function GetAge")
def get_age(message):
    global age;
    age=message.text
    bot.send_message(message.chat.id,"Lets check if everything is right")
    bot.send_message(message.chat.id,'Hello,'+surname+' '+name+'! Your age is '+age)
    bot.register_next_step_handler(message,get_result)

def get_result(message):
    bot.send_message(message.chat.id,'Hello,',surname,name,'! Your age is',age)

@bot.message_handler(content_types='text')

def report(message):
    if message.text=='check':
        bot.reply_to(message, 'Your expression is')
    else:
        bot.reply_to(message,'Incorrect')

bot.infinity_polling()
