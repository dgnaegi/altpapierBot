from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from dataStorage.userData import userData
from dataStorage.dataAccess import dataAccess
from helper.argumentParser import argumentParser
import requests
import re
import json

def start(bot, update):
    chatId = update.message.chat_id
    bot.sendMessage(chatId, "Hi, im altpapierBot. Here to remind you about cardboard and paper removal for Zurich. For more information enter /help")
    bot.sendMessage(chatId, "Please let me know your ZIP Code by sending it in this format:")
    bot.sendMessage(chatId, "/zip 80XX")

def stop(bot, update):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    bot.sendMessage(chatId, "I've always been happy to help you. Your data got deleted entirely. I'll always be there for you when you need me <3")

def help(bot, update):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    bot.sendMessage(chatId, "You can find more information and a small tutorial on http://dgnaegi.ch/blog/altpapierbot. For further questions do not hesitate to contact my creator through twitter: https://twitter.com/ignobledaniel")

def zip(bot, update, args):
    zipCodeOrNone = argumentParser.Parse(args)
    chatId = update.message.chat_id

    if zipCodeOrNone is None:
        bot.sendMessage(chatId, "Invalid input! Please enter a valid postcode of the city of Zurich in this format:")
        bot.sendMessage(chatId, "/zip 80XX")
        return

    data = userData(chatId, zipCodeOrNone)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on for disposal in {} Zurich.".format(zipCodeOrNone))
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")


def main():
    with open('config.json') as data_file:    
            data = json.load(data_file)
            token = data["token"]
            
    updater = Updater(token)
    dataAccess.getAllUserdata()
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('stop',stop))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('zip',zip, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()