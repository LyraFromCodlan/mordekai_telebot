#some of libraries were imported numerous times, because it's more convenient than stack them all in 1 file, but
#  some extensive functions will be in the main file, because of how the bot works
import telebot
from telebot import types
from mysql.connector import connect, Error


#functions for telebots handler
def NewMarkupName(name_lis):                                            #names keyboard_generator
    new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for el in name_lis:
        new_markup.add(types.KeyboardButton(text=el))
    return new_markup

def NewMarkupCommand(com_lis):                                          #command keyboard generator
    new_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for el in com_lis:
        new_markup.add(types.KeyboardButton(text='/'+el))
    return new_markup

def NewInlineMarkup(name_dict: dict):
    new_keyboard=[]
    for name,call_data in name_dict.items():
        new_keyboard.append([types.InlineKeyboardButton(text=name,callback_data=call_data)])
    new_markup=types.InlineKeyboardMarkup(row_width=3,keyboard=new_keyboard)
    return new_markup

