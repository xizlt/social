# Generated by Django 3.0.5 on 2020-05-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/default.jpg', upload_to='users/%Y/%m/%d/'),
        ),
    ]
