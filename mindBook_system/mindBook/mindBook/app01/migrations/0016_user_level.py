# Generated by Django 3.2 on 2021-05-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_alter_userlevel_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.BooleanField(default=False, verbose_name='用户是否有管理员权限'),
        ),
    ]
