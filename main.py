
import telebot
import private_file as pf
from telebot import types
import ext_func as extf
from mysql.connector import connect, Error


bot=telebot.TeleBot(pf.API_name)                              #telebot generation


#Extensive functions are here closed by "#1-- --1" pareathesis, because they can't be imported without reffering to bot directly

#1--

def check_connection(message):
    try:                                                                        #try for safety of the connection
        connection=connect_to_db()
        if connection.is_connected():
            connection.get_server_info()                                      #gets info about mysql version
            cursor = connection.cursor()
    except Error as er:
        bot.send_message(message.chat.id,'Error: '+er)                                  #if exception is caught sends corresponding message to user
    finally:                                                                            #closing connection in case of successfull connection
        if connection.is_connected():
            cursor.close()
            connection.close()

def connect_to_db():
    connection=connect(                                                     #connection to the database
            host='localhost',
            user='LyraHearthstrings', # input('User name: '),
            password='20percentcooler', # getpass('Password: '),
            database='mordecaitelebot' #database name in ''
            )
    return connection

def formate_resp(response):                         #fucntion formating db answer to represent it properly in the buttons or else
    for ind, val in enumerate(response):                              
        response[ind]=str(val).replace(',','').replace(')','').replace('(','').replace("'",'')
    return response

def extract_names_from_db(message, list_names, action):                              #function extract data from the database, must update not on;y to extract names, but rather all possible data
    try:                                                                    #extracts names of entertainment typr from the database and preventing errors
        connection=connect_to_db()
        cursor = connection.cursor()
                                                                #series of ifs to chose correct db inquiry
        if action in ['film','series','comics']:
            db_inquiry="""select """+list_names+"""_name from """ +list_names+"""_list;"""



        cursor.execute(db_inquiry)                                          #send inquery
        data_list=cursor.fetchall()                                        #catching db response
        data_list=formate_resp(data_list)                                  #formating of recieve data to eleminate all unnecessry symbols
        data_list.append('/start')                                          #appends 'start' command to be able to return back
    except:
        bot.send_message(chat_id=message.chat.id,text='Error happened')        #working with errors and letting user know tre is one
        data_list=['empty']
    finally:                                                                        #closing connection after all operations are completed
        if connection.is_connected():
            cursor.close()
            connection.close()
        return data_list                            #returns response as list of names


# class Series():                                         #class that holds all info about series
#     series_name: str
#     series_seas_ep: dict
#     episode_rating: int

# class Comics():                                         #class that holds all info about comics
#     comics_name: str
#     comics_seas_ep: dict
#     comics_rating: int

# class Film():                                         #class that holds all info about film
#     comics_name: str
#     comics_seas_ep: dict
#     comics_rating: int
#     def __init__(self, message, action):
#         return extract_names_from_db(message,name,action)


#--1

@bot.message_handler(commands='start')

#start bot and handle first level requests

def start_bot(message):
    check_connection(message)
    options_dict={
        'Films':'film',
        'Series':'series',
        'Comics':'comics'
        }
    options_keyboard=extf.NewInlineMarkup(options_dict)

    welcome_text='Welcome to Mordecai telegrambot. Today I will help you to entertain yourself. What would you like to watch?'
    bot.send_message(chat_id=message.chat.id,text=welcome_text, reply_markup=options_keyboard)


#callback handler for movies
@bot.callback_query_handler(func=lambda call: call.data=='film')

def handle_mov(call):
    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)

    film_list=extract_names_from_db(call.message, call.data)                #extracts data from the database to form buttons

    mov_keyboard=extf.NewMarkupName(name_lis=film_list)
    msg_text='We have variety of movies. Chose one from the button menu below: '

    bot.send_message(call.message.chat.id, msg_text, reply_markup=mov_keyboard)

    bot.register_next_step_handler(call.message,ViewMovie)

def ViewMovie(message):
    bot.send_message(message.chat.id,text=('You have chosen %s ' % message.text), reply_markup=types.ReplyKeyboardRemove())
    msg_text='Do you want to watch movie, access comments or give your rating?\nChose from the menu below'
    # Film film=Film(message, message.text, "init_film")                                              #initializes class, which hold all movie info, uncluding link
    option_dict={'Watch':'wt','Comments':'cmnt','Rating':'rt'}
    options_keyboard=extf.NewInlineMarkup(name_dict=option_dict)

    bot.send_message(message.chat.id,msg_text,reply_markup=options_keyboard)


    start_markup=extf.NewMarkupCommand(['start'])                   #generates start keyboard so user can return back to start
    bot.send_message(message.chat.id,'If you want to start over again press buttons',reply_markup=start_markup)

    #generate call handler for handling comments, ratings and play - probably an external file. Also must generate and use class templates for movies, series and comics objects 

