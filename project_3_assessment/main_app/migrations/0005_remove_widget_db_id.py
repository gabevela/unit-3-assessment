# Generated by Django 4.0.4 on 2022-07-11 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_widget_db_id_widget_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widget',
            name='db_id',
        ),
    ]
