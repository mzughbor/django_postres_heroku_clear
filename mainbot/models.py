import datetime
import os
from django.db import models

# Create your models here.


class TelegramBot(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title + '  .. المحتوى :  ' + self.body


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author + '  .. علق ب .. :  ' + self.body


def filepath(request, filename):
    old_filename = filename
    time_now = datetime.datetime.now().strftime('%Y%m%d%H:%M%S')
    filename = "%s%s" % (time_now, old_filename)
    return os.path.join('media/', filename)


class Books(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    field = models.CharField(max_length=50)
    language_list = (
        ('ar', 'Arabic'),
        ('eng', 'English'),
        ('epo', 'Spanish'),
        ('fre', 'French'),
        ('tur', 'Turkish'),
        ('dut', 'Dutch'),
        ('chi', 'Chinese'),
        ('por', 'Portuguese'),
        ('ga', 'Irish'),
        ('he', 'Hebrew'),
        ('ind', 'Indonesian'),
        ('fil', 'Filipino'),
        ('jpn', 'Japanese'),
        ('rus', 'Russian'),
        ('hi', 'Hindi'),
    )
    language = models.CharField(max_length=20, choices=language_list)
    pages = models.IntegerField(blank=True)
    author = models.CharField(max_length=35)
    download_link = models.TextField(null=False)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    # add field for summeries / ملخصات كتب عشؤاية

    def __str__(self):
        return self.name

