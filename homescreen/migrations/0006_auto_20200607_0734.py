# Generated by Django 3.0.6 on 2020-06-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homescreen', '0005_auto_20200607_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImageHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=10)),
                ('img_url', models.CharField(max_length=2847)),
            ],
        ),
        migrations.DeleteModel(
            name='BackgroundImageHomescreen',
        ),
    ]