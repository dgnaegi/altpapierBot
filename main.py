from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from dataStorage.userData import userData
from dataStorage.dataAccess import dataAccess
from helper.zipCodeParser import zipCodeParser
from helper.areaCodeParser import areaCodeParser
import requests
import re
import json

def start(bot, update):
    chatId = update.message.chat_id
    bot.sendMessage(chatId, "Hi, im altpapierBot. Here to remind you about cardboard and paper removal for Zurich or St.Gallen. For more information enter /help")
    bot.sendMessage(chatId, "For Zurich, please let me know your ZIP Code by sending it in this format:")
    bot.sendMessage(chatId, "/zip 80XX")
    bot.sendMessage(chatId, "For St.Gallen, send your disposal area (A,B,C,...) like this:")
    bot.sendMessage(chatId, "/area X")

def stop(bot, update):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    bot.sendMessage(chatId, "I've always been happy to help you. Your data got deleted entirely. I'll always be there for you when you need me <3")

def help(bot, update):
    chatId = update.message.chat_id
    bot.sendMessage(chatId, "You can find more information and a small tutorial on https://dgnaegi.ch/2020/09/06/altpapierbot/. For further questions do not hesitate to contact my creator: @ignobled")

def zip(bot, update, args):
    zipCodeOrNone = zipCodeParser.Parse(args)
    chatId = update.message.chat_id

    if zipCodeOrNone is None:
        bot.sendMessage(chatId, "Invalid input! Please enter a valid postcode of the city of Zurich in this format:")
        bot.sendMessage(chatId, "/zip 80XX")
        return

    data = userData(chatId, zipCodeOrNone, None)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on for disposal in {}.".format(zipCodeOrNone))
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def area(bot, update, args):
    areaCodeOrNone = areaCodeParser.Parse(args)
    chatId = update.message.chat_id

    if areaCodeOrNone is None:
        bot.sendMessage(chatId, "Invalid input! Please enter a valid disposal area code of the city of St.Gallen in this format:")
        bot.sendMessage(chatId, "/area X")
        bot.sendMessage(chatId, "Valid areas are: A, B, C, D, E, F, G, H, I, J, K, L-OST, L-WEST")
        return
    
    data = userData(chatId, None, areaCodeOrNone)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on for disposal in area {}.".format(areaCodeOrNone))
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def stats(bot, update):
    chatId = update.message.chat_id
    zhUserCount = "Users in Zurich: " + str(len(dataAccess.getZurichUserdata()))
    sgUserCount = "Users in St.Gallen: " + str(len(dataAccess.getStGallenUserdata()))

    bot.sendMessage(chatId, zhUserCount)
    bot.sendMessage(chatId, sgUserCount)

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
    dp.add_handler(CommandHandler('area',area, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
