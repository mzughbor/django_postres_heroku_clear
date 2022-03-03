from django.contrib import admin

# Register your models here.
from mainbot.models import Post, Category, Books, Poetry, Quotes


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class BooksAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Quotes)
admin.site.register(Poetry)
