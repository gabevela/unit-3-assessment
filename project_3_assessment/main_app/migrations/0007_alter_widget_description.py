# Generated by Django 4.0.4 on 2022-07-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_widget_description_alter_widget_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='description',
            field=models.IntegerField(default=1),
        ),
    ]