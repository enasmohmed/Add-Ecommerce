# Generated by Django 2.2.5 on 2020-04-04 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0019_auto_20200404_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='interested',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childern', to='Shop.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Shop.Category'),
        ),
    ]