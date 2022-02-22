import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegramBot.settings")

import django
django.setup()

from telegram import Bot
from telegram.update import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove

# bot = Bot("API KEY")
# print(bot.get_me())
updater = Updater("5275565416:AAHLyoqmbpLiUtniz2BnBXKMP_v80aBXGus", use_context=True)
from mainbot.models import Post
dispatcher: Dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command and create keyboard
    """
    bot: Bot = context.bot

    kbd_layout = [['إقتباسات عشوائية', 'كتب عشوائية'], ['Option 3', 'ملخصات كتب عشوائية'],
                  ["إبحث عن كتاب"]]
    # حكم وأمثال
    # converting layout to markup
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
    kbd = ReplyKeyboardMarkup(kbd_layout)

    # sending the reply so as to activate the keyboard
    update.message.reply_text(text="Select Options", reply_markup=kbd)


def remove(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """

    # making a reply markup to remove keyboard
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html
    reply_markup = ReplyKeyboardRemove()

    # sending the reply so as to remove the keyboard
    update.message.reply_text(text="I'm back.", reply_markup=reply_markup)
    pass


def echo(update: Update, context: CallbackContext):
    """
    message to handle any "Option [0-9]" Regrex.
    """
    # sending the reply message with the selected option
    update.message.reply_text("You just clicked on '%s'" % update.message.text)
    print(update.message.text)
    pass


def randomBooks(update: Update, context: CallbackContext):
    update.message.reply_text("You just clicked on '%s'" % update.message.text)
    print(update.message.text)
    pass


dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("remove", remove))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"كتاب"), echo))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"كتب عشوائية"), randomBooks))

updater.start_polling()

