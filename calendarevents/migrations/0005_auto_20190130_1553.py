# Generated by Django 2.1.4 on 2019-01-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarevents', '0004_auto_20190128_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventtype',
            options={'verbose_name_plural': 'Event type'},
        ),
        migrations.AlterField(
            model_name='calendar',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='title',
            field=models.TextField(max_length=2000),
        ),
    ]