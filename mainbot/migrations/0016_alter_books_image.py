# Generated by Django 4.0.2 on 2022-03-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbot', '0015_remove_books_any_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]