#callback handler for series
@bot.callback_query_handler(func=lambda call: call.data=='series')

def handle_ser(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)         #delete prevoius message to make interface free of unnecessary options
    series_lis=extract_names_from_db(call.message, call.data)                                   #extracts data from the database to form buttons
    series_keyboard=extf.NewMarkupName(series_lis)
    msg_text='We have variety of series. Chose one from the button menu below or press "\start" to return: '

    bot.send_message(call.message.chat.id, msg_text, reply_markup=series_keyboard)                  #show the markup for user to chose series from the ones in the db
    bot.register_next_step_handler(call.message, ChoseSeason)                                       #next stage is letting user chose the season

#function for nadling series season choice

def ChoseSeason(message):
    pf.series_dict={'name':str.lower(message.text)}
    seasons=[] #Here is database call for number of seasons
    season_markup=extf.NewMarkupName(seasons)

    bot.send_message(message.chat.id,text=('You have chosen %s' % message.text),reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id,text='Now chose season:',reply_markup=season_markup)

    bot.register_next_step_handler(message, ChoseEpisode)

#function for nadling series episode choice

def ChoseEpisode(message):
    pf.series_dict={'season':str.lower(message.text)}
    episodes=[] #Here is database call for number of episodes
    episodes_markup=extf.NewMarkupName(episodes)
    bot.send_message(message.chat.id,text='Now chose episode:',reply_markup=episodes_markup)

    #handler for View which will be made through class

    

#callback handler for comics
@bot.callback_query_handler(func=lambda call: call.data=='comics')

def handle_com(call):

    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)         #delete prevoius message to make interface free of unnecessary options
    com_lis=extract_names_from_db(call.message,call.data)                           #extracts data from the database to form buttons
    com_keyboard=extf.NewMarkupName(com_lis)
    bot.send_message(call.message.chat.id, 'We have variety of comics. Chose one from the button menu below or press "\start" to return: ',reply_markup=com_keyboard)
    # bot.register_next_step_handler(call.message, ChoseYear)

#function for hadling comics year of publishing

def ChoseYear(message):
    pf.series_dict={'name':str.lower(message.text)}
    years=[] #Here is database call for number of year in which issue was published
    years_markup=extf.NewMarkupName(years)

    bot.send_message(message.chat.id,text=('You have chosen %s comics' % message.text),reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id,text='Now chose year of publishing:',reply_markup=years_markup)

    bot.register_next_step_handler(message, ChoseIssue)

#function for hadling comics number of issue - depends on comics

def ChoseIssue(message):
    pf.series_dict={'season':str.lower(message.text)}
    issues=[] #Here is database call for number of issues and their numbers in the database
    issues_markup=extf.NewMarkupName(issues)
    bot.send_message(message.chat.id,text='Now chose issue:',reply_markup=issues_markup)

    #handler for View which will be made through class
 


#check database_connection

@bot.message_handler(commands='check_con')                                  #use command /check_con to start the connection checker

def con_check(message):
    try:                                                                        #try for safety of the connection
        connection=connect_to_db()
        if connection.is_connected():
            db_Info = connection.get_server_info()                                      #gets info about mysql version
            cursor = connection.cursor()
            cursor.execute("select database();")                                        #performs db inquery calling database
            record = str(cursor.fetchone()).replace(',','')                             #cathcing and formating reply from the database
            record=(record[1:-1]).replace("'","")                                       #formating reply from the database
            bot.send_message(message.chat.id,'Connected to MySQL Server version '+db_Info)      #message about MySQL server
            bot.send_message(message.chat.id,'Database is connected to the '+str(record))       #message about connections status
            cursor.execute("show tables;")                                              #new inquery for the db to check if exact db contains anything
            record = str(cursor.fetchone()).replace(',','')                             #cathcing and formating reply from the database
            record=(record[1:-1]).replace("'","")                                       #formating reply from the database
            bot.send_message(message.chat.id,'Database contains:\n'+str(record))        #message about db tables

    except Error as er:
        bot.send_message(message.chat.id,'Error: '+er)                                  #if exception is caught sends corresponding message to user
    finally:                                                                            #closing connection in case of successfull connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            bot.send_message(message.chat.id,'Actions performed\nMySQL connection is closed')   #message about successfull closing of the cnnection

bot.infinity_polling()