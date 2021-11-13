from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dataStorage.userData import userData
from dataStorage.dataAccess import dataAccess
from helper.zipCodeParser import zipCodeParser
from helper.areaCodeParser import areaCodeParser
import json

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi, im altpapierBot. Here to remind you about cardboard and paper removal for Zurich or St.Gallen. For more information enter /help")
    update.message.reply_text("For Zurich, please let me know your postal code by sending it in this format:")
    update.message.reply_text("/zip 80XX")

def stop(update: Update, context: CallbackContext):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    update.message.reply_text("I've always been happy to help you. Your data got deleted entirely. I'll always be there for you when you need me <3")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("You can find more information and a small tutorial on https://dgnaegi.ch/2020/09/06/altpapierbot/. For further questions do not hesitate to contact my creator: @ignobled")

def zip(update: Update, context: CallbackContext):
    zipCodeOrNone = zipCodeParser.Parse(context.args)
    chatId = update.message.chat_id

    if zipCodeOrNone is None:
        update.message.reply_text("Invalid input! Please enter a valid postal code of the city of Zurich in this format:")
        update.message.reply_text("/zip 80XX")
        return

    data = userData(chatId, zipCodeOrNone, None)
    success = dataAccess.saveUserData(data)
    if success:
        update.message.reply_text("You're setup and will be notified from now on for cardboard and paper disposal")
        update.message.reply_text("You can unsubscribe by sending /stop")
    else:
        update.message.reply_text("You are already subscribed! Please unsubscribe first by sending /stop")

def stats(update: Update, context: CallbackContext):
    zhUserCount = "Users in Zurich: " + str(len(dataAccess.getZurichUserdata()))
    sgUserCount = "Users in St.Gallen: " + str(len(dataAccess.getStGallenUserdata()))

    update.message.reply_text(zhUserCount)
    update.message.reply_text(sgUserCount)

def main():
    with open('config.json') as data_file:
            data = json.load(data_file)
            token = data["token"]

    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('stop',stop))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('stats', stats))
    dp.add_handler(CommandHandler('zip',zip, pass_args=True))
    dp.add_handler(CommandHandler('postalcode',zip, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
