# Generated by Django 4.0.2 on 2022-03-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='any_file',
            field=models.FileField(blank=True, null=True, upload_to='router_specifications'),
        ),
    ]
