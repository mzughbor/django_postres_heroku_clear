import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegramBot.settings")
import django
django.setup()
from mainbot import views
from telegram.update import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.bot import Bot

bot = Bot("5135627916:AAHN1isdHyJR9VpeuVvCIbGQInrCtoeA-WQ")
print(bot.get_me())
# updater = Updater("5275565416:AAHLyoqmbpLiUtniz2BnBXKMP_v80aBXGus", use_context=True)
updater = Updater("5135627916:AAHN1isdHyJR9VpeuVvCIbGQInrCtoeA-WQ", use_context=True)
from mainbot.models import Post, Books

dispatcher: Dispatcher = updater.dispatcher


def start_run(update: Update, context: CallbackContext):
    """
    the callback for handling start command and create keyboard
    """
    bot: Bot = context.bot

    kbd_layout = [['إقتباسات عشوائية', 'كتب عشوائية'], ['شعر', 'ملخصات كتب عشوائية'],
                  ["إبحث عن كتاب"]]
    # حكم وأمثال لاغي
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text="Select Options", reply_markup=kbd)


def remove(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text(text="I'm back.", reply_markup=reply_markup)
    pass


def echo(update: Update, context: CallbackContext):
    """
    message to handle any "Option [0-9]" Regrex.
    """
    print("before")
    if str(update.message.text) == "إبحث عن كتاب":
        # print(views.Books.objects.order_by('name')[0].description)
        # update.message.reply_text("You just clicked on '%s'" % views.Books.objects.filter(name__startswith='رواية'))
        update.message.reply_text("You just clicked on '%s'" % views.Books.objects.filter(name__contains='رواية'))
        print('ok')
        # print([e.name for e in Books.objects.all()])
        print([e.name for e in Books.objects.filter(name__contains='رواية')])
        print('ok')
        update.message.reply_text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains='رواية')[0])
        update.message.reply_text("الوصف ... '%s'" % views.Books.objects.filter(name__contains='رواية')[0].description)

    pass


def randomBooks(update: Update, context: CallbackContext):
    update.message.reply_text("You just clicked on '%s'" % update.message.text)
    print(update.message.text)
    pass


dispatcher.add_handler(CommandHandler("start_run", start_run))
updater.dispatcher.add_handler(CommandHandler("start_run", start_run))
updater.dispatcher.add_handler(CommandHandler("remove", remove))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"إبحث عن كتاب"), echo))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"كتب عشوائية"), randomBooks))

updater.start_polling()

