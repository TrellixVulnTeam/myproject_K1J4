# Generated by Django 2.1.4 on 2019-02-05 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwordmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sacemaaccounts',
            old_name='GmailCourseApplications',
            new_name='boardroom_phone',
        ),
        migrations.RenameField(
            model_name='sacemaaccounts',
            old_name='boardroomphone',
            new_name='door_pin',
        ),
        migrations.RenameField(
            model_name='sacemaaccounts',
            old_name='doorpin',
            new_name='gmail_course_applications',
        ),
        migrations.RenameField(
            model_name='sacemaaccounts',
            old_name='eventinvite',
            new_name='pc_lock',
        ),
        migrations.RenameField(
            model_name='sacemaaccounts',
            old_name='pclock',
            new_name='sacema_database',
        ),
        migrations.RenameField(
            model_name='sacemaaccounts',
            old_name='sacemadatabase',
            new_name='sacema_webserver',
        ),
        migrations.RenameField(
            model_name='socialmedia',
            old_name='eventinvite',
            new_name='event_invite',
        ),
        migrations.RemoveField(
            model_name='sacemaaccounts',
            name='sacemawebserver',
        ),
    ]