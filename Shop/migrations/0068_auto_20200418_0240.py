# Generated by Django 2.2.5 on 2020-04-18 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0067_auto_20200418_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_fi',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ur',
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
