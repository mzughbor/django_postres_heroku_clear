# Generated by Django 4.0.2 on 2022-03-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbot', '0009_remove_poetry_poetry_id_remove_quotes_quote_id_and_more'),
    ]
    # ('mainbot', '0007_poetry_quotes'),

    operations = [
        migrations.AlterField(
            model_name='poetry',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]