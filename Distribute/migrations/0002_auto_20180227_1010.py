# Generated by Django 2.0 on 2018-02-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Distribute', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drecord',
            name='record_isVIP',
        ),
        migrations.AddField(
            model_name='drecord',
            name='record_cust_level',
            field=models.IntegerField(default=0),
        ),
    ]
