# Generated by Django 2.2.5 on 2020-04-11 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0039_auto_20200411_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_ar',
            field=models.CharField(default=None, max_length=600),
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
