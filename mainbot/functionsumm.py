
def summeries(update: Update, context: CallbackContext):
    """
    function to get random book to read ? . // First option >>
    """
    char_list = ['أ', 'ب', 'ت', 'ث', 'ح', 'ج', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف',
                 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
    after_tra = str(random.choice(char_list))
    print(after_tra)
    also = [e.name for e in Books.objects.filter(name__contains=after_tra)]  # here where the query happens...
    while len(also) == 0:
        # if len(also) == 0:
        after_tra = str(random.choice(char_list))
        also = [e.name for e in Books.objects.filter(name__contains=after_tra)]
    print(len(also))
    if len(also) == 1:
        i = 1
        update.message.text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i-1])

        print("المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].author)
        try:
            print(
                "الوصف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].description)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

        print(
            "تصنيف الكتاب ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].field)
        print(
            "اللغة ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].language)
        print(
            "عدد الصفحات '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].pages)
        print(
            "رابط التحميل '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].download_link)
    else:
        i = random.choice(range(1, len(also)))
        print("this  my i:", i)
        update.message.text("اسم الكتاب : ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i-1])

        print("المؤلف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].author)
        try:
            print(
                "الوصف  '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].description)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

        print(
            "تصنيف الكتاب ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].field)
        print(
            "اللغة ... '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].language)
        print(
            "عدد الصفحات '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].pages)
        print(
            "رابط التحميل '%s'" % views.Books.objects.filter(name__contains=after_tra)[i - 1].download_link)
