# Generated by Django 4.0.2 on 2022-03-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbot', '0011_alter_quotes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
