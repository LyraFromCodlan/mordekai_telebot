from private_file import API_name
import telegram
TOKEN = 'Замените эту строку на token, полученный от @BotFather'
bot = telegram.Bot(token=API_name)
# Чтобы проверить правильность учетных данных, вызываем метод bot.getMe():
print('bot info in turple: ',bot.get_me())
print('Just bot name: ',bot.name)

updates= bot.get_updates()
print([upd.message.text for upd in updates])

chat_id = bot.get_updates()[-1].message.chat_id  # id чата

for el in updates:
    if 'Update' == el.message.text:
        bot.send_message(chat_id=chat_id, text="Reply to this")
        bot.send_message(chat_id,el.message.text)

print('updates: ',updates)

# bot.send_message(chat_id=chat_id, text="Bamboozeled")


# updates.message.reply_text("I'm sorry Dave I'm afraid I can't do that.")