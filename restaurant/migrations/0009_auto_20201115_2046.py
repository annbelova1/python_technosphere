# Generated by Django 2.2.17 on 2020-11-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20201115_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='picture',
            new_name='photo',
        ),
    ]
