# Generated by Django 2.2.5 on 2020-04-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200412_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
