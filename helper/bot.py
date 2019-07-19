import telegram

class bot:
    def __init__(self, token):
        self.token = token
        self.telegramBot = telegram.Bot(token=token)

    def SendMessage(self, chatId, text):
        self.telegramBot.sendMessage(chatId, text)