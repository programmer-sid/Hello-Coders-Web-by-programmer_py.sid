# Generated by Django 3.0.6 on 2020-06-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homescreen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_num', models.IntegerField(max_length=5000)),
                ('date', models.CharField(max_length=12)),
                ('image_url', models.CharField(max_length=2875)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
