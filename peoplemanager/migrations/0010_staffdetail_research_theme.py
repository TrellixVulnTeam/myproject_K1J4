# Generated by Django 2.2.2 on 2019-06-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoplemanager', '0009_auto_20190626_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdetail',
            name='research_theme',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
    ]