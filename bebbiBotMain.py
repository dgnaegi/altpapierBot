from dataStorage.userData import userData
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dataStorage.dataAccessBasel import dataAccess
from helper.areaCodeParser import areaCodeBaselParser
import json
    
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Sali, ich bi dr bebbi papier bot. Ich bi do zum di für d Karton- und Papierentsorgig in Basel z erinnere. Für meh Informatione, druck uf /hilf")
    update.message.reply_text("Sag mir bitte weli Entsorgigszone (A-H) für di zuetrifft")
    update.message.reply_text("bspw.: /area X")

def stop(update: Update, context: CallbackContext):
    chatId = update.effective_chat.id
    dataAccess.deleteUserData(chatId)
    update.message.reply_text("Freut mi, dassi dir ha könne hälfe. Dini Date sind gänzlich glöscht worde. Bi witerhin do wenn wieder mini hilf bruuchsch <3")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Meh Informatione sowie au e kleins Tutorial findsch uf https://dgnaegi.ch/2020/09/06/altpapierbot/. Für witeri Frooge kasch au dr Entwickler diräkt kontaktiere: @ignobled")

def area(update: Update, context: CallbackContext):
    areaCodeOrNone = areaCodeBaselParser.Parse(context.args)
    chatId = update.message.chat_id

    if areaCodeOrNone is None:
        update.message.reply_text("Ungültigi igob! Bitte gib e gültigi Entsorgigszone im Ruum Basel (A-H) in dem Format ii:")
        update.message.reply_text("/area X")
        return
    
    data = userData(chatId, None, areaCodeOrNone)
    success = dataAccess.saveUserData(data)
    if success:
        update.message.reply_text("Du bisch igrichtet und wirdsch ab jetzt benochrichtigt sobald Karton- und Papierentsorgig in dinere Zone stattfindet.")
        update.message.reply_text("Du kasch di vo de Benochrichtige abmelde indem du /stop itiippsch")
    else:
        update.message.reply_text("Du hesch di scho agmäldet! Bitte mäld di doch zersch ab, in dem du /stop i tippsch")

def main():
    with open('config.json') as data_file:    
            data = json.load(data_file)
            token = data["bebbiToken"]
            
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('stop',stop))
    dp.add_handler(CommandHandler('hilf',help))
    dp.add_handler(CommandHandler('area',area, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
