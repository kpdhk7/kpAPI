# Generated by Django 2.2.3 on 2019-09-22 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankinfo',
            old_name='userate',
            new_name='use_rate',
        ),
    ]