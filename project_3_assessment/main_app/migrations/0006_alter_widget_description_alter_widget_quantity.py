# Generated by Django 4.0.4 on 2022-07-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_widget_db_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='description',
            field=models.TextField(default=1),
        ),
        migrations.AlterField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(default=2),
        ),
    ]
