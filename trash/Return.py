import telebot
import private_file
from telebot import types

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


@bot.message_handler(commands=['popup'])
def popup(message):
    bot.send_message(message.chat.id, 'Choose, which picture you would like to see:')
    markup = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton('1')
    button_2 = types.KeyboardButton('2')
    button_3 = types.KeyboardButton('3 NEW TEXT')
    button_4 = types.KeyboardButton('4')
    button_5 = types.KeyboardButton('5')
    button_6 = types.KeyboardButton('6')

    markup.row(button_1, button_2, button_3)
    markup.row(button_4, button_5, button_6)

    
#     bot.register_next_step_handler(message,pict_chosen)
    
    
# def pict_chosen(message):
#     bot.send_message(message.chat.id, 'Here you go',reply_markup=types.ReplyKeyboardRemove())
#     # bot.send_message(message.chat.id, 'Here you go')
#     for ind in range (1,7):
#         if ind==int(message.text):
#             with open(r'C:\Users\Lyra Hearthstrings\Desktop\Jared.jpg', 'rb') as photo:
#                 bot.send_photo(message.chat.id, photo, caption=message.text+') You again?')
    



@bot.message_handler(content_types='text')

def report(message):
    if message.text=='check':
        bot.reply_to(message, 'Your expression is')
        with open(r'C:\Users\Lyra Hearthstrings\Desktop\Lyra Heartstrings\Media\Pictures\ОtNеЯ\9SR03mw6Rv8.jpg', 'rb') as photo:   #in future use with as safety measurement
            bot.send_photo(message.chat.id, photo, caption='STOP RIGHT HERE OR BONK!!!')
    else:
        bot.reply_to(message,'Incorrect or try /register or /repeat or word  "check"')
        bot.send_photo(message.chat.id, open(r'C:\Users\Lyra Hearthstrings\Desktop\Jared.jpg', 'rb'))   #never forget to add 'r' before path to the photo to read it properly
        
# @bot.message_handler(content_types=['photo'])
# def photo(message):
#     fileID = message.photo[-1].file_id
#     file_info = bot.get_file(fileID)
#     downloaded_file = bot.download_file(file_info.file_path)

#     with open("image.jpg", 'wb') as new_file:
#         new_file.write(downloaded_file)

#     bot.reply_to(message, "You've send this photo. Please don't do this or we will send it back to you. Understood?")
#     reply_of_user=types.ReplyKeyboardMarkup()
#     button_yes=types.KeyboardButton('Yes')
#     button_no=types.KeyboardButton('No')
    
#     reply_of_user.row(button_yes,button_no)

# @bot.callback_query_handler(func=lambda call: True)

# def handle_query(call):
#     if call.text=='Yes':
#         bot.send_message(call.chat.id, 'Good, Anakin, good')
#     elif call.text=='No':
#         bot.send_message(call.chat.id, 'Well then')
#         with open(r'C:\Users\Lyra Hearthstrings\Desktop\VS Code Python\knewIT\MordecaiBot', 'rb') as photo:
#             bot.send_photo(call.chat.id, photo, caption='Take it back and shove it up your arse')
#     else:
#         bot.reply_to(call.chat.id, 'ENGLISH, MF! DO YOU SEAK IT?')
# message handler with pictures and pop-up message for 4 choices


bot.infinity_polling()
