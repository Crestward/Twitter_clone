# Generated by Django 3.2.5 on 2021-07-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210703_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
