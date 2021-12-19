import telebot
import private_file as pf
from telebot import types
import ext_func as extf

#functions for telebots handler
def NewMarkupName(name_lis):                                            #names keyboard_generator
    if name_lis==[]:
        name_lis=['None']

    new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for el in name_lis:
        new_markup.add(types.KeyboardButton(text=el))
    return new_markup

def NewMarkupCommand(com_lis):                                          #command keyboard generator
    if com_lis==[]:
        com_lis=['None']
        
    new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for el in com_lis:
        new_markup.add(types.KeyboardButton(text='/'+el))
    return new_markup


bot=telebot.TeleBot(pf.API_name)                              #telebot generation

@bot.message_handler(commands='start')


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
    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    movies_list=['Batman: Bad Blood','8 mile','Regular Show through the universe']                                     #movie list - must be replaced with database data
    mov_keyboard=extf.NewMarkupName(name_lis=movies_list)
    msg_text='We have variety of movies. Chose one from the button menu below: '

    bot.send_message(call.message.chat.id, msg_text, reply_markup=mov_keyboard)

    bot.register_next_step_handler(call.message,ViewMovie)

def ViewMovie(message):
    bot.send_message(message.chat.id,text=('You have chosen %s ' % message.text), reply_markup=types.ReplyKeyboardRemove())
    msg_text='Do you want to watch movie, access comments or give your rating?\nChose from the menu below'
    pf.film_dict={'name':str.lower(message.text)}
    option_dict={'Watch':'wt','Comments':'cmnt','Rating':'rt'}
    options_keyboard=extf.NewInlineMarkup(name_dict=option_dict)

    bot.send_message(message.chat.id,msg_text,reply_markup=options_keyboard)


    start_markup=extf.NewMarkupCommand(['start'])                   #generates start keyboard so user can return back to start
    bot.send_message(message.chat.id,'If you want to start over again press buttons',reply_markup=start_markup)

    #generate call handler for handling comments, ratings and play - probably an external file. Also must generate and use class templates for movies, series and comics objects 

#callback handler for series
@bot.callback_query_handler(func=lambda call: call.data=='ser')

def handle_ser(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    series_lis=['Atlantis','Young Justice','Regular Show']                                      #series list - must be replaced with database data
    series_keyboard=extf.NewMarkupName(series_lis)
    msg_text='We have variety of series. Chose one from the button menu below: '

    bot.send_message(call.message.chat.id, msg_text, reply_markup=series_keyboard)
    bot.register_next_step_handler(call.message, ChoseSeason)

#function for nadling series season choice

def ChoseSeason(message):
    pf.series_dict={'name':str.lower(message.text)}
    seasons=[] #Here is database call for number of seasons
    season_markup=NewMarkupName(seasons)

    bot.send_message(message.chat.id,text=('You have chosen %s' % message.text),reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id,text='Now chose season:',reply_markup=season_markup)

    bot.register_next_step_handler(message, ChoseEpisode)

#function for nadling series episode choice

def ChoseEpisode(message):
    pf.series_dict={'season':str.lower(message.text)}
    episodes=[] #Here is database call for number of episodes
    episodes_markup=NewMarkupName(episodes)
    bot.send_message(message.chat.id,text='Now chose season:',reply_markup=episodes_markup)

    #handler for View which will be made through class

    

#callback handler for comics
@bot.callback_query_handler(func=lambda call: call.data=='com')

def handle_com(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    com_lis=['Ctr+Alt+Del','Titans','Constantine hellblazer','Transmetroplitan']          #comics list - must be replaced with database data
    com_keyboard=extf.NewMarkupName(com_lis)
    bot.send_message(call.message.chat.id, 'We have variety of comics. Chose one from the button menu below: ',reply_markup=com_keyboard)
    bot.register_next_step_handler(call.message, ChoseYear)

#function for hadling comics year of publishing

def ChoseYear(message):
    pf.series_dict={'name':str.lower(message.text)}
    years=[] #Here is database call for number of year in which issue was published
    years_markup=NewMarkupName(years)

    bot.send_message(message.chat.id,text=('You have chosen %s comics' % message.text),reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id,text='Now chose year of publishing:',reply_markup=years_markup)

    bot.register_next_step_handler(message, ChoseIssue)

#function for hadling comics number of issue - depends on comics

def ChoseIssue(message):
    pf.series_dict={'season':str.lower(message.text)}
    issues=[] #Here is database call for number of issues and their numbers in the database
    issues_markup=NewMarkupName(issues)
    bot.send_message(message.chat.id,text='Now chose issue:',reply_markup=issues_markup)

    #handler for View which will be made through class
 
#check for testing

@bot.message_handler(commands='check')
# inline keyboard appears under the message
def MakeInlineMarkup(message):
    new_markup=types.InlineKeyboardMarkup(row_width=2)

    button_1=types.InlineKeyboardButton(text='1st call', callback_data='1')
    button_2=types.InlineKeyboardButton(text='2nd call', callback_data='2')
    button_3=types.InlineKeyboardButton(text='3rd call',callback_data='3')
    button_4=types.InlineKeyboardButton(text='Go to start the bot',callback_data='start')

    new_markup.add(button_1, button_2, button_3, button_4)

    bot.send_message(message.chat.id,'Wait a sec', reply_markup=new_markup)

    # new_new_markup=types.InlineKeyboardMarkup()
    # new_new_markup.add(types.InlineKeyboardButton('text 1',callback_data='1.1'))

    # bot.edit_message_reply_markup(chat_id=message.chat.id,message_id=message.message_id+1,reply_markup=new_new_markup)

@bot.callback_query_handler(func=lambda call: call.data=='1')

def handle_query_1(call):
    bot.answer_callback_query(callback_query_id=call.id,text='')
    bot.send_message(call.message.chat.id, 'Congratulations. We are number '+call.data)

@bot.callback_query_handler(func=lambda call: call.data=='2' or call.data=='3')

def handle_query(call):
    bot.answer_callback_query(callback_query_id=call.id,text='You have chosen option 2 or 3')
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, 'Your incorrcet answer was :'+call.data)


@bot.callback_query_handler(func=lambda call: call.data=='start')

def handle_query(call):
    bot.answer_callback_query(callback_query_id=call.id,text='Hello, I am Mordecai. I have deleted your Inline keyboard so you can go to start')
    start_bot(call.message)   
#Handler that passes that updates markup and waits for your response

bot.infinity_polling()