# Generated by Django 2.1.4 on 2019-04-11 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstnames', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=20000, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('headshot', models.ImageField(upload_to='personimage')),
            ],
            options={
                'verbose_name_plural': 'Person details',
            },
        ),
        migrations.CreateModel(
            name='StaffDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CS', 'Core Staff'), ('RAF', 'Research Associates And Fellows'), ('TSS', 'Technical Support Staff'), ('T', 'Trainees'), ('A', 'Alumni')], max_length=200)),
                ('job_title', models.CharField(max_length=500)),
                ('job_description', models.TextField(blank=True, max_length=20000, null=True)),
                ('appointment_date', models.DateField(max_length=200)),
                ('termination_date', models.DateField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='peoplemanager.PeopleDetail')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.CharField(blank=True, max_length=500, null=True)),
                ('supervisor_additional', models.CharField(blank=True, max_length=500, null=True)),
                ('institution', models.CharField(max_length=500)),
                ('department', models.CharField(blank=True, max_length=500, null=True)),
                ('thesis_title', models.TextField(max_length=10000)),
                ('degree', models.CharField(choices=[('Hns', 'Hns'), ('MSc', 'MSc'), ('PhD', 'PhD'), ('ERF', 'ERF')], max_length=8)),
                ('currently_registered', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=3)),
                ('start_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True, max_length=200, null=True)),
                ('abstract', models.TextField(blank=True, max_length=20000, null=True)),
                ('archivesupload_id', models.CharField(blank=True, max_length=100, null=True)),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='peoplemanager.PeopleDetail')),
            ],
            options={
                'verbose_name_plural': 'Student details',
            },
        ),
    ]