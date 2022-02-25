# Generated by Django 4.0.2 on 2022-02-24 17:33

from django.db import migrations, models
import mainbot.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbot', '0002_category_post_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('field', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('Arabic', 'ar'), ('English', 'eng'), ('Spanish', 'epo'), ('French', 'fre'), ('Turkish', 'tur'), ('Dutch', 'dut'), ('Chinese', 'chi'), ('Portuguese', 'por'), ('Irish', 'ga'), ('Hebrew', 'he'), ('Indonesian', 'ind'), ('Filipino ', 'fil'), ('Japanese', 'jpn'), ('Russian', 'rus'), ('Hindi', 'hi')], max_length=20)),
                ('pages', models.IntegerField(blank=True)),
                ('author', models.CharField(max_length=35)),
                ('download_link', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=mainbot.models.filepath)),
            ],
        ),
    ]