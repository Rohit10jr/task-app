# Generated by Django 5.0 on 2023-12-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_app_appicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='appicon',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
