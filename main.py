import telebot
import private_file

bot=telebot.TeleBot(private_file.API_name)

@bot.message_handler(commands='register')

def start(message):
    if 'register' in message.text:
        bot.send_message(message.chat.id,'register is inside')

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
    bot.send_message(message.chat.id,'Hello,'+surname+name+'! Your age is'+age)
    # bot.pin_chat_message(name+' '+surname+' '+age,message.chat.id) #don't pin message in dialog, pin in conference

@bot.message_handler(commands='repeat')

def reply(message):
    bot.send_message(message.chat.id,'Are are you stuuupid?', message.text)

@bot.message_handler(content_types='text')

def report(message):
    if message.text=='check':
        bot.reply_to(message, 'Your expression is')
        with open(r'C:\Users\Lyra Hearthstrings\Desktop\Lyra Heartstrings\Media\Pictures\ОtNеЯ\9SR03mw6Rv8.jpg', 'rb') as photo:   #in future use with as safety measurement
            bot.send_photo(message.chat.id, photo, caption='STOP RIGHT HERE OR BONK!!!')
    else:
        bot.reply_to(message,'Incorrect or try /register or /repeat or word  "check"')
        bot.send_photo(message.chat.id, open(r'C:\Users\Lyra Hearthstrings\Desktop\Jared.jpg', 'rb'))   #never forget to add 'r' before path to the photo to read it properly



# message handler with pictures and pop-up message for 4 choices


bot.infinity_polling()


