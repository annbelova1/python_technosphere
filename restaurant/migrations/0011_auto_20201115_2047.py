# Generated by Django 2.2.17 on 2020-11-15 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20201115_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='photo',
            new_name='picture',
        ),
    ]
