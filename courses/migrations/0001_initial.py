# Generated by Django 3.0.6 on 2020-06-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_of_channel', models.CharField(max_length=2875)),
                ('name_of_channel', models.CharField(max_length=15)),
                ('for_which_language', models.CharField(max_length=15)),
                ('link_of_channel', models.CharField(max_length=2857)),
                ('des_of_channel', models.CharField(max_length=250)),
            ],
        ),
    ]
