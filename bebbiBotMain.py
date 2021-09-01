from dataStorage.userData import userData
from telegram.ext import Updater, CommandHandler
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dataStorage.dataAccessBasel import dataAccess
from helper.areaCodeParser import areaCodeBaselParser
import json
    
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi, im bebbiPapierBot. Here to remind you about cardboard and paper removal for Basel. For more information enter /help")
    update.message.reply_text("Let me know your disposal area (A,B,C,...) like this:")
    update.message.reply_text("/area X")

def stop(update: Update, context: CallbackContext):
    chatId = update.effective_chat.id
    dataAccess.deleteUserData(chatId)
    update.message.reply_text(chatId, "I've always been happy to help you. Your data got deleted entirely. I'll always be there for you when you need me <3")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("You can find more information and a small tutorial on https://dgnaegi.ch/2020/09/06/altpapierbot/. For further questions do not hesitate to contact my creator: @ignobled")

def area(update: Update, context: CallbackContext):
    areaCodeOrNone = areaCodeBaselParser.Parse(context.args)
    chatId = update.message.chat_id

    if areaCodeOrNone is None:
        update.message.reply_text(chatId, "Invalid input! Please enter a valid disposal area code of the city of St.Gallen in this format:")
        update.message.reply_text(chatId, "/area X")
        update.message.reply_text(chatId, "Valid areas are: tbd")
        return
    
    data = userData(chatId, areaCodeOrNone, None)
    success = dataAccess.saveUserData(data)
    if success:
        update.message.reply_text(chatId, "You're setup and will be notified from now on for disposal in area {}.".format(areaCodeOrNone))
        update.message.reply_text(chatId, "You can unsubscribe by sending /stop")
    else:
        update.message.reply_text(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def main():
    with open('./config.json') as data_file:    
            data = json.load(data_file)
            token = data["bebbiToken"]
            
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('stop',stop))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('area',area, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
