# Generated by Django 4.2 on 2023-05-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardenApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='pic',
            new_name='pic1',
        ),
        migrations.AddField(
            model_name='service',
            name='pic2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='service'),
        ),
    ]
