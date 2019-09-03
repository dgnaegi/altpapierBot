from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from dataStorage.userData import userData
from dataStorage.dataAccess import dataAccess
from helper.argumentParser import argumentParser
import requests
import re
import json

def start(bot, update):
    chatId = update.message.chat_id
    bot.sendMessage(chatId, "Hi, im altpapierBot. Here to remind you about cardboard and paper removal for Zurich. Don't hesitate to contact my master for all forms of complaints: https://twitter.com/igbobledaniel")
    bot.sendMessage(chatId, "Please let me know your ZIP Code by sending it in this format:")
    bot.sendMessage(chatId, "/zip 80XX")

def stop(bot, update):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    bot.sendMessage(chatId, "I've always been happy to help you. Your data got deleted entirely. I'll always be there for you when you need me <3")

def zip(bot, update, args):
    zipCodeOrNull = argumentParser.Parse(args)
    chatId = update.message.chat_id

    if zipCodeOrNull is None:
        bot.sendMessage(chatId, "Invalid input! Please enter a valid postcode of the city of Zurich in this format:")
        bot.sendMessage(chatId, "/zip 80XX")
        return

    data = userData(chatId, zipCodeOrNull)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on for disposal in {} Zurich.".format(zipCodeOrNull))
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
    dp.add_handler(CommandHandler('zip',zip, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()