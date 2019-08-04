from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from dataStorage.userData import userData
from dataStorage.dataAccess import dataAccess
import requests
import re

def start(bot, update):
    chatId = update.message.chat_id
    bot.sendMessage(chatId, "Hi, im altpapierBot. Here to remind you about cardboard and paper removal for Zurich.")
    bot.sendMessage(chatId, "Please let me know your ZIP Code by sending it in this format /80XX")

def stop(bot, update):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    bot.sendMessage(chatId, "I've always been happy to help you. Your data got deleted entirely. I'll always be there for you when you need me <3")

def zip8000(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8000)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8004(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8004)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8032(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8032)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8041(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8041)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8047(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8047)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8051(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8051)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8057(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8057)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8143(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8143)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8001(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8001)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8005(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8005)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8037(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8037)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8052(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8052)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8063(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8063)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8044(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8044)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8002(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8002)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8006(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8006)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8038(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8038)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8045(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8045)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8049(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8049)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8053(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8053)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8064(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8064)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8003(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8003)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8008(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8008)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8040(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8040)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8046(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8046)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8050(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8050)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8055(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8055)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8093(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8093)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def zip8048(bot, update):
    chatId = update.message.chat_id
    data = userData(chatId, 8048)
    success = dataAccess.saveUserData(data)
    if success:
        bot.sendMessage(chatId, "Yeah, Gwaltstette! You're setup and will be notified from now on.")
        bot.sendMessage(chatId, "You can unsubscribe by sending /stop")    
    else:
        bot.sendMessage(chatId, "You are already subscribed! Please unsubscribe first by sending /stop")

def main():
    updater = Updater('862960436:AAGcEPWlf3h-reN7wK-yc4J_ORMoYAlt8QA')
    dataAccess.getAllUserdata()
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('stop',stop))
    dp.add_handler(CommandHandler('8000',zip8000))
    dp.add_handler(CommandHandler('8004',zip8004))
    dp.add_handler(CommandHandler('8032',zip8032))
    dp.add_handler(CommandHandler('8041',zip8041))
    dp.add_handler(CommandHandler('8047',zip8047))
    dp.add_handler(CommandHandler('8051',zip8051))
    dp.add_handler(CommandHandler('8057',zip8057))
    dp.add_handler(CommandHandler('8143',zip8143))
    dp.add_handler(CommandHandler('8001',zip8001))
    dp.add_handler(CommandHandler('8005',zip8005))
    dp.add_handler(CommandHandler('8037',zip8037))
    dp.add_handler(CommandHandler('8044',zip8044))
    dp.add_handler(CommandHandler('8048',zip8048))
    dp.add_handler(CommandHandler('8052',zip8052))
    dp.add_handler(CommandHandler('8063',zip8063))
    dp.add_handler(CommandHandler('8002',zip8002))
    dp.add_handler(CommandHandler('8006',zip8006))
    dp.add_handler(CommandHandler('8038',zip8038))
    dp.add_handler(CommandHandler('8045',zip8045))
    dp.add_handler(CommandHandler('8049',zip8049))
    dp.add_handler(CommandHandler('8053',zip8053))
    dp.add_handler(CommandHandler('8064',zip8064))
    dp.add_handler(CommandHandler('8003',zip8003))
    dp.add_handler(CommandHandler('8008',zip8008))
    dp.add_handler(CommandHandler('8040',zip8040))
    dp.add_handler(CommandHandler('8046',zip8046))
    dp.add_handler(CommandHandler('8050',zip8050))
    dp.add_handler(CommandHandler('8055',zip8055))
    dp.add_handler(CommandHandler('8093',zip8093))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()