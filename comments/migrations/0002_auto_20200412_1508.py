# Generated by Django 2.2.5 on 2020-04-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]