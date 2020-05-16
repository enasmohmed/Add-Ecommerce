# Generated by Django 2.2.5 on 2020-04-03 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0012_auto_20200403_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='img',
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
