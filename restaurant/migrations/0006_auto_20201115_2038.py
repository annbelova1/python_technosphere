# Generated by Django 2.2.17 on 2020-11-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20201115_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='picture',
            field=models.ImageField(default='restaurant/static/images/cat.jpeg', upload_to='images/'),
        ),
    ]
