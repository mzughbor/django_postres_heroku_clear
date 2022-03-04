import os
import sys
import time
import random

import telepot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telepot.loop import MessageLoop


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegramBot.settings")
import django
import telegram
django.setup()
from mainbot import views
from telegram.update import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, Dispatcher, \
    CallbackQueryHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.bot import Bot

from mainbot.views import books_list_mz

number_counter = 0
word_entered = ''
i = 0

#updater = Updater("5275565416:AAHLyoqmbpLiUtniz2BnBXKMP_v80aBXGus", use_context=True)
updater = Updater("5135627916:AAHN1isdHyJR9VpeuVvCIbGQInrCtoeA-WQ", use_context=True)
from mainbot.models import Post, Books, Poetry, Quotes
dispatcher: Dispatcher = updater.dispatcher


#bot = telepot.Bot('5275565416:AAHLyoqmbpLiUtniz2BnBXKMP_v80aBXGus')
bot = telepot.Bot('5135627916:AAHN1isdHyJR9VpeuVvCIbGQInrCtoeA-WQ')


def start(update: Update, context: CallbackContext, chatId=None):
    """
    the callback for handling start command and create keyboard
    """
    bot: Bot = context.bot
    # bot.telegram.sendMessage(user_id, 'please click below button and give it a number: 1 to 365', )

    kbd_layout = [['إقتباسات عشوائية', 'غذاء معرفي'], ['شعر', 'ملخصات كتب عشوائية'],
                  ["إبحث عن كتاب"]]
    # حكم وأمثال لاغي
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text="من فضلك اختر خياراً من القائمة", reply_markup=kbd)


