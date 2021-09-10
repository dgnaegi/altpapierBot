from dataStorage.userData import userData
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dataStorage.dataAccessBasel import dataAccess
from helper.areaCodeParser import areaCodeBaselParser
import json
    
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Sali, ych bi dr «Bebbi Bapyyr Bot». Ych bi doo, zem di an d Karton- und Bapyyrentsorgig in Baasel z erinnere. Fir mee Informazioone, drugg uf /hilf")
    update.message.reply_text("Saag mir bitte, weeli Entsorgigszoone (A-H) fir di zuedrifft")
    update.message.reply_text("Bsp.: /area X")

def stop(update: Update, context: CallbackContext):
    chatId = update.message.chat_id
    dataAccess.deleteUserData(chatId)
    update.message.reply_text("Frait mi, dass ych dir ha kenne hälfe. Dyyni Daate sind gänzlig glescht worde. Ych bi wyterhin doo, wenn wider myyni Hilf bruuchsch <3")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Mee Informazioone sowie au e glains Tutorial findsch uf https://dgnaegi.ch/2020/09/06/altpapierbot/. Fir wyteri Frooge kasch au dr Entwiggler diräggt aaschryybe: @ignobled")

def area(update: Update, context: CallbackContext):
    areaCodeOrNone = areaCodeBaselParser.Parse(context.args)
    chatId = update.message.chat_id

    if areaCodeOrNone is None:
        update.message.reply_text("Ungiltig Yygob! Bitte gib e giltig Entsorgigszoone im Ruum Baasel (A-H) in däm Formaat yy:")
        update.message.reply_text("/area X")
        return
    
    data = userData(chatId, None, areaCodeOrNone)
    success = dataAccess.saveUserData(data)
    if success:
        update.message.reply_text("Du bisch yygrichtet und wirsch ab jetz benoochrichtigt, sobald e Karton- und Bapyyrentsorgig in dyynere Zoone stattfindet.")
        update.message.reply_text("Du kasch di vo de Benoochrichtige abmälde, indäm du /stop yytippsch")
    else:
        update.message.reply_text("Du hesch di scho aagmolde! Bitte mäld di doch zersch ab, indäm du /stop yytippsch")

def main():
    with open('config.json') as data_file:    
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
