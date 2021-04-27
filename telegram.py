import telebot
import conf
from time import sleep


class Telegram:

    def __init__(self):
        self.bot = telebot.TeleBot(conf.key_api)
        self.first_send = True

    def send_footer(self):
        if self.first_send:
            self.bot.send_message(conf.chat_id, "👀")
            sleep(5)
            self.first_send = False

    def send(self, text):
        self.bot.send_message(conf.chat_id, text)
