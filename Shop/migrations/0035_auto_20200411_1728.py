# Generated by Django 2.2.5 on 2020-04-11 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0034_auto_20200410_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(default='ريال سعودي', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='currency_ar',
            field=models.CharField(default='ريال سعودي', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description_ar',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ar',
            field=models.CharField(db_index=True, default=11, max_length=200),
            preserve_default=False,
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
