from telebot import TeleBot, types
bot = TeleBot('6314580351:AAFKdtVhqHQBzU5XT2XGIfWva_ljKw6jjkI');
from telebot import types
from telebot.types import Message

ban = {}

@bot.message_handler(commands=["ban"])
def btn_cmd_handler(message):    
    if message.reply_to_message != None:
        if message.reply_to_message.forward_from != None:
            if message.reply_to_message.forward_from.id in ban:                
                ban[message.reply_to_message.forward_from.id] = ban[message.reply_to_message.forward_from.id] + 1
                bot.delete_message(message.chat.id, message.id)
                if ban[message.reply_to_message.forward_from.id] >= 10:
                    print('BAN! ' + str(message.reply_to_message.forward_from.id))
                    ban.pop(message.reply_to_message.forward_from.id)
                    bot.delete_message(message.chat.id, message.reply_to_message.id)
                    bot.ban_chat_member(message.chat.id, message.reply_to_message.forward_from.id)
                    bot.send_message(message.chat.id, 'User was banned by People\'s Inquisition!')
            else:
                ban[message.reply_to_message.forward_from.id] = 1
                bot.delete_message(message.chat.id, message.id)


if __name__ == "__main__":
    bot.infinity_polling()