def remove(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text(text="I'm back.", reply_markup=reply_markup)
    pass


def echo(update: Update, context: CallbackContext):
    keyboard_name = [[
        InlineKeyboardButton('إنقرهنا ثم أخبرني الاسم لكي أستطيع مساعدتك', switch_inline_query_current_chat='/name ')
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard_name)
    update.message.reply_text("من فضلك قم بادخال اسم الكتاب بعد النقر على الزر أدناه", reply_markup=reply_markup)
    time.sleep(2)


def name_book(update: Update, context: CallbackContext):
    """
    function to know what the hell user of the bot searching for  name of book to read ?.
    """
    global i
    global word_entered
    global number_counter
    # print(update.message.text)
    # if update.message.text == '@mzughbot /name ':
    a_string = str(update.message.text)
    sliced = a_string[21:] # 15
    # print([e.name for e in Books.objects.all()])
    after_tra = str(sliced.strip())
    # word_entered = after_tra
    also = [e.name for e in Books.objects.filter(name__contains=after_tra)]  # here where the query happens...
    if len(also) == 0:
        update.message.reply_text("نأسف لا يوجد نتائج بحث مطابقة لدينا, حاول بكتاب اخر...")
        update.message.reply_text("لقد أردت البحث عن ... '%s' " % also)
    else:
        keyboard = [[]]
        counter = 0
        for x in also:
            counter += 1
            update.message.reply_text("نتيجه البحث هي :'%s' " % x)
            keyboard[0].append(InlineKeyboardButton(x, callback_data=counter, switch_inline_query='/name'))

        # print(i, "i'm the i ")
        if len(also) >= 2:
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Please choose:', reply_markup=reply_markup)
            word_entered = after_tra

        if len(also) == 1:
            number_counter = len(also)
            # update.message.reply_text.("اسم الكتاب : ... '%s'" % views.Books.objects.filter(
            # name__contains=after_tra)[0])
            update.message.reply_text(
                "المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[0].author)
            try:
                update.message.reply_text(
                    "الوصف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[0].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")

            update.message.reply_text(
                "تصنيف الكتاب ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[0].field)
            update.message.reply_text(
                "اللغة ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[0].language)
            update.message.reply_text(
                "عدد الصفحات '%s'" % views.Books.objects.filter(name__contains=after_tra)[0].pages)
            update.message.reply_text(
                "رابط التحميل '%s'" % views.Books.objects.filter(name__contains=after_tra)[0].download_link)

            # if not [e.name for e in Books.objects.filter(name__contains=sliced)]:
            # print(views.Books.objects.order_by('name')) # description
            # update.message.reply_text("You just clicked on '%s'" % views.Books.objects.filter(name__startswith='رواية'))


def button(update, context):
    """
    callback method handling button press
    """
    global i
    global word_entered
    query: CallbackQuery = update.callback_query
    query2: CallbackQuery = update.callback_query
    query.answer()
    i = int(format(query.data))
    query.edit_message_text(text="لقد اخترت خيار : {}".format(query.data))
    query2.edit_message_text(chooses(Update, CallbackQuery))

    # views.Books.objects.filter(name__contains=word_entered)[i].description,
    # views.Books.objects.filter(name__contains=word_entered)[i].author)
    # update.callback_query.message.edit_text(str(views.Books.objects.filter(name__contains=word_entered)[i].description))
    # update.callback_query.message.edit_text(str(views.Books.objects.filter(name__contains=word_entered)[i].description))
    # query.edit_message_text("المؤلف  '%s'" % views.Books.objects.filter(name__contains=word_entered)[i-1].author)
    # also = [e.name for e in Books.objects.filter(name__contains=word_entered)]  # here where the query happens...


def chooses(update: Update, context: CallbackQuery):
    global i
    global word_entered
    trigger = 1
    print('god damn ',sys.exc_info()[0])
    try:
        views.Books.objects.filter(name__contains=word_entered)[i - 1].description
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
    else:
        if sys.exc_info()[0] is None:
            return "لقد اخترت خيار رقم : {} \n ".format(i) + \
                   "اسم الكتاب : ... '% s' \n " % views.Books.objects.filter(name__contains=word_entered)[i - 1] + \
                   "المؤلف  '%s' \n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].author + \
                   "الوصف  '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].description + \
                   " تصنيف الكتاب ... '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].field +\
                   "اللغة ... '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].language + \
                   "عدد الصفحات '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].pages + \
                   "رابط التحميل '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].download_link
        else:
            return "لقد اخترت خيار رقم : {} \n ".format(i) + \
                   "اسم الكتاب : ... '% s' \n " % views.Books.objects.filter(name__contains=word_entered)[i - 1] + \
                   "المؤلف  '%s' \n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].author + \
                   " تصنيف الكتاب ... '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].field +\
                   "اللغة ... '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].language + \
                   "عدد الصفحات '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].pages + \
                   "رابط التحميل '%s'\n " % views.Books.objects.filter(name__contains=word_entered)[i - 1].download_link


def randomBooks(update: Update, context: CallbackContext):
    update.message.reply_text("لقد ضغطت على زر  '%s' من فضلك انتظر قليلاً ... " % update.message.text)
    char_list = ['أ', 'ب', 'ت', 'ث', 'ح', 'ج', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف',
                 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    after_tra = str(random.choice(char_list))
    # print(after_tra)
    also = [e.name for e in Books.objects.filter(name__contains=after_tra)]  # here where the query happens...
    while len(also) == 0:
        # if len(also) == 0:
        after_tra = str(random.choice(char_list))
        also = [e.name for e in Books.objects.filter(name__contains=after_tra)]
    #print(len(also))
    if str(update.message.text) == "غذاء معرفي":
        update.message.reply_text("الان سأظهر لك كتاب واحد من المكتبة, استمتع بالقراءة ... ")
        if len(also) == 1:
            i = 1
            update.message.reply_text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1])
            update.message.reply_text("المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].author)
            try:
                update.message.reply_text(
                    "الوصف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")

            update.message.reply_text(
                "تصنيف الكتاب ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].field)
            update.message.reply_text(
                "اللغة ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].language)
            update.message.reply_text(
                "عدد الصفحات '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].pages)
            update.message.reply_text(
                "رابط التحميل '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].download_link)
        else:
            i = random.choice(range(1, len(also)))
            # print("this  my i:", i)
            update.message.reply_text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1])
            update.message.reply_text("المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].author)
            try:
                update.message.reply_text(
                    "الوصف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")

            update.message.reply_text(
                "تصنيف الكتاب ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].field)
            update.message.reply_text(
                "اللغة ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].language)
            update.message.reply_text(
                "عدد الصفحات '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].pages)
            update.message.reply_text(
                "رابط التحميل '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].download_link)
        # endif
    elif str(update.message.text) == "ملخصات كتب عشوائية":
        update.message.reply_text("الان سأظهر لك ملخص لكتاب واحد بشكل عشوائي من المكتبة, استمتع بقرائته ... ")
        if len(also) == 1:
            i = 1
            update.message.reply_text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1])
            update.message.reply_text("المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].author)
            try:
                update.message.reply_text(
                    "الملخص :  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].summaries)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
            update.message.reply_text(
                "عدد صفحات الكتاب '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].pages)
            # let the human know that the pdf is on its way
            bot.sendMessage(update.message.chat.id, "preparing pdf of fresh news, pls wait..")
            # file="rgs_plan_ar_semester_2.pdf"
            # file = "mainbot/Capture.png"
            # media\media
            # file = views.Books.objects.filter()[i-1].image #.url
            for book in books_list_mz:
                if str(book.name) == views.Books.objects.filter(name__contains=after_tra)[i - 1]:
                    file = book.image
                    #specifications_file = book.spec
                    print("I'm the file :", file)
                    file = "media/" + str(file)
                    #specifications_file = "media/" + str(specifications_file)
                    # update.message.reply_text("image '%s'" % file)
                    # send the pdf doc
                    bot.sendDocument(chat_id=update.message.chat.id, document=open(file, 'rb'))
                    #bot.sendDocument(chat_id=update.message.chat.id, document=open(specifications_file, 'rb'))
                    # bot.sendMessage(chat_id, "sorry, I can only deliver news")

        else:
            i = random.choice(range(1, len(also)))
            # let the human know that the pdf is on its way
            bot.sendMessage(update.message.chat.id, "preparing pdf of fresh news, pls wait..")
            for book in books_list_mz:
                if str(book.name) == str(views.Books.objects.filter(name__contains=after_tra)[i - 1]):
                    file = book.image
                    print("I'm the file :", file)
                    # file="rgs_plan_ar_semester_2.pdf"
                    # file = "mainbot/Capture.png"
                    # media\media
                    # file = views.Books.objects.filter()[i-1].image #.url
                    file = "media/" + str(file)
                    #specifications_file = book.spec
                    #specifications_file = "media/" + str(specifications_file)
                    # update.message.reply_text("image '%s'" % file)
                    # send the pdf doc
                    bot.sendDocument(chat_id=update.message.chat.id, document=open(file, 'rb'))
                    #bot.sendDocument(chat_id=update.message.chat.id, document=open(specifications_file, 'rb'))
                    # bot.sendMessage(chat_id, "sorry, I can only deliver news")
                    # print("this  my i:", i)

            update.message.reply_text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1])
            update.message.reply_text("المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].author)
            try:
                update.message.reply_text(
                    "الملخص :  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].summaries)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
            update.message.reply_text(
                "عدد صفحات الكتاب '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].pages)
    else:
        pass


def porty(update: Update, context: CallbackContext):
    """
    This is not the best way to do it >> you have to flip it to .id
    or you've take care of name ?? or decsripsion or what the quiry ?
    """
    char_list = ['أ', 'ب', 'ت', 'ث', 'ح', 'ج', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف',
                 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    after_tra = str(random.choice(char_list))
    also = [e.name for e in Poetry.objects.filter(name__contains=after_tra)]  # here where the query happens...
    while len(also) == 0:
        after_tra = str(random.choice(char_list))
        also = [e.name for e in Poetry.objects.filter(name__contains=after_tra)]
    # print(len(also))

    if str(update.message.text) == "شعر":
        update.message.reply_text("سأقوم بعرض بعض من أبيات الشعر من المكتبة بشكل عشوائي : ")
        if len(also) == 1:
            i = 1
            update.message.reply_text("العنوان  '%s'" % views.Poetry.objects.filter(name__contains=after_tra)[i - 1].name)
            try:
                update.message.reply_text(
                    "--  '%s'" % views.Poetry.objects.filter(name__contains=after_tra)[i - 1].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
        else:
            i = random.choice(range(1, len(also)))
            update.message.reply_text("العنوان  '%s'" % views.Poetry.objects.filter(name__contains=after_tra)[i - 1].name)
            try:
                update.message.reply_text(
                    "--  '%s'" % views.Poetry.objects.filter(name__contains=after_tra)[i - 1].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
        # endif
        # update.message.reply_text(" فضلك أدخل /name أولا ثم الاسم لكي أستطيع مساعدتك !!")


def quotes(update: Update, context: CallbackContext):
    char_list = ['أ', 'ب', 'ت', 'ث', 'ح', 'ج', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف',
                 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    after_tra = str(random.choice(char_list))
    also = [e.name for e in Quotes.objects.filter(name__contains=after_tra)]  # here where the query happens...
    while len(also) == 0:
        after_tra = str(random.choice(char_list))
        also = [e.name for e in Quotes.objects.filter(name__contains=after_tra)]
    # print(len(also))

    if str(update.message.text) == "إقتباسات عشوائية":
        update.message.reply_text("سأقوم بعرض بعض من إقتباسات من المكتبة بشكل عشوائي : ")
        if len(also) == 1:
            i = 1
            update.message.reply_text("العنوان  '%s'" % views.Quotes.objects.filter(name__contains=after_tra)[i - 1].name)
            try:
                update.message.reply_text(
                    "--  '%s'" % views.Quotes.objects.filter(name__contains=after_tra)[i - 1].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
        else:
            i = random.choice(range(1, len(also)))
            update.message.reply_text("العنوان  '%s'" % views.Quotes.objects.filter(name__contains=after_tra)[i - 1].name)
            try:
                update.message.reply_text(
                    "--  '%s'" % views.Quotes.objects.filter(name__contains=after_tra)[i - 1].description)
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    sys.stderr.write("ERROR: '%s' caused by '%s'" % context.error, update)
    pass


def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and msg["text"].lower() == "news":
        # let the human know that the pdf is on its way
        bot.sendMessage(chat_id, "preparing pdf of fresh news, pls wait..")
        # file="rgs_plan_ar_semester_2.pdf"
        file="mainbot/Capture.png"

        # send the pdf doc
        bot.sendDocument(chat_id=chat_id, document=open(file, 'rb'))
    elif content_type == 'text':
        bot.sendMessage(chat_id, "sorry, I can only deliver news")


# MessageLoop(bot, handle).run_as_thread()


dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("remove", remove))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"شعر"), porty))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"إبحث عن كتاب"), echo))    # echo
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"@AlmarbadLib_bot /name"), name_book))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"/name"), name_book))
# updater.dispatcher.add_handler(CommandHandler("name", name_book))
# updater.dispatcher.add_handler(CommandHandler("y", multapil_cho))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"كتب عشوائية"), randomBooks))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"غذاء معرفي"), randomBooks))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"إقتباسات عشوائية"), quotes))
updater.dispatcher.add_error_handler(error)  # error handling
updater.dispatcher.add_handler(CallbackQueryHandler(button))  # handling inline buttons pressing

updater.start_polling()
